# RM 프로젝트 홈페이지

공개 주소: https://raemerrr.github.io/

한국어 정적 HTML/CSS 홈페이지로 Lotto Studio를 소개합니다. 앱을 복제하거나 이전하지 않습니다. 기존 서비스와 배포는 별도 저장소에서 유지합니다.

- 앱: https://raemerrr.github.io/3d-lotto-number-generator/
- 앱 저장소: https://github.com/Raemerrr/3d-lotto-number-generator
- `index.html`: 소개, 기능, 앱 이동, 이용 안내
- `privacy.html`: 홈페이지 자체 수집과 호스팅 접속 정보 처리 구분
- `assets/`: CSS, SVG favicon, 1200×630 PNG OG 이미지
- `robots.txt`: 루트 및 실제 로또 사이트맵 안내, 크롤링 차단 없음
- `sitemap.xml`: 이 저장소가 관리하는 홈/개인정보 안내만 포함
- `404.html`: 오류 안내, 검색 색인 제외
- [출시 체크리스트](LAUNCH_CHECKLIST.md), [검증 기록](VERIFICATION.md)

## 로컬 확인

Python 3만 있으면 됩니다. 프레임워크, 패키지 설치, 빌드가 필요 없습니다.

```sh
python3 scripts/check.py
python3 -m http.server 4187 --bind 127.0.0.1
```

http://127.0.0.1:4187/ 에서 확인합니다. 모바일 320/390px, 데스크톱 1440px, 확대 200%, Tab/Shift+Tab/Enter를 확인하세요. 검사 스크립트는 메타데이터·내부 경로·앵커·구조화 데이터·사이트맵·대비와 광고 스크립트 부재를 검증합니다. 시각적·보조기술 검증 전체를 대체하지 않습니다.

앱 링크는 의도적으로 `/3d-lotto-number-generator/`입니다. 이 저장소에 앱 파일이 없으므로 로컬에서는 404가 정상이며, 운영 호스트에서는 기존 앱으로 연결됩니다. 로컬 검증용으로 앱을 복제하지 않습니다.

## GitHub Pages 배포

1. 저장소 Settings → Rules → Rulesets 및 Branches에서 보호/필수 검사를 확인합니다. 기존 보호를 해제하지 않습니다.
2. 작업 브랜치를 푸시하고 main 대상 PR을 생성합니다. `Check static site` 통과 후 리뷰/필수 승인을 받아 병합합니다.
3. Settings → Pages → Build and deployment → Source를 **GitHub Actions**로 설정합니다. 최초 설정은 저장소 관리자 권한이 필요할 수 있습니다.
4. main 푸시에 `Deploy GitHub Pages`가 검사 후 공개 파일만 `_site`에 모아 배포합니다. README, 체크리스트, 검사 스크립트는 배포하지 않습니다. 이미 병합 후 설정했다면 Actions에서 배포 workflow를 수동 실행합니다.
5. Actions의 `deploy` 성공 후 아래 주소를 실제로 확인합니다.

```sh
curl -I https://raemerrr.github.io/
curl -I https://raemerrr.github.io/privacy.html
curl -I https://raemerrr.github.io/assets/favicon.svg
curl -I https://raemerrr.github.io/assets/og.png
curl https://raemerrr.github.io/robots.txt
curl https://raemerrr.github.io/sitemap.xml
curl -I https://raemerrr.github.io/3d-lotto-number-generator/
```

루트와 자산은 HTTP 200, 없는 경로는 404를 확인합니다. 앱 버튼을 눌러 기존 앱의 언어 선택과 접근을 확인합니다. 이 workflow는 루트 저장소만 배포하며 앱 저장소의 workflow나 설정을 변경하지 않습니다.

## 검색 등록과 소유권 인증

공개 배포와 검증 후 운영자가 Search Console에서 실제 URL 속성과 가능한 인증 방식을 확인합니다. 계정 화면의 실제 인증 파일/메타 값을 제공받은 뒤 적용합니다. `github.io`의 DNS를 임의로 변경하거나 토큰을 추측하지 않습니다. 루트와 앱의 사이트맵은 각각 제출할 수 있으며, 앱 사이트맵 관리는 앱 저장소에 남깁니다. 색인, 검색 순위, AI 검색 노출을 보장하지 않습니다.

## AdSense 및 ads.txt 후속 절차

현재 광고·자동 광고·분석 도구를 사용하지 않으며 인증 코드, 게시자 ID, ads.txt도 없습니다. 루트 404 해결은 광고 승인 준비 완료나 승인을 뜻하지 않습니다.

1. 운영자가 AdSense 계정 화면에서 이 사이트 등록 가능 여부, 정책, 인증 방식과 실제 게시자 ID를 확인합니다. 계정 약관 동의와 신청은 운영자가 수행합니다.
2. 실제로 요구되는 인증 값만 전달받아 별도 PR로 적용합니다. 광고 활성화는 이번 범위가 아니며 별도 지시 후 진행합니다.
3. AdSense 화면에 제공된 **실제 ads.txt 한 줄 전체**를 확인한 뒤 저장소 루트에 `ads.txt`를 UTF-8 일반 텍스트로 추가합니다. 빈 파일이나 예시 ID를 배포하지 않습니다.
4. 현재 검사 스크립트의 ads.txt 부재 검사를 실제 행 검증으로 변경하고 PR을 리뷰·병합합니다. 배포 workflow는 루트 ads.txt가 있으면 자동으로 포함합니다.
5. https://raemerrr.github.io/ads.txt 가 200이고 내용이 계정 화면과 정확히 일치하는지 확인한 뒤 AdSense에서 재확인합니다. 반영 시간과 심사 결과는 서비스 측에서 결정합니다.
6. 광고/분석 도입 전 개인정보 안내와 지역별 필요한 동의 설정, 저장소·앱의 실제 처리, 외부 전송과 쿠키를 다시 검토합니다. 운영자 표시나 문의 수단이 필요하면 실제 공개 가능한 정보를 사용자에게 요청합니다. 임의 연락처를 만들지 않습니다.

## 인증 문제

Git 원격 주소는 `git remote set-url origin git@github.com:Raemerrr/raemerrr.github.io.git`로 SSH로 변경할 수 있습니다. SSH Git 인증과 GitHub API/웹 인증은 별개입니다. PR 생성에는 로그인한 웹 또는 `gh auth login`으로 인증한 GitHub CLI가 필요합니다. 인증 비밀은 파일이나 채팅에 기록하지 않습니다.
