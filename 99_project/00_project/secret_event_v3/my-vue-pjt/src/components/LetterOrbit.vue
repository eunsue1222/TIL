<template>
  <div class="orbit-container">
    <div
      v-for="(letter, index) in letters"
      :key="letter.id || index"
      class="letter-object"
      :style="getLetterStyle(index)"
    >
      <div v-if="index !== selectedIndex" class="letter-dot">
        <span class="letter-id">{{ letter.id }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  letters: { type: Array, required: true },
  selectedIndex: { type: Number, required: true },
});

const getLetterStyle = (index) => {
  if (index === props.selectedIndex) {
    return { transform: 'scale(0)', opacity: 0, pointerEvents: 'none' };
  }
  
  const totalItems = props.letters.length;
  let offset = index - props.selectedIndex;
  if (Math.abs(offset) > totalItems / 2) {
    offset = offset > 0 ? offset - totalItems : offset + totalItems;
  }
  
  if (Math.abs(offset) > 3) {
    return { transform: 'scale(0)', opacity: 0, pointerEvents: 'none' };
  }

  // 1. 여기서 색상을 결정합니다.
  let dotColor = '#b3e5fc'; // 기본 파랑
  if (offset === -1 || offset === -2) {
    dotColor = '#ffc0cb'; // 조건부 핑크
  }

  let angleStep = 30; 
  if (Math.abs(offset) === 1) {
    angleStep = 35; 
  }
  const angle = -90 + offset * angleStep;
  const angleInRad = angle * (Math.PI / 180);

  const radius = window.innerWidth * 0.5;
  const centerX = 0;
  const centerY = window.innerHeight + window.innerWidth * 0.2; 
  
  const x = centerX + radius * Math.cos(angleInRad);
  const y = centerY + radius * Math.sin(angleInRad);
  
  const scale = 1 - Math.abs(offset) * 0.1;
  const opacity = 1 - Math.abs(offset) * 0.15;

  return {
    transform: `translate(-50%, -50%) translate(${x}px, ${y}px) scale(${scale})`,
    zIndex: 100 - Math.abs(offset),
    opacity: opacity,
    pointerEvents: 'auto',
    '--dot-color': dotColor, // 2. 결정된 색상을 CSS 변수로 전달합니다.
  };
};
</script>

<style scoped>
.orbit-container {
  position: absolute;
  top: 0;
  left: 50%;
  width: 1px;
  height: 1px;
  pointer-events: none;
}

.letter-object {
  position: absolute;
  transition: all 0.75s cubic-bezier(0.25, 1, 0.5, 1); 
}

.letter-dot {
  width: 120px;
  height: 120px;
  background-color: var(--dot-color); /* 3. CSS 변수를 받아 배경색을 칠합니다. */
  border-radius: 50%;
  border: 3px solid white;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
  display: flex;
  justify-content: center;
  align-items: center;
  /* transform과 background-color 전환 효과를 합칩니다. */
  transition: transform 0.75s cubic-bezier(0.25, 1, 0.5, 1), background-color 0.5s ease;
}

.letter-id {
  font-size: 1.2rem;
  font-weight: bold;
  color: #01579b;
}
</style>