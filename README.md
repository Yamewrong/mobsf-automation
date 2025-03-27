# 🔍 MobAutoAnalyzer

> **Automated Static & Dynamic Malware Analysis System based on MobSF**  
> `MobSF + AVD + Frida + AES Decryption` 기반 **악성코드 분석 자동화 파이프라인**

---

![Shields.io](https://img.shields.io/badge/status-active-green?style=flat-square)
![Python](https://img.shields.io/badge/python-3.10-blue?style=flat-square)
![MobSF](https://img.shields.io/badge/MobSF-3.x-orange?style=flat-square)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Android-lightgrey?style=flat-square)

---

## 📌 프로젝트 개요

이 프로젝트는 MobSF(Mobile Security Framework)를 기반으로 한 **APK 분석 자동화 시스템**입니다.  
다음 기능들을 통합하여 수행합니다:

- 암호화된 DEX 복호화 (AES-128/ECB 기반)
- 정적/동적 분석 자동화 (MobSF API 기반)
- 루팅 탐지 우회, Frida 후킹 자동 적용
- Exported Activity 추적 및 자동 실행
- InsecureBankv2 기반 취약점 탐지 자동화

---

## 🧠 주요 기능 요약

| 기능 | 설명 |
|------|------|
| 🔐 **DEX 복호화** | `.apk`, `.dat`, `.bin` 내 AES-128/ECB 암호화된 파일 자동 탐지 및 복호화 |
| 📦 **APK 리패키징** | apktool 기반으로 복호화된 DEX 포함 재패키징 + 서명 자동화 |
| 🔬 **정적 분석 자동화** | MobSF API 활용해 업로드/해시 관리/리포트 추출 자동화 |
| ⚙️ **동적 분석 자동화** | MobSF Dynamic API + AVD 기반 자동 실행 및 로그 수집 |
| 💉 **Frida 후킹 통합** | `get_combined_frida_script()` 활용한 Frida 스크립트 병합 후 자동 후킹 |
| 📲 **Activity 자동 실행** | PostLogin, Transfer 등 Exported Activity 자동 실행 및 분석 |
| ⚠️ **루팅 탐지 우회** | Frida 기반 루팅 탐지 우회 스크립트 자동 적용 |
| 📊 **리포트 저장** | `final_static_report.json`, `final_dynamic_report.json` 저장 및 활용 |

---

## 🔧 기술 스택

- **Python 3.10**
- **MobSF (Mobile Security Framework)**
- **Frida**
- **AVD (Android Virtual Device)**
- **apktool**
- **AES-128/ECB 복호화 (PyCryptodome)**
---

## 🔁 전체 분석 흐름

```plaintext
[APK 파일] 
   └─▶ [decrypt.py] 암호화된 DEX 복호화
       └─▶ [apktool + sign.py] 리패키징 및 서명
           └─▶ [mobsf.py] 정적 분석
               └─▶ [dynamic_analysis.py] 동적 분석 실행
                   └─▶ [Frida + Activity 실행 + 루팅 우회]
                       └─▶ [JSON 리포트 저장 및 요약 대시보드]
```
📁 프로젝트 구조
```plaintext
MobAutoAnalyzer/
├── main.py                    # 전체 자동화 시작 지점
├── config.py                  # MobSF URL, API KEY 등 설정
├── decrypt.py                 # DEX 복호화 모듈
├── mobsf.py                   # MobSF 정적 분석 API 모듈
├── dynamic_analysis.py        # 동적 분석 + Frida 후킹
├── activity_starter.py        # Exported Activity 실행 및 버튼 자동화
├── frida_scripts/
│   └── android/
│       └── auxiliary/         # 사용자 정의 후킹 스크립트
├── tools/
│   └── apktool_wrapper.py     # apk 리패키징/서명 자동화
├── outputs/
│   ├── final_static_report.json
│   ├── final_dynamic_report.json
│   └── mobsf_rpc_log.txt
```
🧪 샘플 시연 결과 (InsecureBankv2)
✅ 루팅 탐지 우회 성공

✅ devadmin 계정 자동 로그인

✅ PostLogin 화면에서 Exported Activity 직접 실행 성공

🙋‍♂️ 개발자
Cybersecurity Specialist | Security Researcher
💻 GitHub: https://github.com/Yamewrong
🛡️ 보안 프로젝트 문의 또는 협업은 언제든지 환영입니다!
