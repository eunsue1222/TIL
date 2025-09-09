<template>
  <div class="letters-page">
    <h1 class="page-title">14th 대전 4반!!</h1>

    <!-- 로딩/에러 -->
    <p v-if="loading" class="state-msg">불러오는 중…</p>
    <p v-else-if="error" class="state-msg err">{{ error }}</p>

    <!-- 상단 롤링페이퍼 -->
    <div class="note-wrap" v-if="activePerson">
      <div class="note-card">
        <div class="note-text" v-html="activePerson.letter"></div>
        <div class="note-from"> {{ activePerson.name }} 드림 </div>
      </div>
    </div>

    <!-- 신청곡 카드 -->
    <div class="music-card" v-if="activePerson">
      <div class="music-header">
        <span class="music-icon">🎵</span>
        <span class="music-title">{{ activePerson.musicTitle || '신청곡' }}</span>
      </div>
      <div class="music-meta">
        <div class="music-desc">
          {{ activePerson.musicNote || `오늘은 ${activePerson.name}가(이) 신청한 노래!` }}
        </div>
      </div>

      <div class="music-player" v-if="embedUrl">
        <iframe
          :src="embedUrl"
          title="YouTube player"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
        ></iframe>
      </div>
      <div class="music-hint" v-else>
        유효한 유튜브 링크가 없어요. (예: https://youtu.be/xxxx 또는 https://www.youtube.com/watch?v=xxxx)
      </div>
    </div>

    <!-- 컨트롤 -->
    <div class="controls">
      <button class="btn" @click="prevPerson">◀ 이전</button>
      <button class="btn primary" @click="togglePlay">
        {{ isPlaying ? '⏸︎ Pause' : '▶ Play' }}
      </button>
      <button class="btn" @click="nextPerson">다음 ▶</button>
    </div>

    <!-- 아바타: 이전/현재/다음 3명만 -->
    <div class="avatars avatars--three" v-if="visiblePeople.length">
      <button
        v-for="(item, i) in visiblePeople"
        :key="item.role"
        class="avatar"
        :class="['role-' + item.role, { active: item.role === 'curr' }]"
        :title="item.role + ' — ' + item.person.name"
        @click="selectWindowItem(i)"
      >
        {{ item.person.name }}
      </button>
    </div>

    <!-- 턴테이블 -->
    <div class="turntable">
      <div class="vinyl" :class="{ spinning: isPlaying }" :style="{ '--rotation-speed': rotationSpeed }">
        <div class="label">
          <img
            v-if="activePerson?.photoUrl"
            :src="activePerson.photoUrl"
            alt="라벨 이미지"
            class="label-image"
          />
          <div v-else class="label-title">{{ activePerson?.name || '' }}</div>
        </div>
      </div>

      <div class="tonearm" :class="{ engaged: isPlaying }" @transitionend="onTonearmSettled">
        <div class="arm"></div>
        <div class="head"></div>
        <div class="stylus"></div>
      </div>
    </div>

    <div class="page-badge">21</div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue'
import axios from 'axios'

// assets의 png/jpg/jpeg/webp를 전부 가져와서 "파일이름(확장자 제외) -> URL" 매핑
const rawImageModules = import.meta.glob('/src/assets/*.{png,jpg,jpeg,webp}', {
  eager: true,
  import: 'default',
})
const photoMapByName = Object.fromEntries(
  Object.entries(rawImageModules).map(([path, url]) => {
    const filename = (path.split('/').pop() || '').trim()               // e.g. '김소원.png'
    const base = filename.replace(/\.(png|jpe?g|webp)$/i, '')            // ➜ '김소원'
    return [base, url]                                                   // { '김소원': 'blob/...' }
  })
)

/* ------------ 상태 ------------ */
const people = ref([])          // Django에서 받아온 리스트
const activeIndex = ref(0)
const isPlaying = ref(false)
const rotationSpeed = '4s'
const loading = ref(true)
const error = ref('')


/* ------------ 로딩 ------------ */
onMounted(async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/letters/')
    const rows = Array.isArray(res.data) ? res.data : []

    // Django 모델(name, content, music_content, music, link) → 프론트 구조 매핑
    people.value = rows.map(r => ({
      id: r.id ?? r.name,
      name: r.name || '',
      letter: toParagraphHtml(r.content || ''),
      musicNote: r.music_content || '',
      musicTitle: r.music || '',
      youtubeUrl: r.link || '',
      photoUrl: photoMapByName[r.name] || '', 
    }))
  } catch (e) {
    console.error(e)
    error.value = '데이터 로딩에 실패했습니다.'
  } finally {
    loading.value = false
  }
})

/* ------------ 도우미 ------------ */
function toParagraphHtml(text) {
  const t = (text || '').trim()
  if (!t) return ''
  return t.split(/\r?\n/).map(line => `<p>${escapeHtml(line)}</p>`).join('')
}
function escapeHtml(s) {
  return s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;')
}

/* ------------ 파생값 ------------ */
const activePerson = computed(() => people.value[activeIndex.value] || null)

const embedUrl = computed(() => {
  const url = activePerson.value?.youtubeUrl || ''
  const id = extractYouTubeId(url)
  return id ? `https://www.youtube.com/embed/${id}?autoplay=${isPlaying.value ? 1 : 0}&mute=0` : ''
})

function extractYouTubeId (url) {
  if (!url) return ''
  try {
    const short = url.match(/youtu\.be\/([a-zA-Z0-9_-]{6,})/)
    if (short) return short[1]
    const vParam = new URL(url).searchParams.get('v')
    if (vParam) return vParam
    const embed = url.match(/embed\/([a-zA-Z0-9_-]{6,})/)
    if (embed) return embed[1]
  } catch {}
  return ''
}

/* ------------ 3명 윈도우(이전/현재/다음) ------------ */
const visiblePeople = computed(() => {
  const n = people.value.length
  if (!n) return []
  const prev = (activeIndex.value - 1 + n) % n
  const curr = activeIndex.value
  const next = (activeIndex.value + 1) % n
  return [
    { person: people.value[prev], realIdx: prev, role: 'prev' },   // 이전사람
    { person: people.value[curr], realIdx: curr, role: 'curr' },   // 현재사람
    { person: people.value[next], realIdx: next, role: 'next' },   // 다음사람
  ]
})

function selectWindowItem(i) {
  if (!visiblePeople.value.length) return
  activeIndex.value = visiblePeople.value[i].realIdx
}

/* ------------ 컨트롤 ------------ */
function prevPerson () {
  const n = people.value.length
  if (!n) return
  activeIndex.value = (activeIndex.value - 1 + n) % n
}
function nextPerson () {
  const n = people.value.length
  if (!n) return
  activeIndex.value = (activeIndex.value + 1) % n
}
function togglePlay () { isPlaying.value = !isPlaying.value }
function onTonearmSettled () {}

watch(activeIndex, () => {/* 필요 시 확장 */})
</script>

<style scoped>
/* 페이지 레이아웃 */
.letters-page {
  min-height: 100vh;
  background: radial-gradient(ellipse at top, #fffdf5 0%, #f9f4e8 60%, #f2eddc 100%);
  color: #111;
  position: relative;
  overflow-x: hidden;
  padding-bottom: 120px;
  max-width: 800px;
  margin: 0 auto;
  box-shadow: 0 0 30px rgba(0,0,0,0.1);
}

.page-title {
  text-align: center;
  margin: 24px 0 10px;
  font-size: 40px;
  color: #2a5cff;
  letter-spacing: 2px;
  font-weight: 800;
}

/* 롤링페이퍼 카드 */
.note-wrap {
  display: flex;
  justify-content: center;
  margin-top: 24px;
}
.note-card {
  width: 600px; /* 메세지 너비 */
  height: 150px; /* 메세지 높이 */
  background: #ffffffcc;
  box-shadow: 0 10px 24px rgba(0,0,0,0.12);
  border-radius: 14px;
  padding: 18px 20px;
  backdrop-filter: blur(4px);
}
.note-text {
  line-height: 1.65;
  color: #333;
  min-height: 86px;
}
.note-from {
  text-align: right;
  color: #666;
  margin-top: 8px;
  font-size: 13px;
}

/* 신청곡 카드 */
.music-card {
  width: 600px; /* 신청곡 너비 */
  height: 350px; /* 신청곡 높이 */
  margin: 14px auto 0;
  border-radius: 14px;
  background: #fff;
  box-shadow: 0 10px 24px rgba(0,0,0,0.12);
  padding: 12px 14px 16px;
}
.music-header {
  display: flex;
  align-items: center;
  gap: 6px;
  font-weight: 700;
  margin-bottom: 6px;
}
.music-title { font-size: 16px; }
.music-meta { font-size: 14px; color: #666; margin-bottom: 10px; }
.music-player iframe {
  width: 100%;
  height: 285px;
  border-radius: 10px;
}
.music-hint {
  font-size: 13px;
  color: #888;
  padding: 20px;
  text-align: center;
  border: 1px dashed #e1e1e1;
  border-radius: 10px;
}

/* 턴테이블 */
.turntable {
  position: relative;
  /* --- [수정] 컨트롤이 위로 빠지면서 여백 조정 --- */
  margin-top: 36px;
  padding-top: 60px;
  padding-bottom: 120px;
  height: 600px; /* 높이 고정으로 레이아웃 안정화 */
  display: flex; /* 내부 요소 중앙 정렬을 위해 추가 */
  justify-content: center;
  align-items: center;
}

/* 가운데 이미지 */
.label-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
  border: 10px solid #ffffff;
}

/* LP 디스크 */
.vinyl {
  /* --- [수정] 고정 크기 --- */
  width: 600px;
  height: 600px;
  margin: 0 auto;
  background:
    radial-gradient(circle at center, #111 48%, #0a0a0a 52%),
    repeating-radial-gradient(circle at center, rgba(255,255,255,0.06) 0 2px, rgba(0,0,0,0) 2px 6px);
  border-radius: 50%;
  position: absolute; /* 턴테이블 내에서 위치 고정 */
  box-shadow: 0 30px 80px rgba(0,0,0,0.35) inset;
  animation: none;
}

/* 디스크 회전 */
.vinyl.spinning {
  animation: spin var(--rotation-speed, 4s) linear infinite;
}
@keyframes spin {
  to { transform: rotate(360deg); }
}

/* 중앙 라벨 */
.label {
  position: absolute;
  inset: 50%;
  width: 30%;
  aspect-ratio: 1/1;
  transform: translate(-50%, -50%);
  background: radial-gradient(circle at 60% 40%, #9bd1ff, #6aa8ff);
  border-radius: 50%;
  box-shadow: 0 0 0 10px #f9f9f9 inset;
  display: grid;
  place-items: center;
  text-align: center;
  color: #0d2a66;
}
.label-title {
  font-weight: 800;
  font-size: clamp(12px, 2.4vw, 20px);
}

/* 톤암 */
.tonearm {
  position: absolute;
  top: -5px;
  right: 150px;
  width: 280px;
  height: 40px;
  transform-origin: right center;
  transform: rotate(0deg); /* 정지 상태: 수직 위쪽 */
  transition: transform 0.8s ease-in-out;
  pointer-events: none;
  z-index: 5;
}
.tonearm.engaged {
  transform: rotate(-15deg); /* 재생 상태: 수직 아래쪽 */
}

.tonearm .arm {
  position: absolute;
  right: 0;
  top: 14px;
  width: 240px;
  height: 10px;
  background: linear-gradient(#ddd, #bbb);
  border-radius: 6px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.2);
}

.tonearm .head {
  position: absolute;
  right: 240px;
  top: 8px;
  width: 24px;
  height: 18px;
  background: #eaeaea;
  border-radius: 3px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.25);
}

.tonearm .stylus {
  position: absolute;
  right: 236px;
  top: 24px;
  width: 3px;
  height: 20px;
  background: #444;
  border-radius: 2px;
}

/* 컨트롤 */
.controls {
  display: flex;
  gap: 12px;
  justify-content: center;
  /* --- [수정] 신청곡 카드와의 여백 추가 --- */
  margin-top: 20px;
}
.btn {
  padding: 10px 14px;
  border-radius: 12px;
  background: #f0f2ff;
  border: 1px solid #d8e0ff;
  cursor: pointer;
  font-weight: 700;
}
.btn.primary {
  background: #2a5cff;
  color: white;
  border: 1px solid #2148c4;
}

/* 아바타 버튼 */
.avatars {
  display: flex;
  gap: 10px;
  justify-content: center;
  margin-top: 16px;
  flex-wrap: wrap;
}
.avatar {
  width: 64px; height: 64px;
  border-radius: 50%;
  border: 2px solid #dcdcdc;
  background: #f3f3f3 center/cover no-repeat;
  display: grid;
  place-items: center;
  font-size: 12px;
  cursor: pointer;
  transition: transform .15s ease, box-shadow .15s ease, border-color .15s ease;
}
.avatar.active {
  border-color: #2a5cff;
  box-shadow: 0 0 0 4px rgba(42,92,255,0.12);
  transform: translateY(-2px);
}

/* 장식 배지 */
.page-badge {
  position: fixed;
  bottom: 16px; right: 20px;
  width: 46px; height: 46px;
  border-radius: 50%;
  background: #5f95ff22;
  color: #2a5cff;
  display: grid; place-items: center;
  font-weight: 800;
  border: 1px solid #8fb0ff55;
}
</style>