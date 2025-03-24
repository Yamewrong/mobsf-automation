from decompile import decompile_apk
from decrypt import decrypt_all_candidates
from recompile import recompile_apk
from sign import sign_apk
from mobsf import analyze_with_mobsf
import os

# 경로 및 설정
APK_ORIGINAL = "sample.apk"
APK_DECOMPILED_DIR = "sample_decoded"
APK_REBUILT = "sample_rebuilt.apk"
APK_SIGNED = "sample_signed.apk"
ENCRYPTION_KEY = "dbcdcfghijklmaop"

KEYSTORE_PATH = "my-release-key.jks"
KEY_ALIAS = "mykey"
KEY_PASSWORD = "생성한 비밀번호호"

MOBSF_API_KEY = "💥여기에_API_KEY_넣기💥"  # 꼭 바꿔줘!

if __name__ == "__main__":
    print("\n🚀 [0] 시작: APK 자동 분석 파이프라인\n")

    # 1. 디컴파일
    decompile_apk(APK_ORIGINAL, APK_DECOMPILED_DIR)

    # 2. 자동 복호화
    decrypt_all_candidates(APK_DECOMPILED_DIR, ENCRYPTION_KEY)

    # 3. 리컴파일
    recompile_apk(APK_DECOMPILED_DIR, APK_REBUILT)

    # 4. 서명
    sign_apk(KEYSTORE_PATH, KEY_ALIAS, KEY_PASSWORD, APK_REBUILT, APK_SIGNED)

    # 5. MobSF 업로드 및 분석
    analyze_with_mobsf(APK_SIGNED, MOBSF_API_KEY)

    print("\n🎉 모든 단계 완료! report.json에서 결과를 확인하세요.\n")
