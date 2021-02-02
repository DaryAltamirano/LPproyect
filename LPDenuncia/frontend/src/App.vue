<template>
  <div id="app">
    <barnav/>
    <img src="./assets/logo.png">
    <router-view/>
  </div>
</template>


<script>
import Barnav from '@/components/AppDenuncia/Barnav'
export default {
  name: 'App',
  components:{
    Barnav
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
</style>
