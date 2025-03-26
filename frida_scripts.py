from pathlib import Path

def get_combined_frida_script():
    script_dir = Path(__file__).parent / "frida_scripts"
    scripts = [
        "bypass_anti_vm.js",
        "bypass_root_detection.js",  # 루팅 우회 스크립트 추가
    ]

    combined = ""
    for script in scripts:
        path = script_dir / script
        if path.exists():
            combined += f"\n// === {script} ===\n"
            combined += path.read_text(encoding='utf-8')
        else:
            combined += f"\n// === {script} NOT FOUND ===\n"

    return combined
