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
    <li class="nav-item">
      <a href="#" class="nav-link">
        Logout <i class="bi bi-box-arrow-right ms-2"></i
      ></a>
    </li>
  </ul>
</template>

<script>
export default {
  name: "ProductNavigation",
};
</script>

<style></style>
