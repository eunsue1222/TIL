<template>
  <div class="app-wrapper"> <!-- ✅ 가장 바깥쪽 테두리 -->
    <ParentPage />
  </div>
</template>

<script setup>
import ParentPage from './components/ParentPage.vue'
</script>

<style scoped>
.app-wrapper {
  border: 1px solid #aaa;
  margin: 10px;
}
</style>
