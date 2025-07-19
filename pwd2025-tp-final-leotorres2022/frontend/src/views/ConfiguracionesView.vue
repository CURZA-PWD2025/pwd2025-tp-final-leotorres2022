<template>
  <div class="layout">
    <nav class="sidebar">
         <ul>

        <li><router-link :to="{name:'categorias_list'}">Categorias</router-link></li>
        <li><router-link :to="{name:'talles_list'}">Talles</router-link></li>

      </ul>
    </nav>
    <main class="content">
     <RouterView />
     <h1>En el menu lateral Podras configurar las categorias y Talles</h1>

    </main>
  </div>
</template>

<script setup lang="ts">
import useUserStore from '@/stores/user'
const userStore = useUserStore()

</script>

<style scoped>
.layout {
  display: flex;
  flex-direction: row;
  background: #fff;

}
h1 {
  text-align: center;
  margin-top: 1rem;
  color: #333;
}
/* Animación para el sidebar */
.sidebar {
  position: fixed;
  top: 0;
  left: 0;
  width: 120px;
  height: 100%;
  background: #f5f5f5;
  border-right: 1px solid #ddd;
  padding: 2rem 1rem;
  z-index: 100;
  transform: none;
  opacity: 1;
  animation: none;
}

@keyframes slideInSidebar {
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

.sidebar ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.sidebar li {
  margin: 20px 0;
  opacity: 0;
  transform: translateX(-50px);
  animation: slideInLink 0.7s cubic-bezier(.77,0,.18,1) forwards;
  font-size: 1.2rem;
}

.sidebar li:nth-child(1) { animation-delay: 0.5s; }
.sidebar li:nth-child(2) { animation-delay: 1s; }
.sidebar li:nth-child(3) { animation-delay: 1.5s; }
.sidebar li:nth-child(4) { animation-delay: 2s; }
.sidebar li:nth-child(5) { animation-delay: 2.5s; }

@keyframes slideInLink {
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.sidebar a {
  text-decoration: none;
  color: #333;
  font-weight: 600;
  transition: color 0.2s, background 0.2s, padding 0.2s;
  border-radius: 6px;
  display: block;
  margin-top: 5rem;
}

.sidebar a:hover {
  background: #e3f2fd;
  color: #1976d2;
  padding-left: 1.5rem;
}

.sidebar a.router-link-active {
  color: #1976d2;
  font-weight: bold;
  padding-left: 1.5rem;
}
.content {
  flex: 1;
  padding: 2rem;
}

</style>
