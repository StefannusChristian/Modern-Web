<template>
  <div class="container">
    <h2>Report Sales</h2>
    <div v-for="invoice in invoices" :key="invoice.invoice_id">
      {{ invoice }}
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "ReportSales",
  data() {
    return {
      invoices: [],
    };
  },
  methods: {
    getInvoices() {
      const path = "http://127.0.0.1:5000/report_sales";
      axios
        .get(path)
        .then((res) => {
          this.invoices = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getInvoices();
  },
};
</script>

<style></style>