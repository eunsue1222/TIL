<template>
  <div class="youtube-card" @click="$emit('click')">
    <img :src="video.snippet.thumbnails.medium.url" alt="thumbnail" />
    <div class="info">
      <h4>{{ video.snippet.title }}</h4>
      <p>{{ video.snippet.channelTitle }}</p>
      <p>{{ new Date(video.snippet.publishedAt).toLocaleDateString() }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  video: Object
})
</script>

<style scoped>
.youtube-card {
  display: flex;
  cursor: pointer;
  border: 1px solid #ddd;
  border-radius: 6px;
  overflow: hidden;
  transition: box-shadow 0.3s ease;
}

.youtube-card:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

img {
  width: 160px;
  object-fit: cover;
}

.info {
  padding: 10px;
  flex-grow: 1;
}

h4 {
  font-size: 16px;
  margin: 0 0 6px 0;
}

p {
  margin: 2px 0;
  color: #555;
  font-size: 14px;
}
</style>
