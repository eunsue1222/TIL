<template>
  <div class="outer-box"> <!-- ✅ 가장 바깥 큰 테두리 -->
    <h1>부모 페이지입니다.</h1>
    <ChildPage
      v-for="(child, index) in children"
      :key="index"
      :child="child"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ChildPage from './ChildPage.vue'

const children = ref([
  { name: '김하나', age: 30 },
  { name: '김두리', age: 20 },
  { name: '김서이', age: 10 }
])
</script>

<style scoped>
.outer-box {
  border: 1px solid #999;
  padding: 20px;
  margin: 20px;
}
</style>
