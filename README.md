# 🧪 MobAutoAnalyzer

> **Android APK 자동 분석 파이프라인**  
> - 디컴파일 → 복호화 → 리패키징 → 서명 → MobSF 분석 → 리포트 저장  
> - 연구 목적의 APK 분석을 위한 **완전 자동화 도구**

---

## 🎯 Project Goal & 진행 현황

| 구분 | 목표 내용 | 진행 상황 |
|------|-----------|------------|
| 1. MobSF 구조 이해 | - 설정 파일(config.py) 분석<br>- 소스코드/메타데이터 분리<br>- 정적/동적 분석 모듈 구조 파악<br>- API 구조 및 사용법 익히기<br>- 에뮬레이터 연동 확인 | ✅ 정적 분석 구조 및 API 완전 이해<br>🚧 동적 분석 구조 및 에뮬레이터 연동 준비 중 |
| 2. 암호화된 DEX 복호화 | - apktool로 디컴파일/리패키징<br>- AES-128/ECB 복호화 자동화<br>- bytesIO 활용한 메모리 복호화 구현 | ✅ 완전 자동화 완료 (복호화 대상 자동 탐지 포함) |
| 3. 에뮬레이터 연동 및 탐지 우회 *(선택)* | - 설정 파일 통한 연동<br>- MobSF에서 에뮬레이터 제어<br>- frida / non-frida 탐지 우회 기법 | 🚧 MobSF + Genymotion 연동 예정<br>❌ 탐지 우회 기능 미구현 |
| 4. MobSF 분석 결과 확인 | - 정적 분석 결과 수신<br>- 동적 분석 결과 활용 | ✅ 정적 분석 결과 자동 저장 완료<br>🚧 동적 분석 결과 자동화 예정 |
| 5. API 커스터마이징 자동화 | - API로 APK 업로드 및 분석<br>- User Interaction 없는 완전 자동화<br>- 커스텀 분석 기능 개발 *(선택)* | ✅ MobSF API 기반 자동 분석 흐름 구축 완료<br>❌ 커스텀 분석 기능 미적용 |



---

## 🧰 사용 기술

| 기술 스택       | 설명 |
|----------------|------|
| Python 3.10+   | 전체 파이프라인 구현 |
| apktool        | APK 디컴파일 및 리패키징 |
| apksigner      | Android SDK 내 APK 서명 도구 |
| MobSF (API)    | 정적 분석 자동화 |
| pycryptodome   | AES 복호화 |
| requests       | MobSF API 통신 |

---

## 🛠️ 자동화 흐름

```bash
sample.apk
   ↓
[1] apktool 디컴파일
   ↓
[2] 암호화된 DEX 자동 탐지 & 복호화 (AES-128/ECB)
   ↓
[3] apktool 리패키징
   ↓
[4] apksigner 서명
   ↓
[5] MobSF 업로드 & 분석
   ↓
[6] report.json 자동 저장

🚀 실행 방법
1. 의존성 설치
```bash
pip install -r requirements.txt

```
2. 사전 준비
3. 키스토어 생성 (1회만)
```bash
keytool -genkey -v -keystore my-release-key.jks `
 -keyalg RSA -keysize 2048 -validity 10000 -alias mykey

```
4. 전체 실행
```bash
python main.py
```

5. 결과물
sample_signed.apk : 최종 분석 대상
report.json : MobSF 정적 분석 결과 저장

📁 프로젝트 구조
MobAutoAnalyzer/
├── main.py
├── decompile.py
├── decrypt.py
├── recompile.py
├── sign.py
├── mobsf.py
├── requirements.txt
├── my-release-key.jks
├── sample.apk
├── sample_signed.apk
└── report.json

⚠️ 사용 목적
이 도구는 보안 분석 및 연구 목적으로 제작되었습니다.
악의적인 목적으로 사용할 경우 법적 책임은 사용자에게 있습니다.

