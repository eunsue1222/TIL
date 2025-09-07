<!-- src/components/MainPage.vue -->
<template>
  <div class="main">
    <h1 class="title">pinia 연습하기</h1>
    
    <div class="family-list">
      <ParentPage
        v-for="(family, index) in familyStore.familyInfo"
        :key="index"
        :family="family"
      />
    </div>
  </div>
</template>

<script setup>
import { useFamilyStore } from '../stores/family';
import ParentPage from './ParentPage.vue';

const familyStore = useFamilyStore();
</script>

<style scoped>
.main {
  width: 100vw; /* 화면 전체 너비 */
  padding: 0 20px; /* 좌우 약간 여백 */
  margin: 0; /* 중앙 정렬 없애기 */
  box-sizing: border-box; /* 패딩 포함 너비 계산 */
}

.title {
  text-align: left;
  font-size: 2rem;
  font-weight: bold;
  margin: 20px 0;
  width: 100%; /* 전체 너비 */
}
.family-list {
  text-align: center; /* 카드들은 가운데 정렬 유지 */
}
</style>


