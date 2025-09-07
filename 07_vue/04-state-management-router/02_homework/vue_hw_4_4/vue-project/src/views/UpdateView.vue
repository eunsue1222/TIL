<template>
  <div>
    <h2>데이터 수정 페이지</h2>
    <p>이름: {{ user.name }}</p>
    <p>잔고: {{ user.balance }}</p>
    <button @click="increase">+</button>
  </div>
</template>

<script setup>
import { useBalanceStore } from '@/stores/balance'
import { onMounted, reactive } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const store = useBalanceStore()

const user = reactive({ name: '', balance: 0 })

onMounted(() => {
  const name = route.params.name
  const found = store.getBalanceByName(name)
  if (found) {
    user.name = found.name
    user.balance = found.balance
  }
})

function increase() {
  store.increaseBalance(user.name, 1000)
  user.balance += 1000
}
</script>
