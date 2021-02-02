<template lang="html">
<div class= "container">
    <div class = "row ">
        <div class= "col text-left">
            <h2>
                Editar informacion desaparecido
            </h2>
        </div>
    </div>
    <div class ="row">
        <div class ="col">
            <div class ="card">
                <div class ="card-body">
                    <form @submit.prevent="subir">
                    <div class ="form-group row">
                        <label for="Nombre" class="col-sm-2 col-form-label">Nombre</label> 
                        <div class="col-sm-6">
                            <input type="text" placeholder="Nombre" name="Nombre" class="form-control" v-model.trim="form.Nombre">
                        </div>
                    </div>
                    <div class ="form-group row">
                        <label for="Apellido" class="col-sm-2 col-form-label">Apellido</label> 
                        <div class="col-sm-6">
                            <input type="text" placeholder="Appellido" name="Appellido" class="form-control"v-model.trim="form.Appellido">
                        </div>
                    </div>
                    <div class ="form-group row">
                        <label for="Telefono" class="col-sm-2 col-form-label">Telefono</label> 
                        <div class="col-sm-6">
                            <input type="number" placeholder="Telefono" name="Telefono" class="form-control" v-model.trim="form.Telefono">
                        </div>
                    </div>
                    <div class ="form-group row">
                        <label for="Edad" class="col-sm-2 col-form-label">Edad</label> 
                        <div class="col-sm-6">
                            <input type="number" placeholder="Edad" name="Edad" class="form-control" v-model.trim="form.Edad">
                        </div>
                    </div>
                    <div class ="form-group row">
                        <label for="TonoDePiel" class="col-sm-2 col-form-label">Tono De Piel</label> 
                        <div class="col-sm-6">
                            <input type="text" placeholder="TonoDePiel" name="TonoDePiel" class="form-control" v-model.trim="form.TonoDePiel">
                        </div>
                    </div>
                    <div class ="form-group row">
                        <label for="ColorOjos" class="col-sm-2 col-form-label">Color de Ojos</label> 
                        <div class="col-sm-6">
                            <input type="text" placeholder="ColorOjos" name="ColorOjos" class="form-control" v-model.trim="form.ColorOjos">
                        </div>
                    </div>
                    <div class ="form-group row">
                        <label for="Estatura" class="col-sm-2 col-form-label">Estatura</label> 
                        <div class="col-sm-6">
                            <input type="number " step="any" placeholder="Estatura" name="Estatura" class="form-control" v-model.trim="form.Estatura">
                        </div>
                    </div>
                    <div class="row">
                        <div class="col text-left">
                            <b-button type="submit" size="sm" variant="primary" class="btn-large-space">Editar</b-button>
                            <b-button size="sm" variant="" class="btn-large-space" :to="{name:'desaparecido'}">Cancelar</b-button>
                        </div>   
                    </div>
                    </form>
                 </div>
            </div>
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
        denunciaId:this.$route.params.desaparecidoId,
        form: {
        Nombre:'',
        Appellido:'',
        Telefono:0,
        TonoDePiel:'',
        Edad:0,
        ColorOjos:'',
        Estatura:0.0,
        PersonaDesaparecida:[],
        }
       }
    },
        created() {
            this.getDesaparecidos();
        },
     methods: {
        subir(){
             const path = `http://127.0.0.1:8000/api/v1.0/PersonaDesaparecida/${this.denunciaId}/`
             axios.put(path,this.form).then((response)=> {
                this.form.Nombre=response.data.Nombre
                this.form.Appellido=response.data.Appellido
                this.form.Telefono=response.data.Telefono
                this.form.TonoDePiel=response.data.TonoDePiel
                this.form.ColorOjos=response.data.ColorOjos
                this.form.Edad=response.data.Edad
                this.form.Estatura=response.data.Estatura
               swal("Se actualizo correctamente los datos del desaparecido","","error")
            }).catch((error)=>{
                console.error(error)
                swal("No se pudo editar los datos del desaparecido","","error")
            })
        },
        getDesaparecidos(){
            const path =  `http://127.0.0.1:8000/api/v1.0/PersonaDesaparecida/${this.denunciaId}/`
            axios.get(path).then((response)=> {
                this.form.Nombre=response.data.Nombre
                this.form.Appellido=response.data.Appellido
                this.form.Telefono=response.data.Telefono
                this.form.TonoDePiel=response.data.TonoDePiel
                this.form.ColorOjos=response.data.ColorOjos
                this.form.Edad=response.data.Edad
                this.form.Estatura=response.data.Estatura
                this.form.PersonaDesaparecida=response.data.PersonaDesaparecida
            }).catch((error)=>{swal("No se pudo traer los datos del desaparecido","","error")})
        }
    }
}
</script>