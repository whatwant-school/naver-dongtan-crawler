[![Crawling](https://github.com/whatwant-school/naver-dongtan-crawler/actions/workflows/Crawling.yml/badge.svg)](https://github.com/whatwant-school/naver-dongtan-crawler/actions/workflows/Crawling.yml)

# Naver Dongtan Crawler
Naver Open API를 이용하여 '동탄'에 대한 블로그 검색을 하고 그 결과를 저장


## API 인증
`파일` 또는 `환경변수` 두 가지 방법 중 하나 선택하여 등록

- 파일
  - `AUTH_CLIENTID.tmp` : Client ID 값 입력
  - `AUTH_CLIENTSECRET.tmp` : Client Secret 값 입력

- 환경 변수
  - `AUTH_CLIENTID` : Client ID 값 입력
  - `AUTH_CLIENTSECRET` : Client Secret 값 입력


## FireStore 인증
현재는 `파일`만 지원

- `AUTH_FIRESTORE.tmp`


## Python 환경

- version : Python 3.x
- package install
```sh
$ pip install -r requirements.txt
```

## 실행

- 최근 `동탄` 검색어 블로그 포스팅 200개 확인
```sh
$ ./crawler.py > output.tmp
```

- `output.tmp`에 저장된 포스팅을 firestore에 저장
```sh
$ ./push_firestore.py
```

- 저장된 포스팅에 대해서 labelling 작업
```sh
$ ./labelling.py
```
