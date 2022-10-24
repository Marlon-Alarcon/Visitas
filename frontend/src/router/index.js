import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/persona',
    name: 'persona',
    component: () => import('../views/PersonaView.vue')
  },
  {
    path: '/edit/:id',
    name: 'edit',
    component: () => import('../components/edit/Edit.vue')
  },
  {
    path: '/estudiante',
    name: 'estudiante',
    component: () => import(/* webpackChunkName: "about" */ '../views/EstudianteView.vue')
  },
  {
    path: '/editar/:id',
    name: 'editar',
    component: () => import('../components/edit/EditarEstudiante.vue')
  },
  {
    path: '/visitante',
    name: 'visitante',
    component: () => import(/* webpackChunkName: "about" */ '../views/VisitanteView.vue')
  },
  {
    path: '/visita',
    name: 'visita',
    component: () => import(/* webpackChunkName: "about" */ '../views/VisitasView.vue')
  },
  {
    path: '/maestra',
    name: 'maestra',
    component: () => import(/* webpackChunkName: "about" */ '../views/MaestraView.vue')
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})
export default router
