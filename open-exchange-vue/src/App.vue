<template>
  <router-view/>
</template>

<style>
#app {
  font: 1rem "Roboto", sans-serif;
  margin-top: 2%;
}

input[type=button] {
  border: 1px solid;
  padding: calc(.875rem - 3px) 63px calc(.875rem - 3px) 15px;
  background-color: #fff;
  font-size: 14px;
}
input[type=button]:not([disabled]):hover {
  background-color: #000;
  color: #fff;
}
</style>
