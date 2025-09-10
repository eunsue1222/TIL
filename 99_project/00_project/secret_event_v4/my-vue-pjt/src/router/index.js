import { createRouter, createWebHistory } from 'vue-router'
// 1. 방금 만든 Home.vue를 import 합니다.
import Home from '../views/Home.vue' 
import Letters from '../views/Letters.vue'

const routes = [
  // 2. 기본 경로('/')를 Home 컴포넌트로 설정합니다.
  {
    path: '/',
    name: 'home',
    component: Home
  },
  // 3. 기존의 '/letters' 경로는 그대로 유지합니다.
  {
    path: '/letters',
    name: 'letters',
    component: Letters
  }
]

const router = createRouter({
  // --- [수정] ---
  // process.env.BASE_URL 대신 import.meta.env.BASE_URL을 사용합니다.
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
