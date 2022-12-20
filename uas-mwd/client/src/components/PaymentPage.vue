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
  created() {
    const post_url = "http://127.0.0.1:5000/save_invoice";
    this.emitter.on("product-list", (productList) => {
      console.log(productList);
      this.productList = productList;
    });
  },
  mounted() {},
};
</script>

<style></style>
