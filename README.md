# BI-Portfolio
BI 웹 개발 및 분석 포트폴리오


## 🛠️ 자동 인서트 스크립트

[📁 automation_etc/cn_datainsert_automation.py](automation_etc/cn_datainsert_automation.py)

- 반복적인 데이터 입력 작업을 자동화하기 위한 Python 스크립트입니다.
- `pyodbc`를 통해 SQL Server에 연결하여 여러 건의 데이터를 효율적으로 인서트합니다.
- 업무에서 자주 반복되던 엑셀 수작업을 줄이고, 안정성과 속도를 높이기 위해 개발되었습니다.

## 🛠️ 데이터 시트 동기화

[📁 automation_etc/동기화.py](automation_etc/동기화.py)

- 게임에서 사용되는 각 종 키값을 DB에 자동으로 동기화 되게 끔 만드는 작업
- 동기화가 기존에 반자동 시스템(BI 페이지들 통해 클릭) 이었는데, 자동으로 로컬 DB에 인서트 되도록 개발 
- SSIS를 이용하여 다양한 국가에 배포하는 시스템도 만듬
