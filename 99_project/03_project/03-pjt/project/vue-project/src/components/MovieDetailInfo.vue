<!-- src/components/MovieDetailInfo.vue -->
<template>
  <div class="detail-container">
    <img :src="posterUrl" alt="poster" class="poster" />
    <h2>{{ movie.title }}</h2>
    <p><strong>개봉일:</strong> {{ movie.release_date }}</p>
    <p><strong>러닝타임:</strong> {{ movie.runtime }}분</p>
    <p><strong>TMDB 평점:</strong> {{ movie.vote_average }}</p>
    <p><strong>장르:</strong> {{ movie.genres.map(g => g.name).join(', ') }}</p>
    <p class="overview">{{ movie.overview }}</p>
  </div>
</template>

<script setup>
const props = defineProps({
  movie: Object,
})
const posterUrl = `https://image.tmdb.org/t/p/w500${props.movie.poster_path}`
</script>

<style scoped>
.detail-container {
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
}
.poster {
  width: 300px;
  height: auto;
  margin-bottom: 20px;
}
.overview {
  margin-top: 20px;
  line-height: 1.6;
}
</style>
