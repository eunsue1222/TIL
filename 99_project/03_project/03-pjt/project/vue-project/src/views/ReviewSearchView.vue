<template>
  <div class="review-search-view">
    <header class="search-header">
      <input v-model="query" @keyup.enter="search" placeholder="영화 제목을 검색하세요" />
      <button @click="search">검색</button>
    </header>

    <div v-if="loading" class="loading">검색 중...</div>
    <div v-if="error" class="error">{{ error }}</div>

    <div v-if="videos.length" class="video-list">
      <YoutubeCard
        v-for="video in videos"
        :key="video.id.videoId"
        :video="video"
        @click.native="openModal(video)"
      />
    </div>

    <YoutubeReviewModal
      v-if="showModal"
      :video="selectedVideo"
      @close="showModal = false"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import YoutubeCard from '../components/YoutubeCard.vue'
import YoutubeReviewModal from '../components/YoutubeReviewModal.vue'

const API_KEY = import.meta.env.VITE_YOUTUBE_API_KEY
const query = ref('')
const videos = ref([])
const loading = ref(false)
const error = ref(null)
const showModal = ref(false)
const selectedVideo = ref(null)

async function search() {
  if (!query.value.trim()) {
    error.value = '검색어를 입력하세요.'
    return
  }
  error.value = null
  loading.value = true
  videos.value = []
  selectedVideo.value = null

  const searchQuery = encodeURIComponent(query.value + ' review')
  const url = `https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q=${searchQuery}&type=video&key=${API_KEY}`

  try {
    const res = await fetch(url)
    const data = await res.json()

    if (data.error) {
      error.value = data.error.message
      return
    }

    videos.value = data.items
  } catch (err) {
    error.value = '검색 중 오류가 발생했습니다.'
    console.error(err)
  } finally {
    loading.value = false
  }
}

function openModal(video) {
  selectedVideo.value = video
  showModal.value = true
}
</script>

<style scoped>
.review-search-view {
  padding: 20px;
}

.search-header {
  display: flex;
  gap: 8px;
  margin-bottom: 20px;
}

input {
  flex-grow: 1;
  padding: 8px;
  font-size: 16px;
}

button {
  background-color: #0066ff;
  color: white;
  border: none;
  padding: 9px 20px;
  cursor: pointer;
  border-radius: 4px;
  font-weight: bold;
}

button:hover {
  background-color: #004fcc;
}

.loading {
  margin-top: 20px;
  color: #555;
}

.error {
  margin-top: 20px;
  color: red;
}

.video-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
</style>
