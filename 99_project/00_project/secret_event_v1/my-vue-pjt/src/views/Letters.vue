<template>
  <div class="letter-page">
    <div class="page-title">14th 대전 4반!!</div>

    <!-- 우측 상단: 배경음악 플레이어 -->
    <div class="music-player">
      <div class="music-header">
        <span>🎵 Background Music</span>
      </div>
      <div class="music-body">
        <input
          v-model="musicUrl"
          class="music-input"
          type="text"
          placeholder="YouTube 링크를 붙여넣으세요 (예: https://youtu.be/5qap5aO4i9A)"
        />
        <div v-if="videoId" class="music-iframe-wrap">
          <iframe
            :src="youTubeEmbedUrl"
            title="YouTube player"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
          ></iframe>
        </div>
        <div v-else class="music-hint">유효한 유튜브 링크를 입력하면 플레이어가 나타납니다.</div>
      </div>
    </div>

    <div v-if="loading" class="status-message">💌 로딩 중...</div>
    <div v-if="error" class="status-message error">{{ error }}</div>

    <template v-if="letters.length > 0">
      <LetterOrbit :letters="letters" :selectedIndex="selectedIndex" />

      <!-- 중앙의 선택된 편지 카드 -->
      <div v-if="selectedLetter" class="selected-letter-card">
        <p class="letter-content">{{ selectedLetter.content }}</p>
        <h3 class="letter-name">{{ selectedLetter.name }}</h3>
      </div>

      <!-- LP (검은색) -->
      <div class="record-half">
        <div class="record-core">
          <!-- 검은 디스크 -->
          <div class="record-disc">
            <!-- 회전 홈 -->
            <div class="record-groove groove-1"></div>
            <div class="record-groove groove-2"></div>
            <div class="record-groove groove-3"></div>

            <!-- 라벨(센터) -->
            <div class="record-label">
              <div class="label-text">Daejeon 4</div>
            </div>
          </div>
        </div>
      </div>

      <!-- 가운데 장식 이미지는 라벨과 겹치니 제거/비활성 (원하면 남겨도 됨)
      <img ... class="center-image">
      -->

      <!-- 톤암 -->
      <div class="tonearm" :style="tonearmStyle">
        <div class="tonearm-pivot"></div>
        <div class="tonearm-arm">
          <div class="tonearm-head"></div>
        </div>
      </div>

      <!-- 선택 이동 버튼 -->
      <div class="controls">
        <button @click="moveUp" aria-label="이전 편지">▲</button>
        <button @click="moveDown" aria-label="다음 편지">▼</button>
      </div>
    </template>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import LetterOrbit from '@/components/LetterOrbit.vue';
import axios from 'axios';

const letters = ref([]);
const selectedIndex = ref(0);
const loading = ref(true);
const error = ref(null);

/** 배경음악: 유튜브 링크 */
const musicUrl = ref('https://youtu.be/5qap5aO4i9A'); // 기본값: lofi hip hop radio
const videoId = computed(() => {
  // 다양한 형태의 유튜브 URL에서 video id 추출
  const url = musicUrl.value?.trim();
  if (!url) return '';
  // youtu.be/<id>
  let m = url.match(/youtu\.be\/([A-Za-z0-9_-]{11})/);
  if (m) return m[1];
  // youtube.com/watch?v=<id>
  m = url.match(/[?&]v=([A-Za-z0-9_-]{11})/);
  if (m) return m[1];
  // youtube.com/embed/<id>
  m = url.match(/embed\/([A-Za-z0-9_-]{11})/);
  if (m) return m[1];
  return '';
});
const youTubeEmbedUrl = computed(() => {
  // 자동 재생은 브라우저 정책상 음소거(Muted) 상태에서만 가능
  return videoId.value
    ? `https://www.youtube-nocookie.com/embed/${videoId.value}?autoplay=0&controls=1&modestbranding=1&rel=0&loop=1&playlist=${videoId.value}`
    : '';
});

onMounted(async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/letters/');
    // DRF 페이지네이션 대비
    letters.value = Array.isArray(response.data)
      ? response.data
      : (response.data?.results ?? []);
  } catch (err) {
    error.value = '데이터 로딩에 실패했습니다.';
    console.error(err);
  } finally {
    loading.value = false;
  }
});

const selectedLetter = computed(() => {
  return letters.value.length > 0 ? letters.value[selectedIndex.value] : null;
});

const moveUp = () => {
  if (!letters.value.length) return;
  selectedIndex.value = (selectedIndex.value - 1 + letters.value.length) % letters.value.length;
};

const moveDown = () => {
  if (!letters.value.length) return;
  selectedIndex.value = (selectedIndex.value + 1) % letters.value.length;
};

/** 톤암 각도: 선택된 인덱스에 따라 25도 범위에서 부드럽게 이동 */
const tonearmStyle = computed(() => {
  if (!letters.value.length || letters.value.length === 1) return { transform: 'rotate(0deg)' };
  const rotation = (selectedIndex.value / (letters.value.length - 1)) * 25 - 10;
  return { transform: `rotate(${rotation}deg)` };
});
</script>

<style scoped>
/* 전체 */
.letter-page {
  position: relative;
  width: 100vw;
  height: 100vh;
  background: radial-gradient(1200px 800px at 50% 80%, #fff2cc, #fffbeb 50%, #fffef7 100%);
  overflow: hidden;
  font-family: 'Montserrat', sans-serif;
}

/* 제목 */
.page-title {
  position: absolute;
  top: 1.5vh;
  left: 50%;
  transform: translateX(-50%);
  font-family: 'Bebas Neue', sans-serif;
  font-size: clamp(3rem, 6vw, 5rem);
  color: #3d5afe;
  letter-spacing: 4px;
  z-index: 300;
  white-space: nowrap;
  text-shadow: 0 2px 0 #fff;
}

/* 배경음악 플레이어 */
.music-player {
  position: absolute;
  top:65%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: clamp(320px, 45vw, 600px);
  height: clamp(220px, 35vh, 400px);
  background: rgba(255, 255, 255, 0.95);
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
  overflow: hidden;
  z-index: 999;
  backdrop-filter: blur(8px);
}
.music-header {
  padding: 10px 14px;
  font-weight: 700;
  border-bottom: 1px solid rgba(0,0,0,0.06);
}
.music-body {
  padding: 12px 14px 14px;
}
.music-input {
  width: 100%;
  border: 1px solid rgba(0,0,0,0.12);
  border-radius: 10px;
  padding: 10px 12px;
  font-size: 0.9rem;
  outline: none;
}
.music-input:focus {
  border-color: #3d5afe;
  box-shadow: 0 0 0 3px rgba(61,90,254,0.12);
}
.music-iframe-wrap {
  margin-top: 10px;
  position: relative;
  width: 100%;
  aspect-ratio: 16/9;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(0,0,0,0.12);
}
.music-iframe-wrap iframe {
  width: 100%;
  height: 100%;
  display: block;
}
.music-hint {
  color: #777;
  font-size: 0.9rem;
  margin-top: 8px;
}

/* 로딩/에러 */
.status-message {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 1.5rem;
  color: #aaa;
}
.status-message.error { color: #d9534f; }

/* 선택된 편지 카드 */
.selected-letter-card {
  position: absolute;
  top: 30%;               /* 위로 이동 */
  left: 50%;
  transform: translate(-50%, -50%);
  width: clamp(700px, 50vw, 600px);  /* 크기 확대 */
  height: 400px;
  min-height: 280px;
  background-color: white;
  border-radius: 16px;
  box-shadow: 0 12px 32px rgba(0,0,0,0.18);
  padding: 22px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  z-index: 220;
  border: 1px solid rgba(0,0,0,0.06);
}

.letter-content {
  margin: 0;
  font-size: 1rem;
  color: #444;
  line-height: 1.7;
  white-space: pre-wrap;
  word-break: break-word;
  flex-grow: 1;
}
.letter-name {
  margin-top: 16px;
  font-size: 0.92rem;
  color: #888;
  text-align: right;
  font-weight: 600;
}

/* 검은 LP 반원 영역 */
.record-half {
  position: absolute;
  width: min(120vw, 120vh);
  height: min(120vw, 120vh);
  left: 50%;
  bottom: calc(-0.66 * min(120vw, 120vh));
  transform: translateX(-50%);
  overflow: visible;
  pointer-events: none;
}
.record-core {
  position: absolute;
  width: 100%;
  height: 100%;
  left: 50%;
  bottom: 0;
  transform: translateX(-50%);
}
.record-disc {
  position: absolute;
  width: 100%;
  height: 100%;
  left: 50%;
  bottom: 0;
  transform: translateX(-50%);
  border-radius: 50%;
  background: radial-gradient(60% 60% at 50% 50%, #1d1d1d, #0f0f10 60%, #080808 100%);
  box-shadow: 0 -10px 40px rgba(0, 0, 0, 0.2) inset, 0 -10px 40px rgba(0, 0, 0, 0.08);
  animation: record-slow-spin 30s linear infinite;
}


/* 레코드 홈: 더 얇고 은은하게 */
.record-groove {
  position: absolute;
  border-radius: 50%;
  border: 1px solid rgba(255,255,255,0.07);
  box-sizing: border-box;
  pointer-events: none;
  animation: grooves-rotate 20s linear infinite;
}
.groove-1 { width: 92%; height: 92%; top: 4%; left: 4%; }
.groove-2 { width: 78%; height: 78%; top: 11%; left: 11%; animation-duration: 28s; }
.groove-3 { width: 62%; height: 62%; top: 19%; left: 19%; animation-duration: 36s; }

/* 라벨(센터) */
.record-label {
  position: absolute;
  width: min(22vw, 22vh);
  height: min(22vw, 22vh);
  min-width: 180px;
  min-height: 180px;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  background: radial-gradient(80% 80% at 50% 50%, #ffd166, #ff9f1c 70%, #ff7b00 100%);
  border: 12px solid #fff;
  border-radius: 50%;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
  display: grid;
  place-items: center;
}

.label-text {
  font-family: 'Bebas Neue', sans-serif;
  font-size: clamp(1.6rem, 4vw, 3rem);
  color: #222;
  letter-spacing: 2px;
}

/* 애니메이션 */
@keyframes record-slow-spin {
  from { transform: translateX(-50%) rotate(0); }
  to   { transform: translateX(-50%) rotate(360deg); }
}
@keyframes grooves-rotate {
  from { transform: rotate(0); }
  to   { transform: rotate(360deg); }
}

/* 톤암 */
.tonearm {
  position: absolute;
  /* 톤암 컨테이너 크기: 톤암 길이에 맞게 */
  width: 250px;     /* 톤암 몸통 + 머리 크기 */
  height: 1200px;     /* 톤암 높이 */

  /* 화면 위치 (필요에 따라 조정) */
  top: 20vh;
  right: 10vw;

  /* 톤암 회전 기준점 = 톤암 머리 위치로 설정 */
  /* 머리는 오른쪽 끝에 있으므로 transform-origin은 오른쪽 중앙 */
  transform-origin: 100% 50%;

  /* 초기 각도 */
  transform: rotate(35deg);

  transition: transform 0.7s ease-in-out;
  z-index: 240;
  filter: drop-shadow(0 6px 12px rgba(0, 0, 0, 0.25));
}

/* 톤암 머리 (큰 동그라미) */
.tonearm-head {
  position: absolute;
  right: 0;         /* 톤암 컨테이너 오른쪽 끝 */
  top: 50%;         /* 수직 중앙 */
  width: 40px;      /* 큰 동그라미 크기 */
  height: 40px;
  background: #c0c0c0;
  border-radius: 50%;
  box-shadow: 0 0 6px rgba(0,0,0,0.15);
  transform: translateY(-50%);
}

/* 톤암 몸통 (긴 직선) */
.tonearm-arm {
  position: absolute;
  right: 40px;      /* 톤암 머리 왼쪽 바로 옆에서 시작 */
  top: 50%;
  width: 500px;     /* 몸통 길이 */
  height: 6px;
  background: linear-gradient(90deg, #eaeaea, #cfcfcf);
  border-radius: 3px;
  transform: translateY(-50%);
}

/* 톤암 발 (작은 동그라미) */
.tonearm-pivot {
  position: absolute;
  right: 540px;     /* 몸통 시작 지점 왼쪽 끝 (머리 오른쪽 끝에서 220px 떨어진 곳) */
  top: 50%;
  width: 20px;      /* 작은 동그라미 크기 */
  height: 20px;
  background: #888;
  border-radius: 50%;
  box-shadow: 0 0 4px rgba(0,0,0,0.2);
  transform: translateY(-50%);
}




/* 이동 버튼 */
.controls {
  position: absolute;
  bottom: 40px;
  left: 40px;
  display: flex;
  gap: 15px;
  z-index: 260;
}
.controls button {
  width: 60px; height: 60px;
  border: none; border-radius: 50%;
  background-color: white;
  box-shadow: 0 5px 15px rgba(0,0,0,0.15);
  font-size: 1.5rem; color: #0288d1;
  cursor: pointer; transition: all 0.2s ease;
}
.controls button:hover {
  transform: translateY(-3px);
  background-color: #e3f2fd;
}

/* (기존) 중앙 원형 이미지는 라벨로 대체했으니 기본 숨김
.center-image { display: none; }
*/
</style>
