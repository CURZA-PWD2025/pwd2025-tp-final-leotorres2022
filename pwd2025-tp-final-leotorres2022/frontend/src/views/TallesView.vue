<template>

<RouterView />
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
import { onMounted } from 'vue';

const route = useRouter();

onMounted(() => {
  route.push({ name: 'talles_list' });
});

</script>

<style scoped>

</style>
