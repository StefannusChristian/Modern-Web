<template>
  <h1>Ini App Vue</h1>
  <a href="/">Home</a>
  <br /><br />
  <router-link :to="{ path: 'pakaian' }">Pakaian</router-link>
  <br /><br />
  <router-link :to="{ path: 'makanan' }">Makanan</router-link>
  <br /><br />
  <router-link :to="{ path: 'alat_tulis' }">Alat Tulis</router-link>
  <br /><br />
  <router-view />
</template>
