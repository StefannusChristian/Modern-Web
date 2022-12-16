<template>
  <h1 class="mb-3">Ini Component Alat Tulis</h1>
  <div class="d-flex row flex-wrap justify-content-center">
    <div
      class="card product-card px-0 mx-2 mb-3"
      v-for="alat in alat_tulis"
      :key="alat.product_id"
      :id="alat.product_id"
    >
      <img :src="alat.img_filepath" alt="" class="card-img-top img-fluid" />
      <div class="card-body">
        <h5 class="card-title">
          {{ alat.product_name }}
        </h5>
        <h6 class="card-subtitle mb-2">{{ alat.product_price }}</h6>
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
      alat_tulis: [],
    };
  },
  methods: {
    get_alat_tulis() {
      const path = "http://127.0.0.1:5000/alat_tulis";
      axios
        .get(path)
        .then((res) => {
          let alat_tulis = [];
          let rupiah = this.to_rupiah;
          res.data.forEach(function (obj) {
            obj.img_filepath = "http://127.0.0.1:5000/" + obj.img_filepath;
            obj.product_name =
              obj.product_name.charAt(0).toUpperCase() +
              obj.product_name.slice(1);
            obj.product_price = rupiah(obj.product_price);
            alat_tulis.push(obj);
          });
          this.alat_tulis = alat_tulis;
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
    this.get_alat_tulis();
  },
};
</script>

<style></style>
