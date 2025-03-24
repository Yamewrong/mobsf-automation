import subprocess

def sign_apk(keystore, alias, password, input_apk, output_apk):
    print("[4] APK 서명 중...")
    apksigner_path = r"C:\Users\susud\AppData\Local\Android\Sdk\build-tools\36.0.0\apksigner.bat"
    subprocess.run([
        apksigner_path, "sign",
        "--ks", keystore,
        "--ks-key-alias", alias,
        "--ks-pass", f"pass:{password}",
        "--out", output_apk,
        input_apk
    ], check=True)

if __name__ == "__main__":
    sign_apk(
        keystore="my-release-key.jks",
        alias="mykey",
        password="qwe123",  # 테스트용 비밀번호
        input_apk="sample_rebuilt.apk",
        output_apk="sample_signed.apk"
    )
