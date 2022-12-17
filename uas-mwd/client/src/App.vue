<template>
  <div class="d-flex justify-content-between py-3 px-5">
    <h1 class="fw-800">Point of Sales App</h1>
    <ProductNavigation />
  </div>
  <div class="my-3 p-3 d-flex flex-row">
    <LeftSidebar v-if="showSideBar" :latestInvoiceNo="latestInvoiceNo" />
    <div class="w-75 px-5">
      <router-view />
      <router-link
        @click="toggleSideBar()"
        class="btn btn-primary mt-3"
        to="/report_sales"
        v-if="showSideBar"
        >Report Sales</router-link
      >
      <router-link
        @click="toggleSideBar()"
        class="btn btn-primary mt-3"
        to="/"
        v-else
        >Go Back</router-link
      >
    </div>
  </div>
</template>

<script>
import LeftSidebar from "./components/LeftSidebar.vue";
import ProductNavigation from "./components/ProductNavigation.vue";
import axios from "axios";

export default {
  name: "App",
  components: {
    LeftSidebar,
    ProductNavigation,
  },
  data() {
    return { latestInvoiceNo: null, showSideBar: true };
  },
  methods: {
    getLatestInvoiceNo() {
      axios.get("http://127.0.0.1:5000/latest_invoice_no").then((res) => {
        if (res.data === 0) {
          this.latestInvoiceNo = 1;
        } else {
          this.latestInvoiceNo = res.data;
        }
      });
    },
    toggleSideBar() {
      this.showSideBar = !this.showSideBar;
    },
  },
  created() {
    this.getLatestInvoiceNo();
  },
};
</script>
