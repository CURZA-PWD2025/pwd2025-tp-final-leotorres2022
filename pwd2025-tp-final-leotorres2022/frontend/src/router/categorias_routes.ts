const categorias_routes = [
  {
    path: '/categorias',
    name: 'categorias',
    component: () => import('../views/CategoriasView.vue'),
    children: [
      {
        path: '',
        name: 'categorias_list',
        component: () => import('../components/categorias/CategoriasList.vue'),
      },
      {
        path: ':id/update',
        name: 'categorias_update',
        component: () => import('../components/categorias/CategoriasUpdate.vue'),
      },
      {
        path: '',
        name: 'categorias_create',
        component: () => import('../components/categorias/CategoriasCreate.vue'),
      },
      {
        path: ':id/show',
        name: 'categorias_show',
        component: () => import('../components/categorias/CategoriasShow.vue'),
      },

    ]
  }
]

export default categorias_routes
