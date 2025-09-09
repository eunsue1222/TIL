# 수정해야할 파일!!! (중요!!!)
## assets
1. 사진 파일은 반드시 {png,jpg,jpeg,webp} 형태로 저장해야합니다.
2. 사진 파일명은 '김소원.png'와 같은 {이름.png} 형태를 반드시 지켜주세요.
## data.csv 
1. tmp.csv를 참고해주세요

|name|content|music|music_content|link|
|:----:|:-------:|:-----:|:-------------:|:----:|
|이름|편지내용|신청곡|신청곡 이유|음악 링크|
|김소원|마지막이라니ㅜㅜ|체리필터-낭만고양이|고양이가 되고 싶어요!|https://youtu.be/Nh5Ld4EpXJs?si=wPNhocQKmtVACODU|

# 들어와서 해야하는 것 (추가했음!!!)
## backend
1. cd django_pjt
2. python -m venv venv
3. source venv/Scripts/activate
4. pip install -r requirements.txt
5. python manage.py migrate
6. data/dummy_data.csv를 `letters_letter`에 업로드
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