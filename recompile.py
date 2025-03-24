import subprocess

def recompile_apk(decoded_dir, output_apk):
    print("[3] 리컴파일 중...")
    subprocess.run(["java", "-jar", r"C:\semi-2\apktool_2.11.1.jar", "b", decoded_dir, "-o", output_apk], check=True)

if __name__ == "__main__":
    recompile_apk("sample_decoded", "sample_rebuilt.apk")
