<template>
  <h1 class="mb-3 fw-600">Pakaian</h1>
  <div class="d-flex row flex-wrap justify-content-center">
    <div
      class="card product-card px-0 mx-2 mb-3"
      v-for="pakai in pakaian"
      :key="pakai.product_id"
      :id="pakai.product_id"
    >
      <img :src="pakai.img_filepath" alt="" class="card-img-top img-fluid" />
      <div class="card-body">
        <h5 class="card-title">
          {{ pakai.product_name }}
        </h5>
        <h6 class="card-subtitle mb-2">{{ pakai.product_price }}</h6>
        <button
          @click="add_product(pakai.product_id)"
          class="btn btn-dark d-block w-100"
        >
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
          let pakaian = [];
          let rupiah = this.to_rupiah;
          res.data.forEach(function (obj) {
            obj.img_filepath = "http://127.0.0.1:5000/" + obj.img_filepath;
            obj.product_name =
              obj.product_name.charAt(0).toUpperCase() +
              obj.product_name.slice(1);
            obj.product_price_int = obj.product_price;
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
    add_product(pakaian_id) {
      let product_index = this.get_product_id_index(pakaian_id);
      let product = {
        product_id: pakaian_id,
        product_name: this.pakaian[product_index].product_name,
        product_price: this.pakaian[product_index].product_price_int,
        product_qty: 1,
      };
      this.emitter.emit("add_product", product);
    },
    get_product_id_index(pakaian_id) {
      for (let index = 0; index < this.pakaian.length; index++) {
        if (this.pakaian[index].product_id === pakaian_id) {
          return index;
        }
      }
    },
  },
  created() {
    this.getPakaian();
  },
};
</script>

<style></style>
