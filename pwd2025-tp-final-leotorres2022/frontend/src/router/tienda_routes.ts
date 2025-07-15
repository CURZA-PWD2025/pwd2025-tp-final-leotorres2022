const tienda_routes = [
  {
    path: '/tienda',
    name: 'tienda',
    component: () => import('../views/TiendaView.vue') 
   }
]

export default tienda_routes
