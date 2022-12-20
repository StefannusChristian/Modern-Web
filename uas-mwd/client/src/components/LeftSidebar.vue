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
            <div class="d-flex justify-content-between align-items-center py-2">
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
              <div class="btn-group" role="group" aria-label="Basic example">
                <button
                  @click="decrease_product(item)"
                  type="button"
                  class="btn btn-outline-dark"
                >
                  -
                </button>
                <button
                  @click="add_product(item)"
                  type="button"
                  class="btn btn-outline-dark"
                >
                  +
                </button>
                <button @click="clear(item)" class="btn btn-danger">
                  <i class="bi bi-trash3-fill"></i>
                </button>
              </div>
            </div>
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
        @click="pay_product()"
      >
        <i class="bi bi-credit-card-2-back-fill me-2"></i> Pay
      </button>
      <button @click="cancel" class="btn btn-danger d-block w-100 text-start">
        <i class="bi bi-x-square-fill me-2"></i>Cancel
      </button>
      <div
        v-if="pay_warning_message !== ''"
        class="alert alert-danger alert-dismissible fade show mt-3"
        role="alert"
      >
        <strong>{{ pay_warning_message }}</strong>
        <button
          type="button"
          class="btn-close"
          data-bs-dismiss="alert"
          aria-label="Close"
          @click="toggleAlert"
        ></button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "LeftSidebar",
  data() {
    return {
      product_list: [],
      currentDate: this.formatDate(),
      pay_warning_message: "",
    };
  },
  props: {
    latestInvoiceNo: Number,
  },
  methods: {
    get_product_id_index(item) {
      for (let index = 0; index < this.product_list.length; index++) {
        if (this.product_list[index].product_id === item.product_id) {
          return index;
        }
      }
      return -1;
    },
    add_product(item) {
      this.pay_warning_message = "";
      let index = this.get_product_id_index(item);
      // Berarti belom ada di product list
      if (index === -1) {
        this.product_list.push(item);
      } else {
        this.product_list[index].product_qty++;
      }
    },
    decrease_product(item) {
      let index = this.get_product_id_index(item);
      this.product_list[index].product_qty--;
      if (this.product_list[index].product_qty < 1) {
        this.product_list.shift();
      }
    },
    pay_product() {
      const post_url = "http://127.0.0.1:5000/save_invoice";
      if (this.product_list.length > 0) {
        this.pay_warning_message = "";
        axios
          .post(post_url, JSON.stringify(this.product_list), {
            headers: {
              "Content-Type": "application/json",
            },
          })
          .then((response) => console.log(response))
          .catch((error) => console.log(error));
        this.product_list = [];
        this.$router.push("/payment_success");
        this.emitter.emit("get-new-invoice-no");
      } else {
        this.pay_warning_message = "Product list is empty.";
      }
    },
    cancel() {
      this.product_list = [];
    },
    toggleAlert() {
      this.pay_warning_message = "";
    },
    clear(item) {
      let index = this.get_product_id_index(item);
      this.product_list.splice(index, 1);
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
      console.log(item.product_name);
      this.add_product(item);
    });
  },
};
</script>
