<template>
  <h1 class="mb-3">Ini Component Pakaian</h1>
  <div class="d-flex row flex-wrap justify-content-center">
    <div
      class="card product-card mx-2"
      v-for="pakai in pakaian"
      :key="pakai.product_id"
      :id="pakai.product_id"
    >
      <div class="card-body">
        <h5 class="card-title">
          {{ pakai.product_name }}
        </h5>
        <h6 class="card-subtitle mb-2">IDR {{ pakai.product_price }}</h6>
        <button class="btn btn-dark d-block w-100">
          <i class="bi bi-cart-plus-fill me-2"></i>Add Product
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Pakaian",
  data() {
    return {
      pakaian: null,
    };
  },
  methods: {
    getPakaian() {
      const path = "http://127.0.0.1:5000/pakaian";
      axios
        .get(path)
        .then((res) => {
          this.pakaian = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getPakaian();
  },
};
</script>

<style></style>
