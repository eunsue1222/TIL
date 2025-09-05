<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  movieTitle: String,
  show: Boolean,
})

const emit = defineEmits(['update:show'])

const videoId = ref(null)
const loading = ref(false)

// 영화 제목이 바뀔 때마다 Youtube API 호출
watch(
  () => props.movieTitle,
  async (newTitle) => {
    if (!newTitle) return
    loading.value = true
    const query = encodeURIComponent(newTitle + ' trailer')
    const key = import.meta.env.VITE_YOUTUBE_API_KEY
    try {
      const res = await fetch(
        `https://www.googleapis.com/youtube/v3/search?part=snippet&q=${query}&key=${key}&type=video&maxResults=1`
      )
      const data = await res.json()
      videoId.value = data.items?.[0]?.id.videoId || null
    } catch (error) {
      videoId.value = null
    }
    loading.value = false
  },
  { immediate: true }
)

function closeModal() {
  emit('update:show', false)
  videoId.value = null
}
</script>

<template>
  <div
    class="modal fade"
    :class="{ show: show }"
    tabindex="-1"
    style="display: block; background-color: rgba(0, 0, 0, 0.5);"
    v-if="show"
  >
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">{{ movieTitle }} 공식 예고편</h5>
          <button type="button" class="btn-close" @click="closeModal"></button>
        </div>
        <div class="modal-body text-center">
          <div v-if="loading">로딩 중...</div>
          <iframe
            v-if="videoId"
            width="100%"
            height="400"
            :src="`https://www.youtube.com/embed/${videoId}`"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
          ></iframe>
          <div v-else>예고편을 찾을 수 없습니다.</div>
        </div>
      </div>
    </div>
  </div>
</template>
