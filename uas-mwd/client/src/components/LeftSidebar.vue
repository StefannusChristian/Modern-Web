<template>
  <div class="container w-25 mb-5">
    <div class="p-3 bg-light">
      <div class="mb-3">
        <div class="bg-white p-3 rounded-3">
          <span class="fs-6 text-muted d-block">Admin</span>
          <span class="fw-600 fs-5">{{ currentUser }}</span>
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
      <div class="d-flex align-items-center justify-content-between">
        <span class="d-block fs-6">Subtotal</span><br />
        <span class="d-block fs-6">
          {{
            new Intl.NumberFormat("id-ID", {
              style: "currency",
              currency: "IDR",
            })
              .format(total_invoice)
              .slice(0, -3)
          }}
        </span>
      </div>
      <div class="d-flex align-items-center justify-content-between mb-2">
        <div>
          <span class="fs-6 mb-2 fw-500">Diskon</span><br />
          <span class="fw-600"> {{ diskon }}% </span>
        </div>
        <div class="text-danger">
          -{{
            new Intl.NumberFormat("id-ID", {
              style: "currency",
              currency: "IDR",
            })
              .format(price_after_discount.cutoff)
              .slice(0, -3)
          }}
        </div>
      </div>
      <div class="d-flex align-items-center justify-content-between mb-3">
        <span class="d-block fs-6 mb-2 fw-500">Total After Discount</span><br />
        <span class="d-block fw-600">
          {{
            new Intl.NumberFormat("id-ID", {
              style: "currency",
              currency: "IDR",
            })
              .format(price_after_discount.price)
              .slice(0, -3)
          }}
        </span>
      </div>
      <button
        class="btn btn-success d-block w-100 mb-1 text-start"
        @click="checkout()"
      >
        <i class="bi bi-credit-card-2-back-fill me-2"></i>Checkout
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
export default {
  name: "LeftSidebar",
  data() {
    return {
      product_list: [],
      currentDate: this.formatDate(),
      pay_warning_message: "",
      currentUser: sessionStorage.getItem("currentLoggedIn"),
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
      console.log("HALOO");
      this.pay_warning_message = "";
      let index = this.get_product_id_index(item);
      console.log(index, "INI INDEX!!!");
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
    checkout() {
      localStorage.setItem(
        "temp_product_list",
        JSON.stringify(this.product_list)
      );
      if (this.product_list.length > 0) {
        this.pay_warning_message = "";
        localStorage.setItem("product_list", JSON.stringify(this.product_list));
        this.$router.push({
          path: "payment_page",
          query: {
            diskon: this.diskon,
            final_price: this.price_after_discount.price,
          },
        });
        this.emitter.emit("get-new-invoice-no");
        this.emitter.emit("checkout");
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
    price_after_discount() {
      let dis = parseInt(this.diskon);
      let one_hundred_minus_dis = (100 - dis) / 100;
      return {
        price: one_hundred_minus_dis * this.total_invoice,
        cutoff: (dis / 100) * this.total_invoice,
      };
    },
    diskon() {
      let dis = "0";
      let total_price = this.total_invoice;

      if (total_price >= 1000000) {
        dis = "50";
      } else if (total_price >= 500000) {
        dis = "20";
      } else if (total_price >= 200000) {
        dis = "10";
      } else if (total_price >= 100000) {
        dis = "5";
      }
      return dis;
    },
  },
  mounted() {
    this.emitter.on("add_product", (item) => {
      this.add_product(item);
    });
    if (localStorage.getItem("temp_product_list")) {
      this.product_list = JSON.parse(localStorage.getItem("temp_product_list"));
      console.log(this.product_list);
    }
  },
};
</script>
