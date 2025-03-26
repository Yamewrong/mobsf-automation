import requests
import time
import json
import subprocess
from config import MOBS_F_API_KEY, MOBS_F_URL
from frida_hook import apply_frida_hooks
from utils import get_device_identifier
from activity_starter import auto_login, should_auto_login, auto_start_postlogin_activities

EXPORTED_ACTIVITIES = [
    "com.android.insecurebankv2.PostLogin",
    "com.android.insecurebankv2.DoTransfer",
    "com.android.insecurebankv2.ViewStatement",
    "com.android.insecurebankv2.ChangePassword"
]

def stop_dynamic_analysis(apk_hash):
    print("[*] 동적 분석 종료 요청 (/stop_analysis)")
    try:
        resp = requests.post(
            f"{MOBS_F_URL}/api/v1/dynamic/stop_analysis",
            headers={"Authorization": MOBS_F_API_KEY},
            data={"hash": apk_hash}
        )
        if resp.status_code == 200:
            print("[✅] stop_analysis 호출 완료")
        else:
            print(f"[❌] stop_analysis 실패: {resp.status_code} | {resp.text}")
    except Exception as e:
        print(f"[❌] stop_analysis 예외 발생: {e}")

def start_dynamic_analysis(apk_hash, package_name, use_frida=False):
    print("[*] MobSF 동적 분석 시작")
    headers = {"Authorization": MOBS_F_API_KEY}

    identifier = get_device_identifier()
    if not identifier:
        print("[❌] ADB 디바이스 식별 실패")
        return

    # 1. MobSFy 디바이스 구성
    try:
        resp = requests.post(
            f"{MOBS_F_URL}/api/v1/android/mobsfy",
            headers=headers,
            data={"identifier": identifier}
        )
        if resp.status_code == 200:
            print("[✅] 디바이스 구성 완료")
        else:
            print(f"[❌] 디바이스 구성 실패: {resp.status_code} | {resp.text}")
            return
    except Exception as e:
        print(f"[❌] mobsfy 예외 발생: {e}")
        return

    # 2. Frida 후킹 (옵션)
    if use_frida:
        apply_frida_hooks(apk_hash, package_name)

    # 3. 동적 분석 세션 시작
    try:
        resp = requests.post(
            f"{MOBS_F_URL}/api/v1/dynamic/start_analysis",
            headers=headers,
            data={"hash": apk_hash, "re_install": "1", "install": "1"}
        )
        if resp.status_code == 200:
            print("[✅] 동적 분석 세션 시작됨")
        else:
            print(f"[❌] start_analysis 실패: {resp.status_code} | {resp.text}")
            return
    except Exception as e:
        print(f"[❌] start_analysis 예외 발생: {e}")
        return

    time.sleep(5)

    # 4. Exported Activity 실행 + 자동화 흐름
    for idx, activity in enumerate(EXPORTED_ACTIVITIES):
        print(f"[→] 실행 중: {activity}")
        try:
            act_resp = requests.post(
                f"{MOBS_F_URL}/api/v1/android/start_activity",
                headers=headers,
                data={"hash": apk_hash, "activity": activity}
            )
            if act_resp.status_code == 200:
                print(f"[✅] 실행 완료: {activity}")
                if idx == 0 and should_auto_login():
                    auto_login()
                    auto_start_postlogin_activities(apk_hash)
            else:
                print(f"[❌] 실행 실패 ({activity}): {act_resp.status_code} | {act_resp.text}")
        except Exception as e:
            print(f"[❌] Activity 실행 예외: {e}")

        time.sleep(3)

    # 5. 분석 종료
    stop_dynamic_analysis(apk_hash)

    # 6. 리포트 다운로드 (JSON)
    print("[*] 동적 분석 최종 리포트 다운로드")
    for i in range(10):
        time.sleep(5)
        try:
            report_resp = requests.post(
                f"{MOBS_F_URL}/api/v1/dynamic/report_json",
                headers=headers,
                data={"hash": apk_hash}
            )
            if report_resp.status_code == 200 and "error" not in report_resp.text:
                with open("final_dynamic_report.json", "w", encoding="utf-8") as f:
                    f.write(report_resp.text)
                print("[✅] 동적 분석 결과 저장 완료 (final_dynamic_report.json)")
                return
            else:
                print(f"[...] 리포트 생성 대기 중... ({i + 1}/10)")
        except Exception as e:
            print(f"[❌] 리포트 요청 예외: {e}")

    print("[❌] 최종 리포트 저장 실패")
