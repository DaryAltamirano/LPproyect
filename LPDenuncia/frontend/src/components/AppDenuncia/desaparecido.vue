<template lang="html">
<div class= "container">
    <div class = "row ">
        <div class= "col text-left">
            <div class="">
            <h2>
                Listado de desaparecidos
            </h2>
            </div>
            <br>
            <div class="col-md-12">
                <b-table striped hover :items= "desaparecidos" :fields="fields">
                <template v-slot:cell(action)="data">
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
          desaparecidos: [] 
      }
  },
  methods : {
      getDesaparecidos () {
          const path = 'http://127.0.0.1:8000/api/v1.0/PersonaDesaparecida/'
          axios.get(path).then((response) => {
            this.desaparecidos= response.data
         })
          .catch((error)=>{
              console.log(error)
          })
      }
} ,
  created () {
      this.getDesaparecidos()
  }
}
</script>