<template>
  <h1 class="mb-3">Ini Component Makanan</h1>
  <div class="d-flex row flex-wrap justify-content-center">
    <div
      class="card product-card px-0 mx-2 mb-3"
      v-for="makan in makanan"
      :key="makan.product_id"
      :id="makan.product_id"
    >
      <img :src="makan.img_filepath" alt="" class="card-img-top img-fluid" />
      <div class="card-body">
        <h5 class="card-title">
          {{ makan.product_name }}
        </h5>
        <h6 class="card-subtitle mb-2">{{ makan.product_price }}</h6>
        <button
          @click="add_product(makan.product_id)"
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
          let rupiah = this.to_rupiah;
          res.data.forEach(function (obj) {
            obj.img_filepath = "http://127.0.0.1:5000/" + obj.img_filepath;
            obj.product_name =
              obj.product_name.charAt(0).toUpperCase() +
              obj.product_name.slice(1);
            obj.product_price_int = obj.product_price;
            obj.product_price = rupiah(obj.product_price);
            makanan.push(obj);
          });
          this.makanan = makanan;
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
    add_product(makanan_id) {
      let product_index = this.get_product_id_index(makanan_id);
      let product = {
        product_id: makanan_id,
        product_name: this.makanan[product_index].product_name,
        product_price: this.makanan[product_index].product_price_int,
        product_qty: 1,
      };
      this.emitter.emit("add_product", product);
    },
    get_product_id_index(makanan_id) {
      for (let index = 0; index < this.makanan.length; index++) {
        if (this.makanan[index].product_id === makanan_id) {
          return index;
        }
      }
    },
  },
  created() {
    this.getMakanan();
  },
};
</script>

<style></style>
