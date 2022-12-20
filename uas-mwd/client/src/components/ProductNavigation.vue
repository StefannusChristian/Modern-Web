<template>
  <ul class="nav justify-content-end">
    <li class="nav-item">
      <router-link class="nav-link text-dark" to="/">Home</router-link>
    </li>
    <li class="nav-item">
      <router-link class="nav-link text-dark" to="/alat_tulis"
        >Alat Tulis</router-link
      >
    </li>
    <li class="nav-item">
      <router-link class="nav-link text-dark" to="/pakaian"
        >Pakaian</router-link
      >
    </li>
    <li class="nav-item">
      <router-link class="nav-link text-dark" to="/makanan"
        >Makanan</router-link
      >
    </li>
    <li class="nav-item">
      <a href="#" class="nav-link text-dark" @click="logout">
        Logout <i class="bi bi-box-arrow-right ms-2"></i
      ></a>
    </li>
  </ul>
</template>

<script>
export default {
  name: "ProductNavigation",
  methods: {
    logout() {
      sessionStorage.clear();
      this.emitter.emit("logged-out");
      this.$router.push("/");
    },
  },
};
</script>

<style></style>
