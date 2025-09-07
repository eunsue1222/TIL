<template>
  <div class="child-box">
    <h3>자식 페이지입니다.</h3>
    <p>이름 : {{ child.name }}</p>
    <p>나이 : {{ child.age }}</p>
  </div>
</template>

<script setup>
defineProps({
  child: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
.child-box {
  border: 1px solid #ccc;
  padding: 16px;
  margin-bottom: 12px;
  background-color: #fff;
}
</style>
