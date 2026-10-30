# RM 프로젝트 홈페이지

공개 주소: https://raemerrr.github.io/

한국어 정적 HTML/CSS 홈페이지로 Lotto Studio를 소개합니다. 앱을 복제하거나 이전하지 않습니다. 기존 서비스와 배포는 별도 저장소에서 유지합니다.

- 앱: https://raemerrr.github.io/3d-lotto-number-generator/
- 앱 저장소: https://github.com/Raemerrr/3d-lotto-number-generator
- `index.html`: 소개, 기능, 앱 이동, 이용 안내
- `contact.html`: 사용자 확인된 운영자 및 이메일 문의, 개인정보 안내 연결
- `privacy.html`: 홈페이지 자체 수집과 호스팅 접속 정보 처리 구분
- `assets/`: CSS, SVG favicon, 1200×630 PNG OG 이미지
- `robots.txt`: 루트 및 실제 로또 사이트맵 안내, 크롤링 차단 없음
- `sitemap.xml`: 이 저장소가 관리하는 홈/개인정보 안내/문의 페이지만 포함
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

Search Console 및 AdSense 소유권 확인 메타 태그가 루트 HTML에 적용되어 있습니다. 계정 내부 인증·심사 결과는 별도로 확인합니다.

`ads.txt`에는 기존 승인 블로그의 파일과 사용자가 제공한 계정 ID를 대조한 실제 Google 게시자 행을 추가했습니다. 배포 workflow는 파일을 자동 포함합니다. 병합·배포 후 `https://raemerrr.github.io/ads.txt`의 HTTP 200과 내용을 확인해야 합니다.

광고·자동 광고·분석 스크립트는 아직 사용하지 않습니다. ads.txt는 광고를 실행하지 않으며 Google이 강력 권장하는 판매자 선언입니다. 소유권 인증이나 ads.txt 배포 자체가 광고 승인 또는 게재를 뜻하지 않습니다.

후속 순서:
1. Search Console에서 두 사이트맵 제출 결과와 대표 페이지 색인 상태 확인.
2. AdSense 사이트 목록에서 인증 및 심사 요청·결과 확인.
3. 실제 공개 가능한 문의 수단과 운영자 정보 확정.
4. 광고 도입 시 개인정보 고지, 대상 지역의 동의/CMP 및 게재 위치를 먼저 설정.
5. 별도 광고 게재 결정 후 스크립트와 광고 슬롯 연결. 기존 블로그의 GA ID는 복사하지 않음.

공식 근거: https://support.google.com/adsense/answer/12171612

## 인증 문제

Git 원격 주소는 `git remote set-url origin git@github.com:Raemerrr/raemerrr.github.io.git`로 SSH로 변경할 수 있습니다. SSH Git 인증과 GitHub API/웹 인증은 별개입니다. PR 생성에는 로그인한 웹 또는 `gh auth login`으로 인증한 GitHub CLI가 필요합니다. 인증 비밀은 파일이나 채팅에 기록하지 않습니다.
