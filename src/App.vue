<template>
  <div id="app">
    <button type="button" @click="handleClick">调用</button>
  </div>
</template>

<script>
// const { ipcRenderer } = require('electron')

export default {
  name: 'App',
  components: {
  },
  methods: {
    handleClick () {
      window.ipcRenderer.send('sendMessage', 'this is moon here')
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
