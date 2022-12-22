<template>
  <div class="d-flex row flex-wrap justify-content-center mb-5">
    <div
      class="card product-card px-0 mx-2 mb-3"
      v-for="product in products"
      :key="product.product_id"
      :id="product.product_id"
    >
      <img :src="product.img_filepath" alt="" class="card-img-top img-fluid" />
      <div class="card-body">
        <h5 class="card-title">
          {{ product.product_name }}
        </h5>
        <h6 class="card-subtitle mb-2">{{ product.product_price }}</h6>
        <button
          @click="add_product(product.product_id)"
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
  name: "Categories",
  data() {
    return {
      products: [],
      current_category_id: "1",
    };
  },
  methods: {
    get_products() {
      const path =
        "http://127.0.0.1:5000/categories/" + this.current_category_id;
      axios
        .get(path)
        .then((res) => {
          let products = [];
          let rupiah = this.to_rupiah;
          res.data.forEach(function (obj) {
            obj.img_filepath = "http://127.0.0.1:5000/" + obj.img_filepath;
            obj.product_name =
              obj.product_name.charAt(0).toUpperCase() +
              obj.product_name.slice(1);
            obj.product_price_int = obj.product_price;
            obj.product_price = rupiah(obj.product_price);
            products.push(obj);
          });
          this.products = products;
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
    add_product(product_id) {
      let product_index = this.get_product_id_index(product_id);
      let product = {
        product_id: product_id,
        product_name: this.products[product_index].product_name,
        product_price: this.products[product_index].product_price_int,
        product_qty: 1,
      };
      this.emitter.emit("add_product", product);
    },
    get_product_id_index(product_id) {
      for (let index = 0; index < this.products.length; index++) {
        if (this.products[index].product_id === product_id) {
          return index;
        }
      }
    },
  },
  created() {
    this.get_products();
    this.emitter.on("select_category", (category_id) => {
      this.current_category_id = category_id;
      this.get_products();
    });
  },
};
</script>

<style></style>
