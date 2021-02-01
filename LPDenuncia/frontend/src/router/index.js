import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import denunciante from '@/components/AppDenuncia/denunciante'
import editdenunciante from '@/components/AppDenuncia/editdenunciante' 
import deletedenunciante from '@/components/AppDenuncia/deletedenunciante'
import newdenunciante from '@/components/AppDenuncia/newdenunciante'
Vue.use(Router)
export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
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
    },
  ],
  mode : 'history'
})
