import Vue from 'vue'
import Router from 'vue-router'
// IMPORTACIONES DE LOS DENUNCIANTE
import denunciante from '@/components/AppDenuncia/denunciante'
import editdenunciante from '@/components/AppDenuncia/editdenunciante' 
import deletedenunciante from '@/components/AppDenuncia/deletedenunciante'
import newdenunciante from '@/components/AppDenuncia/newdenunciante'
//IMPORTACIONES DE LOS DESAPARECIDOS
import desaparecido from '@/components/AppDenuncia/desaparecido'
import editdesaparecido from '@/components/AppDenuncia/editdesaparecido' 
import deletedesaparecido from '@/components/AppDenuncia/deletedesaparecido'
import newdesaparecido from '@/components/AppDenuncia/newdesaparecido'
import verDenuncias from '@/components/AppDenuncia/verDenuncias'
//GENERAL

import Home from '@/components/AppDenuncia/Home'
Vue.use(Router)
export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },{
      path: '/denunciante',
      name: 'denunciante',
      component: denunciante 
    },{
      path: '/denunciante/:denuncianteId/edit/',
      name: 'editdenunciante',
      component: editdenunciante 
    },{
      path: '/denunciante/:denuncianteId/eliminar',
      name: 'deletedenunciante',
      component: deletedenunciante
    },{
      path: '/denunciante/crear',
      name: 'newdenunciante',
      component: newdenunciante
    },{
      path: '/desaparecido',
      name: 'desaparecido',
      component: desaparecido
    },{
      path: '/desaparecido/:denuncianteId/verDenuncias/:desaparecidoId/editar',
      name: 'editdesaparecido',
      component: editdesaparecido
    },{
      path: '/desaparecido/:denuncianteId/verDenuncias/:desaparecidoId/eliminar',
      name: 'deletedesaparecido',
      component: deletedesaparecido
    },{
      path: '/desaparecido/:denuncianteId/crear',
      name: 'newdesaparecido',
      component: newdesaparecido
    },{
      path: '/desaparecido/:denuncianteId/verDenuncias',
      name: 'verDenuncias',
      component: verDenuncias
    }
  ],
  mode : 'history'
})
