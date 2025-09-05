<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <button class="close-btn" @click="$emit('close')">×</button>
      <iframe
        :src="`https://www.youtube.com/embed/${video.id.videoId}`"
        frameborder="0"
        allowfullscreen
        class="video-iframe"
      ></iframe>
      <h3>{{ video.snippet.title }}</h3>
      <p>{{ video.snippet.channelTitle }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  video: Object
})
</script>

<style scoped>
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
  background: white;
  padding: 20px 30px;
  border-radius: 10px;
  position: relative;
  width: 80%;
  max-width: 720px;
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

.video-iframe {
  width: 100%;
  height: 400px;
  border-radius: 8px;
  margin-bottom: 10px;
}
</style>
