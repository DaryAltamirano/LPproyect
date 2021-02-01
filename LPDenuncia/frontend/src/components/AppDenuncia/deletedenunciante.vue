<template>
<div class ="container">
    <div class="row">
        <div class ="col">
        <h3> Estas seguro de eliminar a este denunciante ? </h3>
          <p>Nombre : {{this.element.Nombre}}</p>
          <p>Apellido : {{this.element.Appellido}}</p>  
          <p>Relacion : {{this.element.Relacion}}</p>  
        </div>
    </div>

    <div class="row">
        <div class="col">
        <b-button v-on:click="deleteDenunciante" variant="danger">Eliminar </b-button>
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
            denuncianteId:this.$route.params.denuncianteId,
            element:{
                Nombre:'',
                Appellido:'',
                Relacion:''
            }
        }
    }, 
    created() {
            this.getDenunciante();
    },
    methods:{   
            getDenunciante(){
            const path =  `http://127.0.0.1:8000/api/v1.0/PersonaDenuncinate/${this.denuncianteId}/`
            axios.get(path).then((response)=> {
                this.element.Nombre=response.data.Nombre
                this.element.Appellido=response.data.Appellido
                //this.form.Telefono=response.data.Telefono
                 this.element.Relacion=response.data.Relacion
            }).catch((error)=>{console.log(error)})
        },
        deleteDenunciante(){
            const path =  `http://127.0.0.1:8000/api/v1.0/PersonaDenuncinate/${this.denuncianteId}/`
            axios.delete(path).then((response)=>{
            location.href='/denunciante'
            }).cath((error)=>{ swal("No es posible eliminar el libro","","error")})
        }   
    }

}
</script>

<style lang="css" scoped>
</style>