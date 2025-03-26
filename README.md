🔐 MobAutoAnalyzer - MobSF 기반 Android 앱 분석 자동화 프로젝트

MobAutoAnalyzer는 Android 앱(APK)의 정적 및 동적 분석을 MobSF와 Frida를 활용하여 자동화한 프로젝트입니다.
에뮬레이터 루팅, Frida 후킹을 포함한 실제 침투 테스트 환경과 유사한 분석 파이프라인을 제공합니다.

🎯 프로젝트 목표
MobSF 구조 및 API 활용법 습득

암호화된 DEX 파일 분석 및 자동 복호화

루팅된 에뮬레이터 연동 및 탐지 우회 (Frida 후킹)

MobSF를 이용한 정적/동적 분석 자동화

MobSF API 기반의 완전 자동화된 분석 파이프라인 구축

🛠️ 사용 기술 및 도구
분석 환경: MobSF, Android Emulator (AVD)

APK 분석 및 조작: Apktool, Apksigner

암호화 복호화: AES-128/ECB (PyCryptodome)

에뮬레이터 컨트롤: ADB (Android Debug Bridge)

후킹 및 탐지 우회: Frida

자동화 스크립트 개발: Python 3.11, Requests, Subprocess

📂 프로젝트 구조
MobAutoAnalyzer/
├── 📜 sample.apk                  # 분석 대상 APK  
├── 📜 decoded_apk/                # 디컴파일된 APK 파일  
├── 📜report.json                # 정적 분석 결과 보고서  
├── 📜final_dynamic_report.json  # 동적 분석 결과 보고서  
├── 📜 main.py                     # 전체 자동화 파이프라인 실행 스크립트  
├── 📜 config.py                   # 환경 설정 (API 키 등)  
├── 📜 decompile.py                # APK 디컴파일  
├── 📜 decrypt.py                  # 암호화된 DEX 파일 복호화  
├── 📜 recompile.py                # APK 리패키징  
├── 📜 sign.py                     # APK 재서명  
├── 📜 mobsf.py                    # MobSF 정적 분석 API 호출  
├── 📜 dynamic_analysis.py         # MobSF 동적 분석 API 호출  
├── 📜 activity_starter.py         # 자동 로그인 및 Activity 실행  
├── 📜 frida_hook.py               # Frida 후킹 적용 스크립트  
└── 📜 utils.py                    # 유틸리티 함수 모음 (ADB 등)  
🚀 프로젝트 실행 방법
1️⃣ 의존성 설치
```bash
pip install requests pycryptodome
```
2️⃣ 자동 분석 실행복사
``` bash
python main.py
```
🧩 자동화된 분석 과정
본 프로젝트는 다음과 같은 흐름으로 자동 분석을 수행합니다.
```scss
APK 업로드 
  → 정적 분석 (MobSF API) 
  → 정적 분석 결과 저장(report.json) 
  → 에뮬레이터 실행 및 앱 설치
  → Frida 후킹 적용 (루팅탐지 및 SSL 우회) 
  → Exported Activity 자동 실행 및 로그인 자동화
  → 동적 분석 수행 (MobSF API)
  → 동적 분석 결과 저장(final_dynamic_report.json)
```
📌 주요 기능 설명
✅ MobSF 구조 및 API 이해
설정파일 (config.py)을 통한 설정 관리

분석 모듈 구조 파악 및 API 활용

MobSF API Docs

✅ 암호화된 DEX 파일 복호화 자동화
APK 디컴파일 후 DEX 파일 복호화

AES-128/ECB 복호화

복호화 키: dbcdcfghijklmaop

✅ 루팅된 Android Emulator 환경 구축
루팅된 AVD 환경 구성

에뮬레이터 관리 및 APK 설치 (ADB 활용)

✅ Frida 후킹 적용 (탐지 우회)
SSL Pinning, 루팅 탐지 및 에뮬레이터 탐지 우회

API 호출 모니터링 기능 제공

✅ 정적/동적 분석 자동화
MobSF API로 APK 업로드 및 분석

Exported Activity 자동 실행 및 자동 로그인 기능 제공

최종 분석 결과 JSON 파일 형태로 제공

📑 산출물 (보고서)
report.json – 정적 분석 결과 보고서

final_dynamic_report.json – 동적 분석 결과 보고서

⚠️ 주의 사항
본 프로젝트는 보안 연구 및 학습 목적으로만 사용됩니다.

타인의 시스템에 허가 없이 사용하는 경우 법적 책임이 발생할 수 있습니다.

🌟 Star와 기여 환영!
프로젝트에 대해 궁금하거나, 개선 아이디어가 있다면 Issue 또는 PR 부탁드립니다 🙌

본 프로젝트가 유용했다면 ⭐ Star 부탁드립니다!

