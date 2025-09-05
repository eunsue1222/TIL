## Vue를 활용한 SPA 구성
Vue로 TMDB, YouTube API를 연동한 영화 추천 웹 애플리케이션을 개발

---

#### 팀원
김소원, 김은수

---

#### 개발언어 및 툴
- Vue 3  
- Node.js LTS  
- Visual Studio Code  
- Google Chrome 
- Python 3.11+  
- Django 5.2.x  
- Django REST framework  
<br>

#### 필수 라이브러리/오픈소스
- Vue 3 
- Vite 
- Bootstrap 
- Django  
- Django REST framework 

---

#### 컴포넌트
![component structure](./images/component_structure.png)

### Router
![router](./images/router.png)

---

#### 프로젝트 실행 결과
##### 0. 프로젝트 초기 세팅 
  - API 키 발급
      - TMDB API
      - Youtube API
  - .env 파일 생성
  - Vue + Vite + Bootstrap

![env](./images/env.png)

---

##### 1. F01 (최고 평점 영화 목록 조회): TMDB API를 활용하여 평점이 높은 영화 목록을 조회하고 화면에 카드로 표시하는 기능
![A](./images/A.png)

---

##### 2. F02 (영화 상세 정보 조회): 특정 영화 카드를 클릭 시, 해당 영화의 상세 정보 페이지로 이동하여 정보를 표시하는 기능
![B](./images/B.png)

---

##### 3. F03 (영화 공식 예고편 조회): 영화 상세 정보 페이지에서 버튼 클릭 시, Youtube API로 예고편을 검색하여 모달창으로 재생하는 기능 
![C](./images/C.png)

---

##### 4. F04 (영화 리뷰 영상 검색/조회): 별도의 검색 페이지에서 키워드로 Youtube 리뷰 영상을 검색하고, 클릭 시 모달창으로 재생하는 기능
- 검색 전
![D1](./images/D1.png)
- 검색 후
![D2](./images/D2.png)

---

#### 소스코드
```
vue-project
 └── src
       ├── components
       │    └── MovieCard.vue
       │    └── MovieDetailInfo.vue
       │    └── YoutubeCard.vue
       │    └── YoutubeReviewModal.vue
       │    └── YoutubeTrailerModal.vue
       ├── router        
       │    └── index.js
       ├── views
       │    └── Homeview.vue
       │    └── MovieDetailView.vue
       │    └── MovieListView.vue
       │    └── RecommendedView.vue
       │    └── ReviewSearchView.vue
       ├── App.vue
       └── main.js   
```

```
MovieCard.vue
```
![MovieCard](./images/MovieCard.png)

```
MovieDetailInfo.vue
```
![MovieDetailInfo](./images/MovieDetailInfo.png)

```
MovieDetailView.vue
```
![MovieDetailView_1](./images/MovieDetailView_1.png)
![MovieDetailView_2](./images/MovieDetailView_2.png)

```
MovieListView.vue
```
![MovieListView](./images/MovieListView.png)

```
ReviewSearchView.vue
```
![ReviewSearchView_1](./images/ReviewSearchView_1.png)
![ReviewSearchView_2](./images/ReviewSearchView_2.png)

```
YoutubeCard.vue
```
![YoutubeCard](./images/YoutubeCard.png)

```
YoutubeReviewModal.vue
```
![YoutubeReviewModal](./images/YoutubeReviewModal.png)

```
YoutubeTrailerModal.vue
```
![YoutubeTrailerModal_1](./images/YoutubeTrailerModal_1.png)
![YoutubeTrailerModal_2](./images/YoutubeTrailerModal_2.png)

---

#### 학습 내용 및 어려었던 점

###### 1. 프로젝트 세팅  
- **학습한 내용:**  
  - Vite 기반 Vue 프로젝트 생성 방식  
  - vue-router 설정 방법  
  - .env를 통한 API 키 보안 관리  

- **어려웠던 부분:**  
  - `.env`에 저장한 API 키가 적용되지 않던 문제 → `VITE_` 접두사 필요  
  - 서버 재시작 없이 키를 적용하려다 실패  

- **새로 배운 것:**  
  - Vite 프로젝트에서 환경 변수 사용 시 주의사항  
  - 기본 세팅이 프로젝트 전반의 흐름에 큰 영향을 준다는 점  

---

###### 2. 영화 목록 조회  
- **학습한 내용:**  
  - TMDB의 Top Rated API 사용  
  - `v-for`로 리스트 렌더링, props 전달 구조  

- **어려웠던 부분:**  
  - 이미지 경로가 `/w500` 접두어를 포함해야 제대로 나오는 점을 놓침  

- **새로 배운 것:**  
  - API 응답 구조 분석의 중요성  
  - 반복 렌더링 시 고유 key의 필요성  

---

###### 3. 영화 상세 정보  
- **학습한 내용:**  
  - 라우터 파라미터로 영화 ID 전달  
  - `useRoute()`를 통한 동적 URL 활용  

- **어려웠던 부분:**  
  - API 호출 시 언어 파라미터를 빠뜨려 영어로 표시됨  

- **새로 배운 것:**  
  - 동적 라우팅 처리 방법  
  - 외부 API 요청 시 요청 파라미터의 중요성  

---

###### 4. 예고편 모달  
- **학습한 내용:**  
  - YouTube 검색 API로 영상 ID 추출  
  - Bootstrap 모달과 iframe 연동  

- **어려웠던 부분:**  
  - 검색 결과의 `videoId`가 없거나 `undefined`일 때 예외 처리  

- **새로 배운 것:**  
  - optional chaining (`?.`)을 통한 안전한 객체 접근  
  - YouTube API의 응답 구조  

---

###### 5. 리뷰 영상 검색  
- **학습한 내용:**  
  - 사용자 입력 기반 API 호출 흐름  
  - `v-model`을 활용한 양방향 데이터 바인딩  

- **어려웠던 부분:**  
  - 검색어가 없거나 결과가 없는 경우 UI가 빈 화면으로 보이는 문제  

- **새로 배운 것:**  
  - 검색 기능 구현 시 예외처리 및 상태 관리의 중요성  
  - 사용자 경험을 고려한 UI 흐름 설계  

---

###### 마무리
SPA를 처음부터 끝까지 구현하면서 Vue의 기본기뿐만 아니라, API 연동, 사용자 경험, 비동기 처리, 데이터 흐름 등 실무에서 마주하게 될 요소들을 많이 체험해볼 수 있었습니다. 단순한 구현을 넘어서, 사용자의 시선에서 동작하고 반응하는 서비스를 만드는 재미를 느낄 수 있었습니다.

---