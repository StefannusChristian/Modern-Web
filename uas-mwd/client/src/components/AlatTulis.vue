<template>
  <h1 class="mb-3">Ini Component Alat Tulis</h1>
  <div class="d-flex row flex-wrap justify-content-center">
    <div
      class="card product-card mx-2"
      v-for="alat in alat_tulis"
      :key="alat.product_id"
      :id="alat.product_id"
    >
      <div class="card-body">
        <h5 class="card-title">
          {{ alat.product_name }}
        </h5>
        <h6 class="card-subtitle mb-2">IDR {{ alat.product_price }}</h6>
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
  name: "AlatTulis",
  data() {
    return {
      alat_tulis: null,
    };
  },
  methods: {
    get_alat_tulis() {
      const path = "http://127.0.0.1:5000/alat_tulis";
      axios
        .get(path)
        .then((res) => {
          this.alat_tulis = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.get_alat_tulis();
  },
};
</script>

<style></style>
