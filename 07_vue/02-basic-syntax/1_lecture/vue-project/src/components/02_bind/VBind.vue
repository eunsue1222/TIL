<template>
  <div>
    <!-- :[속성이름]: 동적으로 바인딩 -->
    <img :src="imageSrc"> <!-- v-bind:src="imageSrc" -->
    <a :href="myUrl">Move to url</a>
    <p :[dynamicattr]="dynamicValue">Dynamic Attr</p>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const imageSrc = ref('https://picsum.photos/200')
  const myUrl = ref('https://www.google.com/')
  const dynamicattr = ref('title')
  const dynamicValue = ref('Hello Vue.js')
</script>

<style scoped>

</style>