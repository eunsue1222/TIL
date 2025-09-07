<template>
  <div class="parent">
    <h3>부모 컴포넌트</h3>
    <p>{{ family.father }}</p>
    <p>{{ family.mother }}</p>

    <div
      v-for="(child, index) in family.children"
      :key="index"
      class="child-box"
    >
      <ChildPage :child="child" />
    </div>
  </div>
</template>

<script setup>
import ChildPage from './ChildPage.vue';

defineProps({
  family: Object
});
</script>

<style scoped>
.parent {
  background-color: #f9f9f9;
  padding: 30px 20px; /* 좌우 여백 조금 */
  margin: 10px 0;
  width: 100%; /* 가로 100% */
  text-align: center;
  border: 1px solid #ccc;
  border-radius: 0;
  box-sizing: border-box;
}

.child-box {
  margin-top: 20px;
}
</style>


