# 수정해야할 파일!!! (중요!!!)
## assets
1. 사진 파일은 반드시 {png,jpg,jpeg,webp} 형태로 저장해야합니다.
2. 사진 파일명은 '김소원.png'와 같은 {이름.png} 형태를 반드시 지켜주세요.
## data.csv 
1. tmp.csv를 참고해주세요

|name|content|music|music_content|image_link|music_link|
|:----:|:-------:|:-----:|:-------------:|:----:|:----:|
|이름|편지내용|신청곡|신청곡 이유|사진 링크|음악 링크|
|김소원|마지막이라니ㅜㅜ|체리필터-낭만고양이|고양이가 되고 싶어요!|googledrive|https://youtu.be/Nh5Ld4EpXJs?si=wPNhocQKmtVACODU|

# 들어와서 해야하는 것 (추가했음!!!)
## backend
1. cd django_pjt
2. python -m venv venv
3. source venv/Scripts/activate
4. pip install -r requirements.txt
5. python manage.py migrate
6. data/rolling_paper_v4.csv를 `letters_letter`에 업로드
7. python manage.py runserver

## frontend
1. cd my-vue-pjt 
2. npm install
3. npm install axios
4. npm run dev
5. `http://localhost:5173/letters` 접속  

```vue
<!-- views/Letters.vue와 backend 연결되는 부분: axios.get 이하 api 주소가 중요함-->
onMounted(async () => {
  try {
    // 실제 API 엔드포인트로 교체하세요.
    const response = await axios.get('http://127.0.0.1:8000/letters/');
    letters.value = response.data;
  } catch (err) { 
    error.value = '데이터 로딩에 실패했습니다.'; 
    console.error(err); 
  } finally { 
    loading.value = false; 
  }
});
```

# 롤링페이퍼 & 뮤직 플레이어 웹앱

Vue 3와 Django를 기반으로 제작된 인터랙티브 롤링페이퍼 및 음악 신청 웹 애플리케이션입니다. '14기 대전 4반' 구성원들의 메시지와 신청곡을 레트로한 턴테이블 컨셉의 UI를 통해 감상할 수 있습니다.

참고: 위 이미지는 예시이며, 실제 프로젝트 스크린샷으로 교체하는 것을 권장합니다.

---

## ✨ 주요 기능
- **데이터 연동**: Django 백엔드 API를 통해 각 개인의 롤링페이퍼, 신청곡, 프로필 이미지 링크를 동적으로 불러옵니다.
- **인터랙티브 UI**: 실제 턴테이블처럼 음악 재생 시 LP판이 회전하고 톤암(바늘)이 움직이는 애니메이션이 적용되어 있습니다.
- **음악 재생**: YouTube iframe을 통해 신청곡을 직접 재생하고 컨트롤할 수 있습니다.
- **유동적인 레이아웃**: 편지 내용 길이에 따라 롤링페이퍼 카드의 높이가 자동으로 조절됩니다.
- **반응형 디자인**:
  - 넓은 화면 (PC): 롤링페이퍼/신청곡과 턴테이블이 좌우로 나란히 배치되어 한눈에 모든 정보를 볼 수 있습니다.
  - 좁은 화면 (모바일/창 분할): 모든 요소가 세로로 배치되어 스크롤에 최적화된 경험을 제공합니다.
- **데이터 처리 유틸리티**: Python 스크립트를 통해 CSV 파일의 데이터를 정제하고, Google Drive 링크를 웹에 적합한 URL로 일괄 변환하는 기능을 포함합니다.

---

## 💻 기술 스택
- **Frontend**: Vue 3 (Composition API), axios
- **Backend**: Django (REST API 제공)
- **Styling**: CSS (Flexbox, Media Queries for Responsive Design)
- **Utilities**: Python, pandas

---

## 🚀 개발 과정 및 주요 결정사항 (Development Log)

### v0.1: 초기 컨셉 - 세로 스크롤 CD 플레이어
- **요구사항**: /letters/ API에서 받은 데이터를 CD 디스크가 위아래로 움직이는 형태로 시각화.  
- **구현**: v-for를 이용해 아이템을 렌더링하고, 선택된 아이템(selectedIndex)에 따라 transform: translateY()와 scale()을 동적으로 적용하여 애니메이션 효과 구현.

---

### v0.2: 디자인 개선 - 아날로그 & 레트로 컨셉으로 전환
- **요구사항**: 보내주신 레퍼런스 이미지처럼, 리듬 게임 UI와 유사한 아날로그 감성의 디자인으로 변경.  
- **구현**:
  - 어두운 가죽 질감의 배경과 입체적인 버튼 디자인 적용.
  - 아이템 배치 방식을 LP판 위 트랙 리스트처럼 보이도록 transform-origin과 rotate를 사용한 방사형 레이아웃으로 변경.

---

### v0.3: 레이아웃 재구성 - 밝은 테마와 공전하는 편지들
- **요구사항**: 화면 하단에 반만 보이는 레코드판과 그 주위를 공전하는 편지 객체 디자인. 밝은 테마(연노랑, 연파랑) 적용.  
- **구현**:
  - UI를 Letters.vue(부모)와 LetterOrbit.vue(자식) 컴포넌트로 분리하여 역할 분담.
  - LetterOrbit.vue에서 삼각함수(Math.cos, Math.sin)를 이용해 각 편지 객체의 원형 궤도 좌표를 동적으로 계산.
  - 선택된 편지는 중앙에 큰 카드로, 나머지는 작은 원으로 표시하도록 v-if와 동적 클래스 적용.

---

### v0.4: 백엔드 연동 및 데이터 처리
- **요구사항**: Django API와 실제 데이터 연동 및 CSV 데이터 사전 처리.  
- **구현**:
  - onMounted 훅에서 axios를 사용해 API 호출 및 데이터 바인딩.  
  - Python 스크립트 제작:  
    - music 컬럼의 불필요한 문자(<, >)와 공백을 제거.  
    - YouTube API를 연동하여 music 제목으로 검색 후 music_link 컬럼 생성.  
    - Google Drive 링크(open?id=..., /d/...)에서 파일 ID를 추출하여 웹에 직접 삽입 가능한 lh3.googleusercontent.com 형식의 URL로 일괄 변환하는 기능 추가.  

---

### v0.5: 디테일 수정 및 버그 해결
- **요구사항**: 턴테이블 톤암(바늘), 타이틀 옆 아이콘 추가, 유동적인 카드 높이, 이미지 로딩 문제 해결.  
- **구현**:
  - note-card의 고정 height를 min-height로 변경하여 내용 길이에 따라 높이가 유동적으로 변하도록 수정.  
  - **이미지 로딩 문제 해결**:  
    - **초기 증상**: API 응답은 정상이지만, 레코드판 중앙에 이미지가 표시되지 않고 대체 텍스트('라벨 이미지')만 나타나는 현상.  
    - **원인 분석**:  
      - 브라우저 개발자 도구의 Network 탭에서 이미지 요청이 403 Forbidden 또는 net::ERR_BLOCKED_BY_ORB 에러와 함께 실패하는 것을 확인.  
      - 403 Forbidden: Google Drive 파일의 공유 설정이 '비공개'로 되어 있어 웹사이트에서 접근할 권한이 없는 문제.  
      - net::ERR_BLOCKED_BY_ORB: 브라우저가 이미지 파일을 예상했으나, Google Drive가 바이러스 검사 경고 등 다른 HTML 페이지를 응답으로 보내 보안상의 이유로 브라우저가 차단하는 문제.  
    - **해결 과정**:  
      - Google Drive 파일의 공유 설정을 **'링크가 있는 모든 사용자'**로 변경.  
      - 단순 공유 링크가 아닌, 웹 삽입에 적합한 URL 형식을 탐색.  
      - 가장 안정적으로 원시 이미지 데이터를 반환하는 https://lh3.googleusercontent.com/d/[FILE_ID] 형식을 최종 해결책으로 채택하고, Python 스크립트에 해당 변환 로직을 추가.  
  - 타원형 이미지 문제를 해결하기 위해 .label 컨테이너의 크기를 width, height를 고정 픽셀 값으로 설정하여 완벽한 정사각형으로 만듦.  
  - z-index 대신 궤도 각도를 동적으로 조절하여 중앙 카드와 외곽 객체가 겹치지 않도록 수정.  

---

### v0.6: 반응형 디자인 적용 (최종)
- **요구사항**: 넓은 화면에서는 좌우 2단 레이아웃, 좁은 화면에서는 기존의 세로 1단 레이아웃으로 표시.  
- **구현**:
  - `<template>` 구조를 main-content, content-panel, player-panel로 재구성.  
  - CSS에 @media (min-width: 1200px) 미디어 쿼리를 추가.  
  - 넓은 화면일 때 main-content에 display: flex를 적용하여 content-panel과 player-panel을 가로로 배치.  
  - tonearm의 위치 기준을 컨테이너 가장자리가 아닌 중앙(calc(50% - ... ))으로 변경하여 레이아웃 변동에도 상대적 위치를 유지하도록 개선.  

---

# 개인적인 소감...  
## 김은주  
* DBMS의 소중함을 느낄 수 있었음. db.sqlite3는 gitignore로 관리하고 있기 때문에 공유할 수 없었고, csv 파일을 항상 연동해서 사용해야 하니 번거로웠음  
* 앞으로 form 제출하라고 하면 빨리 빨리 해야겠다  

## 김소원
* django, vue 수업을 대충 들었던 것을 웹앱 만들면서 엄청 후회하였다ㅜㅡㅜ csv 파일을 데이터베이스에 올리는 것조차 몰라서 한참 헤매였던 기억이,,, 정말 만드는 내내 머리를 쥐어뜯으면서 괴로웠지만 이렇게 만들면서 강사님이 강조하셨던 부분이 왜 그렇게 강조하셨는지 몸소 느낄 수 있는 좋은 기회였다. 
* 백엔드와 프론트엔드의 연결을 실제로 구현해본 좋은 경험이였고 개인적으로 프론트엔드의 소중함을 느낄 수 있었다,,,

## 김은수
* 데이터를 CSV로 처리하는 것이 아니라 백엔드 데이터베이스와 연동하여 작업하는 과정은 처음이라 어려웠다. 하지만 강의 시간에 배운 백엔드-프론트엔드 연동 과정을 실제로 다시 경험해보면서, 전체적인 흐름을 깊이 있게 이해할 수 있었다. 이번 프로젝트를 통해 기획의 중요성을 다시 한 번 실감했고, 협업을 통해 소통 능력과 문제 해결 능력도 키울 수 있었다. 프로젝트를 원활하게 진행하기 위해서는 내가 맡은 부분뿐 아니라 다른 파트에 대한 이해도 필요하다는 것을 깨달았고, 그만큼 더 열심히 공부해야겠다는 다짐을 하게 되었다. 