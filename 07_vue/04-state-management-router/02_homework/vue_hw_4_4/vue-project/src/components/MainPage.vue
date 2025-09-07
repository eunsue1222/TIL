<template>
  <div>
    <p>이름: {{ info.name }}</p>
    <p>잔고: {{ info.balance }}</p>
    <button @click="goUpdate">updateBalance</button>
    <hr />
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const props = defineProps({
  info: Object
})

const router = useRouter()

function goUpdate() {
  router.push({ name: 'update', params: { name: props.info.name } })
}
</script>
