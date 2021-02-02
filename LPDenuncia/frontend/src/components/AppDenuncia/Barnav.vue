<template>
<nav class="navbar navbar-expand-lg navbar-light bg-info">
   <b-button class="btn btn-info text-dark" :to="{name:'Home'}">Inicio</b-button>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
    <ul class="navbar-nav mr-auto mt-2 mt-lg-0">    
      <li class="nav-item active">
        <b-button class="btn btn-info text-dark" :to="{name:'denunciante'}">Denunciante</b-button>
      </li>
      <li class="nav-item active">
        <a class="nav-link text-dark" href="#">Aparicion</a>
      </li>
      <li class="nav-item active ">
       <b-button class="btn btn-info text-dark" :to="{name:'desaparecido'}">Desaparecido</b-button>
      </li>
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="Buscar" placeholder="Buscar">
      <button class="btn btn-success my-2 my-sm-0" type="submit">Buscar </button>
    </form>
  </div>
</nav>
</template>
<script>
export default {
    data(){
        return {

        }
    }
}
</script>