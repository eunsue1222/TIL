<!-- src/views/MovieListView.vue -->
<template>
  <div>
    <h2>🎥 최고 평점 영화 목록</h2>
    <div v-if="movies.length === 0">Loading...</div>
    <div class="movie-grid">
      <MovieCard v-for="movie in movies" :key="movie.id" :movie="movie" />
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import MovieCard from '../components/MovieCard.vue'

const movies = ref([])

const API_KEY = import.meta.env.VITE_TMDB_API_KEY
const TMDB_URL = `https://api.themoviedb.org/3/movie/top_rated?api_key=${API_KEY}&language=ko-KR`

onMounted(async () => {
  try {
    const res = await fetch(TMDB_URL)
    const data = await res.json()
    movies.value = data.results
  } catch (err) {
    console.error('영화 목록 로딩 실패:', err)
  }
})
</script>

<style scoped>
.movie-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 30px;
  justify-content: center;
  margin-top: 20px;
}
</style>
