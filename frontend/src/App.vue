<template>
  <div id="app">
    <NavMenu></NavMenu>
  </div>
</template>

<script>
import NavMenu from './components/NavMenu'
export default {
  components: {
    NavMenu
  },
  name: 'App',
   data() {
      return {

      };
    },
    methods: {

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
}
</style>
