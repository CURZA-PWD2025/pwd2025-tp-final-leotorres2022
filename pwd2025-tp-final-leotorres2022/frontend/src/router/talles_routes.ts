const talles_routes = [
  {
    path: '/talles',
    name: 'talles',
    component: () => import('../views/TallesView.vue'),
    children: [
      {
        path: '',
        name: 'talles_list',
        component: () => import('../components/talles/TallesList.vue'),
      },
      {
        path: ':id/update',
        name: 'talles_update',
        component: () => import('../components/talles/TallesUpdate.vue'),
      },
      {
        path: '',
        name: 'talles_create',
        component: () => import('../components/talles/TallesCreate.vue'),
      },
      {
        path: ':id/show',
        name: 'talles_show',
        component: () => import('../components/talles/TallesShow.vue'),
      },
    ],
  },
]

export default talles_routes
