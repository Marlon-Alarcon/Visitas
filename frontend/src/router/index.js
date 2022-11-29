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
    path: '/Edit/:id',
    name: 'Edit',
    component: () => import('../components/edit/EditarPersona.vue')
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
    path: '/editV/:id',
    name: 'edit',
    component: () => import(/* webpackChunkName: "about" */ '../components/edit/EditarVisitante.vue')
  },
  {
    path: '/visita',
    name: 'visita',
    component: () => import(/* webpackChunkName: "about" */ '../views/VisitasView.vue')
  },
  {
    path: '/editVisita/:id',
    name: 'edita',
    component: () => import(/* webpackChunkName: "about" */ '../components/edit/EditarVisitas.vue')
  },
  {
    path: '/maestra',
    name: 'maestra',
    component: () => import(/* webpackChunkName: "about" */ '../views/MaestraView.vue')
  },
  {
    path: '/actualizando',
    name: 'actualizando',
    component: () => import(/* webpackChunkName: "about" */ '../views/Disparador/actualizando.vue')
  },
  {
    path: '/consulta',
    name: 'consulta',
    component: () => import(/* webpackChunkName: "about" */ '../views/Consultas/Consulta.vue')
  },
  {
    path: '/consulta2',
    name: 'consulta2',
    component: () => import(/* webpackChunkName: "about" */ '../views/Consultas/Consulta2.vue')
  },
  {
    path: '/consulta3',
    name: 'consulta3',
    component: () => import(/* webpackChunkName: "about" */ '../views/Consultas/Consulta3.vue')
  },
  {
    path: '/consulta4',
    name: 'consulta4',
    component: () => import(/* webpackChunkName: "about" */ '../views/Consultas/Consulta4.vue')
  },
  {
    path: '/muestra',
    name: 'muestra',
    component: () => import(/* webpackChunkName: "about" */ '../views/Consultas/Muestra.vue')
  },

  
]

const router = createRouter({
  history: createWebHistory(),
  routes
})
export default router
