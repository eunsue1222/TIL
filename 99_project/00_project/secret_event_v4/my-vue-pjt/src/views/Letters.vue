<template>
  <div class="letters-page">
    <!-- [수정] 타이틀 옆에 PNG 이미지 추가 -->
    <h1 class="page-title">
      <span>14th 대전 4반!!</span>
      <img :src="titleIcon" alt="Title Icon" class="title-icon" />
    </h1>
    <!-- 로딩/에러 메시지 -->
    <p v-if="loading" class="state-msg">불러오는 중…</p>
    <p v-else-if="error" class="state-msg err">{{ error }}</p>

    <!-- [수정] 반응형 레이아웃을 위한 메인 컨테이너 추가 -->
    <div class="main-content" v-if="activePerson">
      
      <!-- 좌측 컨텐츠 패널 -->
      <div class="content-panel">
        <!-- 상단 롤링페이퍼 -->
        <div class="note-wrap">
          <div class="note-card">
            <div class="note-text" v-html="activePerson.letter"></div>
            <div class="note-from"> {{ activePerson.name }} 드림 </div>
          </div>
        </div>

        <!-- 신청곡 카드 -->
        <div class="music-card">
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
            유효한 유튜브 링크가 없어요.
          </div>
        </div>
      </div>

      <!-- 우측 플레이어 패널 -->
      <div class="player-panel">
        <!-- 컨트롤 -->
        <div class="controls">
          <button class="btn" @click="prevPerson">◀ 이전</button>
          <button class="btn primary" @click="togglePlay">
            {{ isPlaying ? '⏸︎ Pause' : '▶ Play' }}
          </button>
          <button class="btn" @click="nextPerson">다음 ▶</button>
        </div>

        <!-- 아바타 -->
        <div class="avatars avatars--three" v-if="visiblePeople.length">
          <button
            v-for="(item, i) in visiblePeople"
            :key="item.person.id"
            class="avatar"
            :class="{ active: item.role === 'curr' }"
            :title="item.person.name"
            @click="selectWindowItem(i)"
          >
            {{ item.person.name }}
          </button>
        </div>

        <!-- 턴테이블 -->
        <div class="turntable">
          <div class="vinyl" :class="{ spinning: isPlaying }">
            <div class="label">
              <img
                v-if="activePerson && activePerson.photoUrl"
                :src="activePerson.photoUrl" 
                alt="라벨 이미지"
                class="label-image"
              />
              <div v-else class="label-title">{{ activePerson?.name || '' }}</div>
            </div>
          </div>
          <div class="tonearm" :class="{ engaged: isPlaying }">
            <div class="arm"></div>
            <div class="head"></div>
            <div class="stylus"></div>
          </div>
        </div>
      </div>
    </div>

    <div class="page-badge">14</div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue'
import axios from 'axios'
import titleIcon from '@/assets/icon.png'

/* ------------ 상태 (State) ------------ */
const people = ref([])
const activeIndex = ref(0)
const isPlaying = ref(false)
const rotationSpeed = '4s'
const loading = ref(true)
const error = ref('')

/* ------------ 데이터 로딩 ------------ */
onMounted(async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/letters/')
    const rows = Array.isArray(res.data) ? res.data : []

    people.value = rows.map(r => ({
      id: r.id ?? r.name,
      name: r.name || '',
      letter: toParagraphHtml(r.content || ''),
      musicNote: r.music_content || '',
      musicTitle: r.music || '',
      youtubeUrl: r.music_link || '',
      photoUrl: r.image_link || '',
    }))
  } catch (e) {
    console.error("데이터 로딩 중 에러 발생:", e)
    error.value = '데이터를 불러오는 데 실패했습니다.'
  } finally {
    loading.value = false
  }
})

/* ------------ 도우미 함수 ------------ */
function toParagraphHtml(text) {
  const t = (text || '').trim()
  if (!t) return ''
  return t.split(/\r?\n/).map(line => `<p>${escapeHtml(line)}</p>`).join('')
}
function escapeHtml(s) {
  return s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;')
}

/* ------------ 파생값 (Computed Properties) ------------ */
const activePerson = computed(() => people.value[activeIndex.value] || null)

const embedUrl = computed(() => {
  const url = activePerson.value?.youtubeUrl || ''
  const id = extractYouTubeId(url)
  return id ? `https://www.youtube.com/embed/${id}?autoplay=${isPlaying.value ? 1 : 0}&mute=0` : ''
})

function extractYouTubeId (url) {
  if (!url) return ''
  try {
    const short = url.match(/youtu\.be\/([a-zA-Z0-9_-]{11})/)
    if (short) return short[1]
    const vParam = new URL(url).searchParams.get('v')
    if (vParam) return vParam
    const embed = url.match(/embed\/([a-zA-Z0-9_-]{11})/)
    if (embed) return embed[1]
  } catch {}
  return ''
}

/* ------------ 3명 윈도우(이전/현재/다음) 로직 ------------ */
const visiblePeople = computed(() => {
  const n = people.value.length
  if (!n) return []
  const prev = (activeIndex.value - 1 + n) % n
  const curr = activeIndex.value
  const next = (activeIndex.value + 1) % n
  return [
    { person: people.value[prev], realIdx: prev, role: 'prev' },
    { person: people.value[curr], realIdx: curr, role: 'curr' },
    { person: people.value[next], realIdx: next, role: 'next' },
  ]
})

function selectWindowItem(i) {
  if (!visiblePeople.value.length) return
  activeIndex.value = visiblePeople.value[i].realIdx
}

/* ------------ 컨트롤 로직 ------------ */
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
/* 페이지 레이아웃 (기본: 세로 배치) */
.letters-page {
  min-height: 100vh;
  background: radial-gradient(ellipse at top, #fffdf5 0%, #f9f4e8 60%, #f2eddc 100%);
  color: #111;
  position: relative;
  overflow-x: hidden;
  padding: 0 20px 120px;
  max-width: 1400px;
  margin: 0 auto;
}
.page-title {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 15px;
  text-align: center;
  margin: 24px 0 10px;
  font-size: 40px;
  color: #2a5cff;
  letter-spacing: 2px;
  font-weight: 800;
}
.title-icon {
  width: 100px;
  height: 100px;
}
.state-msg {
    text-align: center;
    padding: 40px;
    color: #888;
}
.state-msg.err {
    color: #d9534f;
}
.content-panel, .player-panel {
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
}

/* 롤링페이퍼 카드 */
.note-wrap {
  display: flex;
  justify-content: center;
  margin-top: 24px;
}
.note-card {
  width: 100%;
  min-height: 150px;
  background: #ffffffcc;
  box-shadow: 0 10px 24px rgba(0,0,0,0.12);
  border-radius: 14px;
  padding: 18px 20px;
  backdrop-filter: blur(4px);
  transition: min-height 0.3s ease;
}
.note-text {
  line-height: 1.65;
  color: #333;
}
.note-text :deep(p) { margin: 0 0 1em; }
.note-text :deep(p:last-child) { margin-bottom: 0; }
.note-from {
  text-align: right;
  color: #666;
  margin-top: 8px;
  font-size: 13px;
}

/* 신청곡 카드 */
.music-card {
  height: 350px;
  margin: 14px auto 0;
  border-radius: 14px;
  background: #fff;
  box-shadow: 0 10px 24px rgba(0,0,0,0.12);
  padding: 12px 14px 16px;
  display: flex;
  flex-direction: column;
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
.music-player {
    flex-grow: 1;
    display: flex;
    align-items: center;
    justify-content: center;
}
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
  width: 100%;
}

/* 턴테이블 */
.turntable {
  position: relative;
  margin-top: 36px;
  padding-top: 60px;
  padding-bottom: 120px;
  height: 600px;
  display: flex;
  justify-content: center;
  align-items: center;
}
/* --- [수정] --- */
/* LP 디스크 */
.vinyl {
  width: 600px;
  height: 600px;
  background:
    radial-gradient(circle at center, #111 48%, #0a0a0a 52%),
    repeating-radial-gradient(circle at center, rgba(255,255,255,0.06) 0 2px, rgba(0,0,0,0) 2px 6px);
  border-radius: 50%;
  position: absolute;
  box-shadow: 0 30px 80px rgba(0,0,0,0.35) inset;
  
  /* 애니메이션을 항상 정의하되, 기본 상태는 '정지'로 설정 */
  animation: spin 4s linear infinite;
  animation-play-state: paused;
}

/* 디스크 회전 */
.vinyl.spinning {
  /* .spinning 클래스는 이제 애니메이션을 '실행'하는 역할만 합니다. */
  animation-play-state: running;
}
@keyframes spin {
  to { transform: rotate(360deg); }
}

/* --- [추가] 반응형 레이아웃 --- */
@media (min-width: 1200px) {
  .main-content {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    gap: 40px;
    margin-top: 40px;
  }
  .content-panel { order: 1; flex: 0 0 600px; margin: 0; }
  .player-panel { order: 2; flex: 0 0 600px; margin: 0; }
  .turntable, .controls, .avatars { margin-top: 0; }
  .controls { margin-bottom: 16px; }
  .avatars { margin-bottom: 24px; }
  .turntable { padding-top: 0; }
}

@keyframes spin { to { transform: rotate(360deg); } }
.label {
  position: absolute;
  inset: 50%;
  width: 180px;
  height: 180px;
  transform: translate(-50%, -50%);
  background: radial-gradient(circle at 60% 40%, #9bd1ff, #6aa8ff);
  border-radius: 50%;
  box-shadow: 0 0 0 10px #f9f9f9 inset;
  display: grid;
  place-items: center;
  text-align: center;
  color: #0d2a66;
  overflow: hidden;
}
.label-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.label-title {
  font-weight: 800;
  font-size: clamp(12px, 2.4vw, 20px);
}

/* 톤암 */
.tonearm {
  position: absolute;
  
  /* --- [수정] --- */
  /* 컨테이너의 가장자리(top, right) 대신 중심(50%)을 기준으로 위치를 계산합니다. */
  /* 이렇게 하면 vinyl과의 상대적 위치가 항상 동일하게 유지됩니다. */
  top: calc(50% - 320px); /* 세로 위치 (중심에서 위로) */
  left: calc(50% - 30px);  /* 가로 위치 (중심에서 약간 왼쪽) */

  width: 280px;
  height: 40px;
  transform-origin: right center; /* 회전축은 그대로 오른쪽 중앙 */
  transform: rotate(0deg);
  transition: transform 0.8s ease-in-out;
  pointer-events: none;
  z-index: 5;
}
.tonearm.engaged { transform: rotate(-15deg); }
.tonearm .arm, .tonearm .head, .tonearm .stylus { position: absolute; }
.tonearm .arm { right: 0; top: 14px; width: 240px; height: 10px; background: linear-gradient(#ddd, #bbb); border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.2); }
.tonearm .head { right: 240px; top: 8px; width: 24px; height: 18px; background: #eaeaea; border-radius: 3px; box-shadow: 0 2px 6px rgba(0,0,0,0.25); }
.tonearm .stylus { right: 236px; top: 24px; width: 3px; height: 20px; background: #444; border-radius: 2px; }

/* 컨트롤 */
.controls {
  display: flex;
  gap: 12px;
  justify-content: center;
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
  background: #f3f3f3;
  display: grid;
  place-items: center;
  font-size: 12px;
  cursor: pointer;
  transition: transform .15s ease, box-shadow .15s ease, border-color .15s ease;
  text-align: center;
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

/* --- [추가] 반응형 레이아웃 --- */
/* 화면 너비가 1200px 이상일 때 아래 스타일이 적용됩니다. */
@media (min-width: 1200px) {
  .main-content {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    gap: 40px; /* 좌우 패널 사이의 간격 */
    margin-top: 40px;
  }

  .content-panel {
    order: 1; /* 좌측에 배치 */
    flex: 0 0 600px; /* 너비 600px 고정 */
    margin: 0;
  }

  .player-panel {
    order: 2; /* 우측에 배치 */
    flex: 0 0 600px; /* 너비 600px 고정 */
    margin: 0;
  }

  /* 가로 배치일 때 불필요한 상단 여백 제거 */
  .turntable, .controls, .avatars {
    margin-top: 0;
  }
  
  /* 컨트롤과 아바타를 턴테이블 위로 이동시키기 위한 순서 조정 */
  .controls {
      margin-bottom: 16px;
  }
  .avatars {
      margin-bottom: 24px;
  }
  .turntable {
      padding-top: 0;
  }
}
</style>