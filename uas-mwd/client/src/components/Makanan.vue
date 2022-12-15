<template>
  <h1 class="mb-3">Ini Component Makanan</h1>
  <div class="d-flex row flex-wrap justify-content-center">
    <div
      class="card product-card mx-2"
      v-for="makan in makanan"
      :key="makan.product_id"
      :id="makan.product_id"
    >
      <img :src="makan.img_filepath" alt="" class="card-img-top" />
      <div class="card-body">
        <h5 class="card-title">
          {{ makan.product_name }}
        </h5>
        <h6 class="card-subtitle mb-2">IDR {{ makan.product_price }}</h6>
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
  name: "Makanan",
  data() {
    return {
      makanan: [],
    };
  },

  methods: {
    getMakanan() {
      const path = "http://127.0.0.1:5000/makanan";
      axios
        .get(path)
        .then((res) => {
          let makanan = [];
          res.data.forEach(function (obj) {
            obj.img_filepath = "http://127.0.0.1:5000/" + obj.img_filepath;
            obj.product_name =
              obj.product_name.charAt(0).toUpperCase() +
              obj.product_name.slice(1);
            makanan.push(obj);
          });
          this.makanan = makanan;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMakanan();
  },
};
</script>

<style></style>
