<template>
  <h1>Payment Succesful!</h1>
  <p>Get latest invoice detail!</p>
  {{ productList }}
  <br />
</template>

<script>
export default {
  name: "PaymentPage",
  data() {
    return {
      invoice: null,
      productList: [],
    };
  },
  methods: {},
  mounted() {
    // const post_url = "http://127.0.0.1:5000/save_invoice";
    const product_list = localStorage.getItem("product_list");
    this.productList = product_list;
  },
};
</script>

<style></style>
