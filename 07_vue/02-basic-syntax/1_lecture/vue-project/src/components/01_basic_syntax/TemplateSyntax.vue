<template>
  <div>
    <!-- template syntax -->
    <p>Message: {{ msg }}</p>
    <div v-html="rawHtml"></div> <!-- 사용자 입력값 v-html에 할당 금지 -->>
    <div v-bind:id="dynamicId"></div>
    {{ number + 1 }}
    {{ ok ? 'YES' : 'NO' }}
    {{ msg.split('').reverse().join('') }}

    <!-- directive -->
    <div v-bind:id="`list-${id}`"></div>
    <p v-if="seen">Hi there</p>
    <a v-bind:href="myUrl">Link</a>
    <button v-on:click="doSomething">button</button>
    <form v-on:submit.prevent="onSubmit"> <!-- prevent: 페이지 새로고침 -->
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  
  const msg = 'Hello'
  const rawHtml = ref('<span style="color:red">This should be red.</span>')
  const dynamicId = ref('my-id')
  const number = ref(1)
  const ok = ref(true)
  const seen = ref(true)
  const id = ref(100)
  const myUrl = 'https://www.google.co.kr/'

  const doSomething = function () {
    console.log('button clicked')
  }
  const onSubmit = function () {
    console.log('form submitted')
  }
</script>

<style scoped>

</style>