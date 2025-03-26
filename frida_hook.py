import requests
from config import MOBS_F_API_KEY, MOBS_F_URL
from utils import get_device_identifier
from frida_scripts import get_combined_frida_script
import json

def apply_frida_hooks(apk_hash, package_name):
    print("[*] Frida 후킹 적용 시작")

    identifier = get_device_identifier()
    if not identifier:
        print("[❌] ADB 디바이스 식별 실패")
        return

    # 병합된 스크립트 불러오기
    frida_code = get_combined_frida_script() or ""

    url = f"{MOBS_F_URL}/api/v1/frida/instrument"
    headers = {
        "Authorization": MOBS_F_API_KEY
        # Content-Type 생략 → form-urlencoded 로 전송됨!
    }

    payload = {
        "hash": apk_hash,
        "identifier": identifier,
        "new_package": package_name,
        "frida_code": frida_code,
        "frida_action": "spawn",
        "frida_scripts": "sslpinning,apimonitor,root",  # ✅ 문자열 쉼표 구분, 배열 아님
        "default_hooks": "sslpinning,apimonitor",          # ✅ 꼭 포함
        "auxiliary_hooks": "root,clipboard,debugger"
    }

    print("[DEBUG] 보내는 Payload:\n" + json.dumps(payload, indent=2))

    try:
        response = requests.post(url, data=payload, headers=headers)  # ✅ data= 사용!
        if response.status_code == 200:
            print("[✅] Frida 후킹 적용 완료")
        else:
            print(f"[❌] Frida 후킹 실패: {response.status_code} | {response.text}")
    except Exception as e:
        print(f"[❌] Frida 후킹 중 예외 발생: {e}")
