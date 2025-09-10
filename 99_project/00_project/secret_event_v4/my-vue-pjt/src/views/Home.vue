<template>
  <div class="home-container">
    <!-- 장식용 별들 -->
    <div class="stars-container">
      <div class="star star-1">
        <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
      </div>
      <div class="star star-2">
        <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
      </div>
      <div class="star star-3">
        <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
      </div>
      <div class="star star-4">
        <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
      </div>
    </div>

    <div class="content-box">
      <!-- [추가] 리본 위 원형 이미지 -->
      <img :src="teacherAvatar" alt="강사님" class="ribbon-avatar" />
      
      <!-- h1에 ribbon 클래스 추가 -->
      <h1 class="main-title ribbon">🤍김구현 강사님 감사합니다🤍</h1>
      <router-link to="/letters" class="nav-button">
        4반 신청곡 들으러 가기
      </router-link>
    </div>
  </div>
</template>

<script setup>
// [추가] src/assets 폴더에서 이미지를 불러옵니다.
// '/src/assets/teacher-avatar.jpg' 경로에 이미지를 넣어주세요.
import teacherAvatar from '@/assets/image.png';
</script>

<style scoped>
.home-container {
  width: 100vw;
  height: 100vh;
  background-color: #fffbeb; 
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  position: relative; /* 별들의 위치 기준점 */
  overflow: hidden; /* 별들이 밖으로 나가지 않도록 */
}

.content-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 1; /* 별들 위에 위치하도록 */
}

/* [추가] 리본 위 아바타 이미지 스타일 */
.ribbon-avatar {
  width: 400px;
  height: 400px;
  border-radius: 50%;
  border: 6px solid white;
  box-shadow: 0 5px 20px rgba(0,0,0,0.15);
  
  /* 리본과 겹치도록 위치 조정 */
  position: relative;
  z-index: 2; /* 리본 위에 위치 */
  margin-bottom: -60px; /* 아래 리본과 절반 겹치게 */
  object-fit: cover;
}

.main-title {
  font-size: clamp(2.5rem, 5vw, 4rem);
  color: #334155;
  font-weight: 700;
  /* margin-bottom은 리본에 의해 제어되므로 제거 */
}

/* --- [수정] 리본 배너 스타일 --- */
.ribbon {
  background-color: #4b8fde;
  color: white;
  padding: 30px 60px; /* 아바타와 겹치므로 상하 패딩 증가 */
  margin-bottom: 40px; /* 버튼과의 간격 */
  position: relative;
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
  border-radius: 5px;
}

/* 리본 꼬리 공통 스타일 */
.ribbon::before,
.ribbon::after {

}

/* 리본 왼쪽 꼬리 */
.ribbon::before {
  left: -20px; /* 메인 배너와 겹치게 위치 */
  /* V-자 모양으로 자르기 */
  clip-path: polygon(100% 0, 100% 100%, 0 100%, 40% 50%, 0 0);
}

/* 리본 오른쪽 꼬리 */
.ribbon::after {
  right: -20px; /* 메인 배너와 겹치게 위치 */
  /* 오른쪽은 모양을 뒤집어야 함 */
  clip-path: polygon(100% 0, 100% 100%, 0 100%, 0 0, 60% 50%);
}


.nav-button {
  display: inline-block;
  padding: 18px 36px;
  background-color: #60a5fa;
  color: white;
  border-radius: 12px;
  text-decoration: none;
  font-size: 1.1rem;
  font-weight: 600;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  transition: all 0.2s ease-in-out;
  border: 3px solid white; /* 흰색 테두리 추가 */
}
.nav-button:hover {
  transform: translateY(-3px);
  background-color: #3b82f6;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
}

/* --- [추가] 별 스타일 --- */
.stars-container {
  position: absolute;
  width: 100%;
  height: 100%;
}
.star {
  position: absolute;
  width: 50px;
  height: 50px;
  color: #ffca28; /* 노란색 별 */
  animation: twinkle 3s infinite ease-in-out;
}
.star svg path {
  fill: currentColor;
}
.star-1 { top: 15%; left: 15%; animation-delay: 0.5s; }
.star-2 { top: 20%; right: 10%; animation-delay: 1s; }
.star-3 { bottom: 25%; left: 20%; animation-delay: 1.5s; }
.star-4 { bottom: 15%; right: 18%; animation-delay: 0s; }

@keyframes twinkle {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(0.8); opacity: 0.7; }
}
</style>

