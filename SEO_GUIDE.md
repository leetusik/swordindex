# Swordindex SEO Guide

이 가이드는 Swordindex 웹사이트의 검색 엔진 최적화(SEO)를 위한 지침을 제공합니다.

## 목차

1. [기본 SEO 설정](#기본-seo-설정)
2. [Google Search Console 설정](#google-search-console-설정)
3. [Naver Search Advisor 설정](#naver-search-advisor-설정)
4. [사이트맵 관리](#사이트맵-관리)
5. [콘텐츠 최적화](#콘텐츠-최적화)
6. [기술적 SEO](#기술적-seo)
7. [모바일 최적화](#모바일-최적화)
8. [로컬 SEO](#로컬-seo)

## 기본 SEO 설정

### 메타 태그

모든 페이지에는 다음 메타 태그가 포함되어 있어야 합니다:

- `title`: 페이지 제목 (60자 이내)
- `description`: 페이지 설명 (160자 이내)
- `keywords`: 관련 키워드 (콤마로 구분)
- `canonical`: 표준 URL

### Open Graph 태그

소셜 미디어 공유를 위한 Open Graph 태그:

- `og:title`: 페이지 제목
- `og:description`: 페이지 설명
- `og:image`: 공유 이미지 (1200x630px 권장)
- `og:url`: 페이지 URL

## Google Search Console 설정

1. [Google Search Console](https://search.google.com/search-console)에 접속
2. 도메인 소유권 확인
   - HTML 파일 업로드
   - DNS 레코드 추가
   - Google Analytics 연결
3. 사이트맵 제출
   - `sitemap.xml` 제출
4. 색인 생성 요청
   - URL 검사 도구 사용

### 사이트맵 제출 스크립트

사이트맵 제출을 위해 `submit_sitemap.py` 스크립트를 사용할 수 있습니다:

```bash
python submit_sitemap.py
```

## Naver Search Advisor 설정

한국 시장을 위한 Naver 검색 최적화:

1. [Naver Search Advisor](https://searchadvisor.naver.com/)에 접속
2. 사이트 등록 및 소유권 확인
3. 사이트맵 제출
4. 검색 노출 설정 최적화

## 사이트맵 관리

사이트맵은 검색 엔진이 웹사이트의 구조를 이해하는 데 도움을 줍니다:

1. XML 사이트맵 업데이트
   ```bash
   python generate_sitemap.py
   ```

2. HTML 사이트맵 업데이트
   - `/sitemap/` 페이지에서 모든 중요 페이지 링크 유지

## 콘텐츠 최적화

### 키워드 연구

주요 키워드:
- AI 검색 솔루션
- 이커머스 검색
- 쇼핑몰 검색 최적화
- 검색 정확도 향상
- 이탈율 감소
- 한국 이커머스
- 중소기업 솔루션

### 콘텐츠 작성 지침

1. 제목(H1)에 주요 키워드 포함
2. 부제목(H2, H3)에 관련 키워드 포함
3. 첫 문단에 주요 키워드 포함
4. 자연스러운 키워드 밀도 유지 (2-3%)
5. 고품질 이미지에 적절한 alt 텍스트 추가
6. 내부 링크 활용

## 기술적 SEO

### 페이지 속도 최적화

1. 이미지 최적화
   - WebP 형식 사용
   - 적절한 크기로 리사이징
   - 지연 로딩 적용

2. 코드 최적화
   - CSS/JS 최소화
   - 중요하지 않은 JS 지연 로딩
   - 브라우저 캐싱 활용

### 모바일 최적화

1. 반응형 디자인 확인
2. 모바일 페이지 속도 테스트
3. 터치 요소 크기 및 간격 최적화

### 구조화된 데이터

스키마 마크업을 사용하여 검색 결과에서 더 많은 정보 표시:
- Organization
- Service
- FAQPage (FAQ 섹션 추가 시)

## 로컬 SEO

한국 시장을 위한 로컬 SEO:

1. 네이버 지도 등록
2. 카카오 지도 등록
3. 구글 비즈니스 프로필 최적화
4. 로컬 디렉토리 등록

## 정기적인 SEO 점검

1. 월간 검색 콘솔 보고서 검토
2. 키워드 순위 모니터링
3. 경쟁사 분석
4. 콘텐츠 업데이트 계획

---

이 가이드는 지속적으로 업데이트됩니다. 질문이나 제안사항이 있으면 팀에 문의하세요. 

