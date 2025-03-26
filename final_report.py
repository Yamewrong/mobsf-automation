import requests
import time
from config import MOBS_F_API_KEY, MOBS_F_URL

def stop_dynamic_analysis(apk_hash):
    """동적 분석 종료 API 호출 (MobSF 내부 리포트 생성을 유도함)"""
    print("[*] MobSF 동적 분석 종료 요청 중...")
    url = f"{MOBS_F_URL}/api/v1/dynamic/stop_analysis"
    headers = {'Authorization': MOBS_F_API_KEY}
    data = {"hash": apk_hash}

    try:
        resp = requests.post(url, data=data, headers=headers)
        if resp.status_code == 200:
            print("[✅] 분석 종료 요청 성공")
        else:
            print(f"[❌] 분석 종료 요청 실패: {resp.status_code} | {resp.text}")
    except Exception as e:
        print(f"[❌] 분석 종료 중 예외 발생: {e}")

def download_dynamic_report(apk_hash, max_retries=10, delay=5):
    """최종 리포트 다운로드 (자동 재시도 포함)"""
    print("[*] 동적 분석 최종 리포트 다운로드 요청 시작")

    url = f"{MOBS_F_URL}/api/v1/dynamic/report_json"
    headers = {'Authorization': MOBS_F_API_KEY}
    data = {"hash": apk_hash}

    for i in range(max_retries):
        try:
            response = requests.post(url, data=data, headers=headers)
            if response.status_code == 200 and "error" not in response.text.lower():
                with open("final_dynamic_report.json", "w", encoding="utf-8") as f:
                    f.write(response.text)
                print("[✅] 최종 리포트 저장 완료 (final_dynamic_report.json)")
                return
            else:
                print(f"[...] 리포트 생성 대기 중... ({i + 1}/{max_retries})")
        except Exception as e:
            print(f"[❌] 리포트 요청 중 예외 발생: {e}")

        time.sleep(delay)

    print(f"[❌] 리포트 저장 실패 최종: {response.text if 'response' in locals() else '요청 실패'}")


# ✅ 추가: 정적 분석 PDF 저장
def download_static_pdf(apk_hash, filename="static_report.pdf"):
    print("[📄] 정적 분석 PDF 다운로드 중...")
    url = f"{MOBS_F_URL}/api/v1/download_pdf"
    headers = {'Authorization': MOBS_F_API_KEY}
    data = {"hash": apk_hash}

    try:
        response = requests.post(url, data=data, headers=headers)
        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"[✅] 정적 PDF 저장 완료 → {filename}")
        else:
            print(f"[❌] 정적 PDF 저장 실패: {response.status_code} | {response.text}")
    except Exception as e:
        print(f"[❌] 정적 PDF 요청 중 예외 발생: {e}")


# ✅ 추가: 동적 분석 PDF 저장
def download_dynamic_pdf(apk_hash, filename="dynamic_report.pdf"):
    print("[📄] 동적 분석 PDF 다운로드 중...")
    url = f"{MOBS_F_URL}/api/v1/dynamic/download_pdf"
    headers = {'Authorization': MOBS_F_API_KEY}
    data = {"hash": apk_hash}

    try:
        response = requests.post(url, data=data, headers=headers)
        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"[✅] 동적 PDF 저장 완료 → {filename}")
        else:
            print(f"[❌] 동적 PDF 저장 실패: {response.status_code} | {response.text}")
    except Exception as e:
        print(f"[❌] 동적 PDF 요청 중 예외 발생: {e}")
