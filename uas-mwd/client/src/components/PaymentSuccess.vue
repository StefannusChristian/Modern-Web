<template>
  <h1>Payment Succesful!</h1>
  <p>Get latest invoice detail!</p>
</template>

<script>
export default {
  name: "PaymentSuccess",
  methods: {
    getLatestInvoiceDetail() {
      console.log("Getting latest invoice detail!");
    },
  },
  created() {
    console.log("Payment succesful!");
    this.getLatestInvoiceDetail();
  },
};
</script>

<style></style>
