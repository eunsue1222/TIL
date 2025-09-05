<template>
  <div v-if="movie" class="movie-detail-view">
    <MovieDetailInfo :movie="movie" />

    <div class="trailer-section">
      <h3>공식 예고편</h3>
      <button @click="showTrailer = true" class="trailer-btn">
        ▶️ 예고편 보기
      </button>
    </div>

    <!-- 예고편 모달 -->
    <div v-if="showTrailer" class="modal-overlay" @click.self="showTrailer = false">
      <div class="modal-content">
        <button class="close-btn" @click="showTrailer = false">×</button>
        <h4>{{ movie.title }} 공식 예고편</h4>
        <iframe
          v-if="trailerKey"
          :src="`https://www.youtube.com/embed/${trailerKey}`"
          frameborder="0"
          allowfullscreen
          class="trailer-iframe"
        ></iframe>
        <p v-else>예고편을 불러오는 중입니다...</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import MovieDetailInfo from '../components/MovieDetailInfo.vue'

const route = useRoute()
const movie = ref(null)
const showTrailer = ref(false)
const trailerKey = ref(null)

const API_KEY = import.meta.env.VITE_TMDB_API_KEY
const movieId = route.params.movieId

const detailURL = `https://api.themoviedb.org/3/movie/${movieId}?api_key=${API_KEY}&language=ko-KR`
const videoURL = `https://api.themoviedb.org/3/movie/${movieId}/videos?api_key=${API_KEY}&language=ko-KR`

onMounted(async () => {
  try {
    const res = await fetch(detailURL)
    movie.value = await res.json()
  } catch (err) {
    console.error('영화 상세 정보 불러오기 실패:', err)
  }
})

// 모달이 열릴 때 예고편 정보 받아오기
watch(showTrailer, async (newVal) => {
  if (newVal && !trailerKey.value) {
    try {
      const res = await fetch(videoURL)
      const data = await res.json()
      // YouTube 타입이고, official이거나 'Trailer' 타입인 영상 우선 선택
      const officialTrailer = data.results.find(
        v => v.site === 'YouTube' && (v.type === 'Trailer' || v.official)
      )
      trailerKey.value = officialTrailer ? officialTrailer.key : null
    } catch (err) {
      console.error('예고편 정보 불러오기 실패:', err)
    }
  }
})
</script>

<style scoped>
.movie-detail-view {
  max-width: 700px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

.trailer-section {
  margin-top: 40px;
  margin-bottom: 40px;
}

.trailer-btn {
  background-color: #ff3d00;
  color: white;
  border: none;
  padding: 12px 24px;
  font-size: 16px;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.trailer-btn:hover {
  background-color: #e63600;
}

/* 모달 스타일 */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(50, 50, 50, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.modal-content {
  background-color: white;
  padding: 20px 30px;
  border-radius: 10px;
  position: relative;
  max-width: 720px;
  width: 90%;
  text-align: center;
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 15px;
  font-size: 28px;
  font-weight: bold;
  border: none;
  background: none;
  cursor: pointer;
}

.trailer-iframe {
  width: 100%;
  height: 400px;
  margin-top: 10px;
  border-radius: 6px;
}
</style>
