<template>
  <div class="d-flex justify-content-between py-3 px-5">
    <h1>Ini App Vue</h1>
    <ProductNavigation />
  </div>
  <div class="my-3 p-3 d-flex flex-row">
    <LeftSidebar />
    <div class="w-75 px-5">
      <router-view />
      <button class="btn btn-primary mt-3">Report Sales</button>
    </div>
  </div>
</template>

<script>
import LeftSidebar from "./components/LeftSidebar.vue";
import ProductNavigation from "./components/ProductNavigation.vue";

export default {
  name: "App",
  components: {
    LeftSidebar,
    ProductNavigation,
  },
};
</script>
