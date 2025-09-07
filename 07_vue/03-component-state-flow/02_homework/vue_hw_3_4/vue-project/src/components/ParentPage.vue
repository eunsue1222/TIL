<template>
  <div class="outer-box">
    <h1>부모 페이지입니다.</h1>
    <ChildPage
      v-for="(child, index) in children"
      :key="index"
      :child="child"
      @giveMeAllowance="updateBalance"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ChildPage from './ChildPage.vue'

// 자식 정보 배열
const children = ref([
  { name: '김하나', age: 30, balance: 102000 },
  { name: '김두리', age: 20, balance: 12000 },
  { name: '김서이', age: 10, balance: 4000 }
])

// 버튼 클릭 이벤트 처리
function updateBalance(child) {
  child.balance += 1000
}
</script>

<style scoped>
.outer-box {
  border: 1px solid #999;
  padding: 20px;
  margin: 20px;
}
</style>
