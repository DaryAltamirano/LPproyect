<template lang="html">
<div class= "container">
    <div class = "row ">
        <div class= "col text-left">
            <div class="">
            <h2>
                Listado de denunciantes
            </h2>
            
            <b-button size="sm" :to="{name:'newdenunciante'}" variant="primary">Nuevo denunciante </b-button>
            </div>
            <br>
            <div class="col-md-12">
                <b-table striped hover :items= "denunciantes" :fields="fields">
                <template v-slot:cell(action)="data">
                    <b-button size="sm" variant="success" :to="{name:'newdesaparecido',params:{denuncianteId:data.item.id}}">Denunciar</b-button>
                    <b-button size="sm" variant="primary" :to="{name:'editdenunciante',params:{denuncianteId:data.item.id}}">Editar</b-button>
                    <b-button size="sm" variant="danger" :to="{name:'deletedenunciante',params:{denuncianteId:data.item.id}}">Eliminar</b-button>
                    <b-button size="sm" variant="" :to="{name:'verDenuncias',params:{denuncianteId:data.item.id}}">Denuncias pendientes</b-button>
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
            {key:'Relacion', label:'Relacion'},
            {key:'Action', label:''},
          ],
          denunciantes: [] 
      }
  },
  methods : {
      getDenunciantes () {
          const path = 'http://127.0.0.1:8000/api/v1.0/PersonaDenuncinate/'
          axios.get(path).then((response) => {
            this.denunciantes= response.data
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