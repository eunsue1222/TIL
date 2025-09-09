# 들어와서 해야하는 것
## backend
1. cd django_pjt
2. python -m venv venv
3. source venv/Scripts/activate
4. python manage.py migrate
5. data/dummy_data.csv를 `letters_letter`에 업로드
5. python manage.py runserver

## frontend
1. cd my-vue-pjt 
2. npm install
3. npm run dev
4. `http://localhost:5173` 접속  

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