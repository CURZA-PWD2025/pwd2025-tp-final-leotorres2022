import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import tienda_routes from './tienda_routes'
import categorias_routes from './categorias_routes'
import ConfiguracionesView from '@/views/ConfiguracionesView.vue'
import ClubView from '@/views/ClubView.vue'
import socios_routes from './socios_routes'
import galeria_routes from './galeria_routes'
import talles_routes from './talles_routes'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    ...tienda_routes,
    ...categorias_routes,
    ...socios_routes,
    ...galeria_routes,
    ...talles_routes,
    { path: '/configuraciones', name: 'configuraciones', component: ConfiguracionesView },
    { path: '/club', name: 'club', component: ClubView },
  ],
})

export default router
