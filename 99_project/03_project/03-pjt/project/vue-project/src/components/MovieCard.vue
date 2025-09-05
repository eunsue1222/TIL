<!-- src/components/MovieCard.vue -->
<template>
  <router-link :to="`/${movie.id}`" class="movie-card-link">
    <div class="movie-card">
      <img :src="posterUrl" alt="poster" class="poster" />
      <div class="info">
        <h3 class="title">{{ movie.title }}</h3>
        <p class="overview">{{ movie.overview }}</p>
      </div>
    </div>
  </router-link>
</template>

<script setup>
const props = defineProps({
  movie: Object,
})

const posterUrl = `https://image.tmdb.org/t/p/w500${props.movie.poster_path}`
</script>

<style scoped>
.movie-card {
  width: 300px;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
  transition: transform 0.2s ease;
}

.movie-card:hover {
  transform: scale(1.02);
}

.poster {
  width: 100%;
  height: 450px;
  object-fit: cover;
}

.info {
  padding: 10px;
}

.title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 8px;
}

.overview {
  font-size: 14px;
  color: #333;
  max-height: 100px;
  overflow: hidden;
  text-overflow: ellipsis;
  line-height: 1.4;
}
</style>
