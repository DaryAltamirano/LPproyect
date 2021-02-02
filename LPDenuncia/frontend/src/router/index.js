import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import denunciante from '@/components/AppDenuncia/denunciante'
import editdenunciante from '@/components/AppDenuncia/editdenunciante' 
import deletedenunciante from '@/components/AppDenuncia/deletedenunciante'
import newdenunciante from '@/components/AppDenuncia/newdenunciante'
import Home from '@/components/AppDenuncia/Home'
import desaparecido from '@/components/AppDenuncia/desaparecido'
import editdesaparecido from '@/components/AppDenuncia/editdenunciante'
import deletedesaparecido from '@/components/AppDenuncia/deletedesaparecido'
import newdesaparecido from '@/components/AppDenuncia/newdesaparecido'
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
      name: 'Editardenunciante',
      component: editdenunciante 
    },{
      path: '/denunciante/:denuncianteId/eliminar',
      name: 'deledenunciante',
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
      path: '/desaparecido/:desaparecidoId/edit/',
      name: 'editdesaparecido',
      component: editdesaparecido
    },{
      path: '/desaparecido/:desaparecidoId/eliminar',
      name: 'deletedesaparecido',
      component: deletedesaparecido
    },{
      path: '/desaparecido/crear',
      name: 'newdesaparecido',
      component: newdesaparecido
    },
  ],
  mode : 'history'
})
