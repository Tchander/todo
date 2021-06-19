<template>
  <v-app id="app">
        <router-view />
  </v-app>
</template>

<style>
*, *:before, *:after {
  padding: 0;
  margin: 0;
  border: 0;
  box-sizing: border-box;
}
html, body {
  height: 100%;
  font-family: 'Roboto', sans-serif;
  background-color: #fff;
  color: #000;
  text-align: center;
  font-size: 16px;
  font-weight: 400;
  line-height: 30px;
  margin: 0;
}
h1, h2, h3, h4, h5, h6, p, span {
  margin: 0;
  padding: 0;
}
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
