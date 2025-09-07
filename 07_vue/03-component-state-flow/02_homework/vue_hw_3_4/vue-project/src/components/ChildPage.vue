<template>
  <div class="child-box">
    <h3>자식 페이지입니다.</h3>
    <p>이름 : {{ child.name }}</p>
    <p>나이 : {{ child.age }}</p>
    <p>용돈 : {{ child.balance.toLocaleString() }}</p>

    <!-- 버튼 클릭 시 부모에게 이벤트 전달 -->
    <button @click="requestAllowance">용돈 주세요.</button>
  </div>
</template>

<script setup>
const props = defineProps({
  child: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['giveMeAllowance'])

function requestAllowance() {
  emit('giveMeAllowance', props.child)
}
</script>

<style scoped>
.child-box {
  border: 1px solid #ccc;
  padding: 16px;
  margin-bottom: 12px;
  background-color: #fff;
}
</style>
