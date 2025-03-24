import requests
import json
import time

def analyze_with_mobsf(apk_path, api_key, mobsf_url="http://127.0.0.1:8000"):
    print("[5] 📤 MobSF 분석 중...")

    headers = {'Authorization': api_key}

    # 1. 업로드
    with open(apk_path, 'rb') as f:
        files = {
            'file': ('sample_signed.apk', f, 'application/vnd.android.package-archive')
        }
        upload_resp = requests.post(f'{mobsf_url}/api/v1/upload', files=files, headers=headers)
        upload_data = upload_resp.json()
        print(f"📦 업로드 응답: {upload_data}")

    apk_hash = upload_data.get('hash')
    if not apk_hash:
        print("[❌] 해시값 없음. 업로드 실패.")
        return

    # 2. 분석 요청
    scan_data = {
        'scan_type': 'apk',
        'file_name': upload_data['file_name'],
        'hash': apk_hash
    }
    scan_resp = requests.post(f'{mobsf_url}/api/v1/scan', data=scan_data, headers=headers)
    print("🔎 분석 요청 완료")

    # 3. 분석 결과 가져오기 (POST로!)
    report_json_url = f'{mobsf_url}/api/v1/report_json'
    data = {'hash': apk_hash}

    for i in range(20):
        time.sleep(1.5)
        report_resp = requests.post(report_json_url, data=data, headers=headers)
        if report_resp.status_code == 200 and report_resp.text.strip():
            try:
                report = report_resp.json()
                print(f"[✅] 분석 결과 수신 완료! (시도 {i+1}/20)")
                break
            except Exception:
                print(f"[⚠️] JSON 파싱 실패, 재시도 중... ({i+1}/20)")
        else:
            print(f"[⏳] 결과 대기 중... ({i+1}/20)")
    else:
        print("[❌] 분석 결과를 끝내 받지 못했습니다.")
        return

    # 4. 저장
    with open("report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=4)

    print("[✅] 분석 완료! report.json 저장됨")
