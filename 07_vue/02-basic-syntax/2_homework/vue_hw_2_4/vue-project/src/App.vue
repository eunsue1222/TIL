<template>
  <div id="app">
    <h1>글꼴 테스트기</h1>
    <ul>
      <li v-for="font in fonts" :key="font.style">
        <label>{{ font.style }} 테스트</label>
        <input type="text" v-model="font.text" />
        <div
          v-if="font.text"
          class="preview"
          :style="{ fontFamily: font.style }"
        >
          {{ font.text }}
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { reactive } from 'vue'

// 글꼴 배열: style + text
const fonts = reactive([
  { style: '바탕', text: '' },
  { style: '휴먼엽서체', text: '' },
  { style: '궁서체', text: '' }
])
</script>

<style scoped>
body {
  font-family: sans-serif;
  padding: 20px;
}
h1 {
  margin-bottom: 30px;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  margin-bottom: 20px;
  padding: 15px;
}
label {
  display: block;
  font-weight: bold;
  margin-bottom: 10px;
}
input {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
  box-sizing: border-box;
}
</style>
