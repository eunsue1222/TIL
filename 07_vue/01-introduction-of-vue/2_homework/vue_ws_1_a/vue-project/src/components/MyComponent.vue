<template>
  <div class="my-component">
    <header class="header">
      <h1>Gallery</h1>
    </header>
    <main class="main">
      <div>카드</div>
    </main>
  </div>  
</template>

<script setup>
import { ref } from 'vue'
import sample from '../assets/sample.png'
const sampleImage = ref(sample)
</script>

<style scoped>
</style>
