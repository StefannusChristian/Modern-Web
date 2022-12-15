<template>
  <h1 class="mb-3">Ini Component Pakaian</h1>
  <div class="d-flex row flex-wrap justify-content-center">
    <div
      class="card product-card mx-2"
      v-for="pakai in pakaian"
      :key="pakai.product_id"
      :id="pakai.product_id"
    >
      <img :src="pakai.img_filepath" alt="" class="card-img-top" />
      <div class="card-body">
        <h5 class="card-title">
          {{ pakai.product_name }}
        </h5>
        <h6 class="card-subtitle mb-2">{{ pakai.product_price }}</h6>
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
      pakaian: [],
    };
  },
  methods: {
    getPakaian() {
      const path = "http://127.0.0.1:5000/pakaian";
      axios
        .get(path)
        .then((res) => {
          let pakaian = [];
          let rupiah = this.to_rupiah;
          res.data.forEach(function (obj) {
            obj.img_filepath = "http://127.0.0.1:5000/" + obj.img_filepath;
            obj.product_name =
              obj.product_name.charAt(0).toUpperCase() +
              obj.product_name.slice(1);
            obj.product_price = rupiah(obj.product_price);
            pakaian.push(obj);
          });
          this.pakaian = pakaian;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    to_rupiah(num) {
      return new Intl.NumberFormat("id-ID", {
        style: "currency",
        currency: "IDR",
      })
        .format(num)
        .slice(0, -3);
    },
  },
  created() {
    this.getPakaian();
  },
};
</script>

<style></style>
