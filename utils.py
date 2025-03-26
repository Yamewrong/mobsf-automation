import subprocess

def get_device_identifier():
    """
    연결된 ADB 디바이스(에뮬레이터)의 identifier(예: emulator-5554)를 반환합니다.
    여러 디바이스가 있을 경우 첫 번째 항목을 반환합니다.
    """
    try:
        output = subprocess.check_output(['adb', 'devices'], encoding='utf-8')
        lines = output.strip().split('\n')

        if len(lines) <= 1:
            print("[❌] ADB 디바이스 목록이 비어 있습니다. 에뮬레이터가 실행 중인지 확인하세요.")
            return None

        for line in lines[1:]:
            if '\tdevice' in line:
                identifier = line.split('\t')[0]
                print(f"[+] 연결된 디바이스 식별자: {identifier}")
                return identifier

        print("[❌] 실행 중인 ADB 디바이스를 찾지 못했습니다.")
    except subprocess.CalledProcessError as e:
        print(f"[❌] ADB 호출 실패: {e}")
    except Exception as e:
        print(f"[❌] 예기치 않은 오류: {e}")
    
    return None
