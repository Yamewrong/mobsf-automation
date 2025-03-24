import subprocess

def decompile_apk(apk_path, output_dir):
    print("[1] 디컴파일 중...")

    apktool_jar = r"C:\semi-2\apktool_2.11.1.jar"##jar 파일 경로 넣어주세요
    subprocess.run([
        "java", "-jar", apktool_jar,
        "d", apk_path,
        "-o", output_dir,
        "-f"
    ], check=True)

if __name__ == "__main__":
    decompile_apk("sample.apk", "sample_decoded")
