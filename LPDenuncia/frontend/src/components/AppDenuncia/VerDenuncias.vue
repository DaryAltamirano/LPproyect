<template lang="html">
<div class= "container">
    <div class = "row ">
        <div class= "col text-left">
            <div class="">
            <h2>
                Listado de denuncias pendientes
            </h2>
            <!-- <b-button size="sm" :to="{name:'newdenunciante'}" variant="primary">Nuevo denunciante </b-button> -->
            </div>
            <br>
            <div class="col-md-12">
                <b-table striped hover :items= "denuncias" :fields="fields">
                <template v-slot:cell(action)="data">
                    <b-button size="sm" variant="primary" :to="{name:'editdesaparecido',params:{desaparecidoId:data.item.id}}">Editar</b-button>
                    <b-button size="sm" variant="danger" :to="{name:'deletedesaparecido',params:{desaparecidoId:data.item.id}}">Eliminar</b-button>
                </template>
                </b-table>
            </div>
        </div>
    </div>
</div>
</template>
<script>

import axios from 'axios';
export default {
  data() {
      return {
           fields: [
            {key:'Nombre', label:'Nombre' },
            {key:'Appellido', label:'Apellido'},
            {key:'Telefono', label:'Telefono'},
            {key:'action', label:''},
          ],
          denuncias: [] 
      }
  },
  methods : {
      getDenunciantes () {
          const path = 'http://127.0.0.1:8000/api/v1.0/PersonaDesaparecida/'
          axios.get(path).then((response) => {
            this.denuncias= response.data
         })
          .catch((error)=>{
              console.log(error)
          })
      }
} ,
  created () {
      this.getDenunciantes()
  }
}
</script>