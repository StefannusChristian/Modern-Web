<template>
  <h1 class="mb-3 fw-700">Checkout Page</h1>
  <div class="bg-light rounded-2 container py-3 mb-3">
    <table class="table table-striped rounded-2 mb-3">
      <thead>
        <tr>
          <th>Product Name</th>
          <th>Price</th>
          <th>Qty.</th>
          <th>Amount</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in productList" :key="product.product_id">
          <td>{{ product.product_name }}</td>
          <td>{{ product.product_price }}</td>
          <td>{{ product.product_qty }}</td>
          <td>{{ product.product_price * product.product_qty }}</td>
        </tr>
        <tr>
          <td>{{ diskon }}</td>
          <td>{{ price_after_discount }}</td>
        </tr>
        <tr>
          <td></td>
          <td></td>
          <td class="fw-600">Subtotal</td>
          <td class="fw-600">{{ getSubtotal }}</td>
        </tr>
      </tbody>
    </table>
    <button class="btn btn-success w-100 text-center" @click="confirmPayment()">
      Confirm Payment
    </button>
  </div>
  <br />
</template>

<script>
import axios from "axios";

export default {
  name: "PaymentPage",
  data() {
    return {
      productList: [],
      subtotal: 0,
      diskon: 0,
      price_after_discount: 0,
    };
  },
  methods: {
    confirmPayment() {
      const post_url = "http://127.0.0.1:5000/save_invoice";
      let new_product_list = {
        product_list: this.productList,
        diskon: this.diskon,
        price_after_diskon: this.price_after_discount,
        user_name: sessionStorage.getItem("currentLoggedIn"),
      };
      if (this.productList.length > 0) {
        axios
          .post(post_url, JSON.stringify(new_product_list), {
            headers: {
              "Content-Type": "application/json",
            },
          })
          .then((response) => console.log(response))
          .catch((error) => console.log(error));
        this.productList = [];
        this.subtotal = 0;
        this.$router.push("/");
        this.emitter.emit("payment-good");
      }
    },
  },
  computed: {
    getSubtotal() {
      let productList = JSON.parse(localStorage.getItem("product_list"));
      for (let index = 0; index < productList.length; index++) {
        let qty = productList[index].product_qty;
        let price = productList[index].product_price;
        let total_price = qty * price;
        this.subtotal += total_price;
      }
      return this.subtotal;
    },
  },
  mounted() {
    const product_list = JSON.parse(localStorage.getItem("product_list"));
    this.productList = product_list;
    this.diskon = JSON.parse(this.$route.query.diskon);
    this.price_after_discount = JSON.parse(this.$route.query.final_price);
  },
};
</script>

<style></style>
