import { createRouter, createWebHistory } from 'vue-router'

import Letters from '../views/Letters.vue' // 경로를 실제 파일 위치에 맞게 수정하세요.

const routes = [
  // ... 다른 라우트들
  {
    // 2. 새로운 라우트 객체를 추가합니다.
    path: '/letters',
    name: 'letters',
    component: Letters
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})
// 막줄 routes=[], 일 경우 error [not found]

export default router
