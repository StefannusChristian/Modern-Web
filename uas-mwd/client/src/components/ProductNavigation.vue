<template>
  <ul class="nav justify-content-end">
    <li class="nav-item">
      <router-link class="nav-link" to="/">Home</router-link>
    </li>
    <li class="nav-item">
      <router-link class="nav-link" to="/alat_tulis">Alat Tulis</router-link>
    </li>
    <li class="nav-item">
      <router-link class="nav-link" to="/pakaian">Pakaian</router-link>
    </li>
    <li class="nav-item">
      <router-link class="nav-link" to="/makanan">Makanan</router-link>
    </li>
  </ul>
</template>

<script>
export default {
  name: "ProductNavigation",
};
</script>

<style></style>
