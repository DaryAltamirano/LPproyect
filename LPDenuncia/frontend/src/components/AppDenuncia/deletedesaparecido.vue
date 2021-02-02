<template>
<div class ="container">
    <div class="row">
        <div class ="col">
        <h3>¿ Estas seguro de eliminar a este desaparecido ? </h3>
          <p>Nombre : {{this.element.Nombre}}</p>
          <p>Apellido : {{this.element.Appellido}}</p>   
        </div>
    </div>

    <div class="row">
        <div class="col">
        <b-button v-on:click="deleteDesaparecidos" variant="danger">Eliminar </b-button>
        </div>
    </div>
</div>
</template>
<script>
import axios from 'axios'
import swal from 'sweetalert'
export default {
    data(){
        return {
            desaparecidoId:this.$route.params.desaparecidoId,
            element:{
                Nombre:'',
                Appellido:''
            }
        }
    }, 
    created() {
            this.getDesaparecido();
    },
    methods:{   
            getDesaparecido(){
            const path =  `http://127.0.0.1:8000/api/v1.0/PersonaDesaparecida/${this.desaparecidoId}/`
            axios.get(path).then((response)=> {
                this.element.Nombre=response.data.Nombre
                this.element.Appellido=response.data.Appellido
            }).catch((error)=>{console.log(error)})
        },
        deleteDesaparecidos(){
            const path =  `http://127.0.0.1:8000/api/v1.0/PersonaDesaparecida/${this.desaparecidoId}/`
            axios.delete(path).then((response)=>{
            location.href='/denunciante'
            }).cath((error)=>{ swal("No es posible eliminar el desapareceido","","error")})
        }   
    }

}
</script>

<style lang="css" scoped>
</style>