# 검증 기록

확인일: 2026-10-30 (한국 시간)

## 초기 상태

- 로컬·원격 모두 커밋 없는 빈 저장소. README, AGENTS.md, workflow 없음.
- 공개 저장소 API: `has_pages: false`, 기본 브랜치 main.
- 루트 URL HTTP 404. 기존 앱 루트와 sitemap HTTP 200.
- 공개 Rulesets API는 빈 배열. 브랜치 보호 상세는 인증 필요로 확인하지 못함.
- HTTPS Git/API 저장 인증은 거부됨(401). SSH 인증은 성공.
- PR 비교를 위해 내용 없는 초기 커밋만 main에 SSH 푸시. 구현은 `codex/root-homepage`에서 진행.

## 로컬 통과

- `python3 scripts/check.py` 통과: 언어, 제목, 설명, canonical, 내부 파일·앵커, JSON-LD, 루트 사이트맵 범위, robots, OG PNG 1200×630, ads.txt/실행 스크립트 부재.
- 로컬 홈페이지, 개인정보 페이지, CSS, favicon, OG PNG, robots, sitemap HTTP 200.
- 글자 대비: 본문 13.62:1, 보조 본문 6.14:1, 안내문 5.61:1, CTA 7.94:1, 녹색 제목 7.27:1. 계산 기반 검사이며 접근성 인증을 뜻하지 않음.
- 앱 내 브라우저의 실제 폭 319px에서 소개·버튼·일러스트·기능 영역 육안 확인. 문서 scrollWidth 312px로 가로 넘침 없음.
- Tab 첫 포커스는 본문 바로가기, solid 포커스 표시 확인. Enter로 #main 이동 확인. 모든 링크가 네이티브 a 요소이며 양의 tabindex 없음.
- 브라우저 UI의 데스크톱 viewport 설정 요청이 실제 화면 폭에 반영되지 않아 데스크톱 육안 검증은 미완료.
- 외부 앱 루트 및 실제 앱 sitemap HTTP 200 재확인. 앱 소스/배포에는 변경 없음.

## 미완료와 제한

- PR 생성, 보호 규칙 상세 조회, Pages 설정은 유효한 GitHub 웹/API 인증이 필요함. SSH는 Git 푸시만 해결함.
- main 병합 및 배포 전이므로 운영 루트 200, 운영 자산/메타/robots/sitemap, 실제 버튼 이동 결과는 아직 검증하지 않음.
- Search Console 소유권 인증·검색 등록과 AdSense 신청/승인은 진행하지 않음.
- 모든 보조기술·브라우저·화면 크기 조합을 검증한 것은 아님.
