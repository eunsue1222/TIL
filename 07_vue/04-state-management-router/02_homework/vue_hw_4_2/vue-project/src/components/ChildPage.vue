<template>
  <div class="child">
    <h4>자식 페이지</h4>
    <p>{{ child.name }}</p>
  </div>
</template>

<script setup>
defineProps({
  child: Object
});
</script>

<style scoped>
.child {
  border: 1px solid #ddd;
  padding: 15px;
  background-color: white;
  text-align: center;
  border-radius: 0; /* 모서리 각지게 */
}
</style>
