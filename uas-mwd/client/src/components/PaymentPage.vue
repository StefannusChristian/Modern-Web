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
    };
  },
  methods: {
    confirmPayment() {
      const post_url = "http://127.0.0.1:5000/save_invoice";
      if (this.productList.length > 0) {
        axios
          .post(post_url, JSON.stringify(this.productList), {
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
      for (let i = 0; i < this.productList.length; i++) {
        let amount =
          this.productList[i].product_price * this.productList[i].product_qty;
        this.subtotal += amount;
      }
    },
  },
  mounted() {
    const product_list = JSON.parse(localStorage.getItem("product_list"));
    this.productList = product_list;
  },
};
</script>

<style></style>
