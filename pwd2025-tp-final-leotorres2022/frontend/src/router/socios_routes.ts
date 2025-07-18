const socios_routes = [
  {
    path: '/socios',
    name: 'socios',
    component: () => import('../views/SociosView.vue'),
    children: [
      {
        path: '',
        name: 'socios_list',
        component: () => import('../components/socios/SociosList.vue'),
      },
      {
        path: ':id/update',
        name: 'socios_update',
        component: () => import('../components/socios/SociosUpdate.vue'),
      },
      {
        path: '',
        name: 'socios_create',
        component: () => import('../components/socios/SociosCreate.vue'),
      },
      {
        path: ':id/show',
        name: 'socios_show',
        component: () => import('../components/socios/SociosShow.vue'),
      },
    ],
  },
]
export default socios_routes
