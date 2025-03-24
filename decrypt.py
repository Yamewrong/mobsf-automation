import os
from Crypto.Cipher import AES

def decrypt_all_candidates(base_dir, key):
    print("[2] 🔍 복호화 대상 자동 탐지 중...")

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".dex") or file.endswith(".bin") or file.endswith(".dat"):
                full_path = os.path.join(root, file)
                print(f"[🤔] 후보 파일 발견: {full_path}")
                
                try:
                    with open(full_path, 'rb') as f:
                        data = f.read()

                    cipher = AES.new(key.encode(), AES.MODE_ECB)
                    decrypted = cipher.decrypt(data)

                    # DEX 헤더 확인
                    if decrypted.startswith(b'dex\n'):
                        out_path = os.path.join(base_dir, "classes.dex")
                        with open(out_path, 'wb') as f:
                            f.write(decrypted)
                        print(f"[✅] 복호화 성공 → 저장 위치: {out_path}")
                        return True  # 첫 번째 성공만 저장

                    else:
                        print(f"[⚠️] 복호화 성공했지만 DEX 파일이 아님: {file}")

                except Exception as e:
                    print(f"[❌] 복호화 실패: {file} → {e}")

    print("[🔚] 복호화된 DEX를 찾지 못했습니다.")
    return False
