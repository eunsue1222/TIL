<template>
  <div id="app">
    <h1>조건문 연습하기</h1>

    <button @click="toggleLogin">Login/Logout</button>

    <div v-if="isLogin">
      <li>유저네임: {{ user.userName }}</li>
      <li>관리자여부: {{ user.isAdmin }}</li>
      <li>비밀번호: {{ user.passWord }}</li>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'

const isLogin = ref(false)

const user = reactive({
  userName: 'admin',
  isAdmin: true,
  passWord: '1q2w3e4r'
})

function toggleLogin() {
  isLogin.value = !isLogin.value
}
</script>

<style scoped>
button {
  margin-bottom: 10px;
}
</style>
