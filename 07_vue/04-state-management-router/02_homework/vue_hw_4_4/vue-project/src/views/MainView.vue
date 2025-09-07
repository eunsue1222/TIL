<template>
  <div>
    <h2>메인 페이지</h2>
    <MainPage
      v-for="item in balances"
      :key="item.name"
      :info="item"
    />
  </div>
</template>

<script setup>
import { useBalanceStore } from '@/stores/balance'
import MainPage from '@/components/MainPage.vue'

const store = useBalanceStore()
const balances = store.balances
</script>
