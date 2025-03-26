# main.py

from decompile import decompile_apk
from decrypt import decrypt_all_candidates
from recompile import recompile_apk
from sign import sign_apk
from mobsf import analyze_with_mobsf
from dynamic_analysis import start_dynamic_analysis

# 파일 경로 및 설정
APK_ORIGINAL = "sample.apk"
APK_DECOMPILED_DIR = "sample_decoded"
APK_REBUILT = "sample_rebuilt.apk"
APK_SIGNED = "sample_signed.apk"
ENCRYPTION_KEY = "dbcdcfghijklmaop"

KEYSTORE_PATH = "my-release-key.jks"
KEY_ALIAS = "mykey"
KEY_PASSWORD = "qwe123"
MOBSF_API_KEY = "8be9d6173cc21a8e60552334050cfe71c02c8e935bdf4b805354b2fe5bc77a0e"  # 보안상 실제 키는 깃헙에 올리지 않도록 주의!
MOBSF_URL = "http://127.0.0.1:8000"

def run_analysis():
    print("\n🚀 [0] MobSF 자동 분석 파이프라인 시작!\n")

    try:
        print("[1] APK 디컴파일")
        decompile_apk(APK_ORIGINAL, APK_DECOMPILED_DIR)

        print("[2] 암호화된 DEX 자동 복호화")
        decrypt_all_candidates(APK_DECOMPILED_DIR, ENCRYPTION_KEY)

        print("[3] APK 리컴파일")
        recompile_apk(APK_DECOMPILED_DIR, APK_REBUILT)

        print("[4] APK 서명")
        sign_apk(KEYSTORE_PATH, KEY_ALIAS, KEY_PASSWORD, APK_REBUILT, APK_SIGNED)

        print("[5] MobSF 정적 분석 시작")
        result = analyze_with_mobsf(APK_SIGNED, MOBSF_API_KEY)
        apk_hash = result["hash"]
        package_name = result["package_name"]

        print("[6] MobSF 동적 분석 (자동 로그인 + Exported Activity 실행)")
        start_dynamic_analysis(apk_hash=apk_hash, package_name=package_name, use_frida=True)

        print("\n🎉 분석 완료! report.json 및 final_dynamic_report.json 확인!\n")

    except Exception as e:
        print(f"[❌] 전체 자동 분석 중 오류 발생: {e}")

if __name__ == "__main__":
    run_analysis()
