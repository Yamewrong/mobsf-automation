import requests
import json
import subprocess
import time
import traceback
from config import MOBS_F_API_KEY, MOBS_F_URL


def tap(x, y, delay=1):
    subprocess.call(["adb", "shell", "input", "tap", str(x), str(y)])
    time.sleep(delay)


def back():
    subprocess.call(["adb", "shell", "input", "keyevent", "4"])
    time.sleep(1)


def auto_login():
    print("[*] 자동 로그인 시도 중...")
    tap(150, 350)  # Username 입력칸
    subprocess.call(["adb", "shell", "input", "text", "devadmin"])
    time.sleep(1)
    tap(380, 600)  # Login 버튼 클릭
    print("[✅] 자동 로그인 완료")


def should_auto_login():
    """현재 화면이 로그인 화면인지 확인"""
    try:
        output = subprocess.check_output(
            ['adb', 'shell', 'dumpsys', 'window', 'windows'], encoding='utf-8'
        )
        if "com.android.insecurebankv2/.PostLogin" in output:
            print("[🔄] 이미 PostLogin 화면이므로 로그인 생략")
            return False
    except Exception as e:
        print(f"[❌] 현재 액티비티 확인 실패: {e}")
    return True


def auto_start_postlogin_activities(apk_hash):
    print("[*] Exported Activities 실행 시작")
    headers = {"Authorization": MOBS_F_API_KEY}
    activities = [
        "com.android.insecurebankv2.DoTransfer",
        "com.android.insecurebankv2.ViewStatement",
        "com.android.insecurebankv2.ChangePassword"
    ]

    for act in activities:
        print(f"[+] 실행 요청: {act}")
        try:
            resp = requests.post(
                f"{MOBS_F_URL}/api/v1/android/start_activity",
                headers=headers,
                data={"hash": apk_hash, "activity": act}
            )
            if resp.status_code == 200:
                print(f"[✅] {act} 실행 완료")
                if should_auto_login():
                    auto_login()
            else:
                print(f"[❌] 실행 실패 ({act}): {resp.status_code} | {resp.text}")
        except Exception as e:
            print(f"[❌] {act} 실행 중 예외 발생: {e}")
        time.sleep(3)


def start_activity(apk_hash, activity_name=None):
    """Exported Activity 자동 추출 및 실행"""
    headers = {'Authorization': MOBS_F_API_KEY}
    try:
        apps_resp = requests.get(f"{MOBS_F_URL}/api/v1/dynamic/get_apps", headers=headers)
        apk_list = apps_resp.json().get("apks", [])
        package_name = next((app.get("PACKAGE_NAME") for app in apk_list if app.get("MD5") == apk_hash), None)
        print(f"[+] 패키지명: {package_name}")

        report_resp = requests.post(
            f"{MOBS_F_URL}/api/v1/report_json",
            headers=headers,
            data={"hash": apk_hash}
        )
        report = report_resp.json() if report_resp.status_code == 200 else {}
        raw_exported = report.get("exported_activities", [])
        exported_activities = (
            json.loads(raw_exported.replace("'", '"')) if isinstance(raw_exported, str) else raw_exported
        )

        if not exported_activities:
            print("[❌] Exported Activity 없음")
            return

        target = activity_name or exported_activities[0]
        print(f"[+] 자동 선택된 Activity: {target}")

        start_resp = requests.post(
            f"{MOBS_F_URL}/api/v1/android/start_activity",
            headers=headers,
            data={"hash": apk_hash, "activity": target}
        )

        if start_resp.status_code == 200:
            print("[✅] Activity 실행 성공")
        else:
            print(f"[❌] 실행 실패: {start_resp.status_code} | {start_resp.text}")

    except Exception as e:
        print(f"[❌] 오류 발생: {type(e).__name__} | {e}")
        traceback.print_exc()
