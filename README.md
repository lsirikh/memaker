# MEMAKER Web

Django로 구성한 메이커 교육·제품 소개 웹 프로젝트입니다. 계정, 게시판, 강의와 제품 정보를 앱별로 분리하고 서버 렌더링 템플릿으로 화면을 구성합니다.

## 구성

- [accounts](accounts): 가입, 로그인과 사용자 프로필
- [lectures](lectures): 강의 목록·상세 및 관심 항목
- [products](products): 제품 분류·목록·상세 및 관심 항목
- [boards](boards), [intro](intro), [polls](polls): 게시판과 기타 웹 기능
- [templates](templates), `static`: 화면과 정적 리소스
- [manage.py](manage.py): Django 관리 명령 진입점

## 실행 준비

개발 당시 Django API를 사용하는 기존 프로젝트이며, 의존성을 고정한 설치 목록은 별도로 정리해야 합니다. 실행 전 Python·Django 버전, DB 연결, 메일·미디어 설정과 migration 상태를 확인하세요.

저장소에는 SQL 백업, 업로드 자료와 로그도 포함되어 있습니다. 새 개발 환경에서는 빈 테스트 데이터베이스를 준비하고 개인·운영 데이터를 복원하지 않는 방식으로 확인하는 것이 좋습니다. 이 README는 운영 서버 배포나 최신 Django 호환성을 보장하지 않습니다.
