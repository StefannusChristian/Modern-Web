<template>
  <div
    class="d-flex justify-content-between py-3 px-5"
    v-if="loggedIn && showSideBar"
  >
    <h1 class="fw-800">Point of Sales App</h1>
    <ProductNavigation />
  </div>
  <div class="my-3 p-3 d-flex flex-row" v-if="loggedIn">
    <LeftSidebar v-if="showSideBar" :latestInvoiceNo="latestInvoiceNo" />
    <div :class="[!showSideBar ? 'w-100' : 'w-75', 'px-5']">
      <router-view />
      <router-link
        @click="toggleSideBar()"
        class="btn btn-primary mt-3 fixed-bottom rounded-0 fs-3"
        to="/report_sales"
        v-if="showSideBar"
        ><i class="bi bi-clipboard-data-fill me-2"></i>Report Sales</router-link
      >
      <router-link
        @click="toggleSideBar()"
        class="btn btn-primary mt-3 fixed-bottom rounded-0 fs-3"
        to="/"
        v-else
        ><i class="bi bi-arrow-left me-2"></i>Go Back</router-link
      >
    </div>
  </div>
  <Login v-else @login-detected="toggleLoggedInFlag" />
</template>

<script>
import LeftSidebar from "./components/LeftSidebar.vue";
import ProductNavigation from "./components/ProductNavigation.vue";
import axios from "axios";
import Login from "./components/Login.vue";

export default {
  name: "App",
  components: {
    LeftSidebar,
    ProductNavigation,
    Login,
  },
  data() {
    return {
      latestInvoiceNo: null,
      showSideBar: true,
      loggedIn: false,
    };
  },
  methods: {
    getLatestInvoiceNo() {
      axios.get("http://127.0.0.1:5000/latest_invoice_no").then((res) => {
        this.latestInvoiceNo = res.data.invoice_no + 1;
      });
    },
    toggleSideBar() {
      this.showSideBar = !this.showSideBar;
      this.checkout = !this.checkout;
    },
    toggleLoggedInFlag() {
      if (sessionStorage.getItem("currentLoggedIn") !== null) {
        this.loggedIn = true;
      } else {
        this.loggedIn = !this.loggedIn;
      }
    },
  },
  created() {
    this.getLatestInvoiceNo();
  },
  mounted() {
    if (sessionStorage.getItem("currentLoggedIn") !== null) {
      this.loggedIn = true;
    }
    this.emitter.on("logged-out", () => {
      sessionStorage.clear();
      this.toggleLoggedInFlag();
    });
    this.emitter.on("get-new-invoice-no", () => {
      this.getLatestInvoiceNo();
    });
    this.emitter.on("checkout", () => {
      this.checkout = !this.checkout;
      this.showSideBar = !this.showSideBar;
    });
    this.emitter.on("payment-good", () => {
      this.checkout = !this.checkout;
      this.showSideBar = !this.showSideBar;
    });
    this.emitter.on("disable_side_bar", () => {
      this.showSideBar = false;
    });
  },
};
</script>
