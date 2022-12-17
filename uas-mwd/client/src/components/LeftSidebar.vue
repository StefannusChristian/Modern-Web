<template>
  <div class="container w-25">
    <div class="p-3 bg-light">
      <div class="mb-3">
        <div class="bg-white p-3 rounded-3">
          <span class="fs-6 text-muted d-block">Admin</span>
          <span class="fw-600 fs-5">John Doe</span>
        </div>
      </div>
      <div class="mb-3 px-1">
        <h5 class="fw-700">Invoice</h5>
        <div class="d-flex justify-content-between align-items-center">
          <small class="d-block text-muted">Date</small
          ><span class="d-block fw-500">{{ currentDate }}</span>
        </div>
        <div class="d-flex justify-content-between align-items-center mb-3">
          <small class="d-block text-muted">Invoice No.</small
          ><span class="d-block fw-500">{{ latestInvoiceNo }}</span>
        </div>
        <ul
          v-for="item in product_list"
          class="list-group"
          :key="item.product_id"
        >
          <li class="list-group-item mb-1">
            <div class="d-flex justify-content-between align-items-center">
              <div class="fw-400">{{ item.product_name }}</div>
              <div class="fw-400">x{{ item.product_qty }}</div>
            </div>
            <span class="fw-400">
              {{
                new Intl.NumberFormat("id-ID", {
                  style: "currency",
                  currency: "IDR",
                })
                  .format(item.product_price * item.product_qty)
                  .slice(0, -3)
              }}
            </span>
          </li>
        </ul>
      </div>
      <h5 class="mb-3">
        <span class="fw- fs-6 mb-2 fw-500">Total</span><br />
        <span class="fw-600">
          {{
            new Intl.NumberFormat("id-ID", {
              style: "currency",
              currency: "IDR",
            })
              .format(total_invoice)
              .slice(0, -3)
          }}
        </span>
      </h5>
      <button
        class="btn btn-success d-block w-100 mb-1 text-start"
        @click="saveInvoice"
      >
        <i class="bi bi-credit-card-2-back-fill me-2"></i> Pay
      </button>
      <button @click="cancel" class="btn btn-danger d-block w-100 text-start">
        <i class="bi bi-x-square-fill me-2"></i>Cancel
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "LeftSidebar",
  data() {
    return {
      product_list: [],
      currentDate: this.formatDate(),
    };
  },
  props: {
    latestInvoiceNo: Number,
  },
  methods: {
    add_product(item) {
      let item_not_yet_added = true;
      for (let index = 0; index < this.product_list.length; index++) {
        if (this.product_list[index].product_id === item.product_id) {
          this.product_list[index].product_qty++;
          item_not_yet_added = false;
        }
      }
      if (item_not_yet_added) {
        this.product_list.push(item);
      }
    },
    cancel() {
      this.product_list = [];
    },
    formatDate() {
      let date = new Date();
      let day = date.getDate();
      let month = date.getMonth() + 1;
      let year = date.getFullYear();

      // This arrangement can be altered based on how we want the date's format to appear.
      let currentDate = `${day}/${month}/${year}`;
      return currentDate;
    },
    fetchLatestInvoiceNo() {
      console.log("Hello world!");
    },
    saveInvoice() {
      console.log(this.product_list);
    },
  },

  computed: {
    total_invoice() {
      let total = 0;
      this.product_list.forEach((item) => {
        total += item.product_price * item.product_qty;
      });
      return total;
    },
  },

  mounted() {
    this.emitter.on("add_product", (item) => {
      this.add_product(item);
    });
  },
};
</script>
