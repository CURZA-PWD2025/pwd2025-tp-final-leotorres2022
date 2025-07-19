const compras_routes = [
  {
    path: '/compras',
    name: 'compras',
    component: () => import('../views/ComprasView.vue'),
    children: [
      {
        path: '',
        name: 'compras_list',
        component: () => import('../components/compras/ComprasList.vue'),
      },
      {
        path: ':id/update',
        name: 'compras_update',
        component: () => import('../components/compras/ComprasUpdate.vue'),
      },
      {
        path: 'create',
        name: 'compras_create',
        component: () => import('../components/compras/ComprasCreate.vue'),
      },
      {
        path: ':id/show',
        name: 'compras_show',
        component: () => import('../components/compras/ComprasShow.vue'),
      },

    ]
  }
]
export default compras_routes
