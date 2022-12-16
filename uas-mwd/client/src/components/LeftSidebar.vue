<template>
  <div class="container w-25">
    <div class="p-3 bg-light">
      <div class="mb-3">
        <h3>Invoice Header</h3>
        <div class="bg-dark text-white p-2 m-2 rounded-3">
          Admin:<br />
          <span class="fw-semibold">John Doe</span>
        </div>
      </div>
      <div class="mb-3">
        <h4>Invoice Body</h4>
        <ul
          v-for="item in product_list"
          class="list-group"
          :key="item.product_id"
        >
          <li class="list-group-item">
            {{ item.product_name }} qty ({{ item.product_qty }}):
            {{ item.product_price * item.product_qty }}
          </li>
        </ul>
      </div>
      <h5>Total: {{ total_invoice }}</h5>
      <button class="btn btn-success d-block w-100 mb-1">
        <i class="bi bi-credit-card-2-back-fill me-2"></i>Pay
      </button>
      <button @click="cancel" class="btn btn-danger d-block w-100">
        <i class="bi bi-x-square-fill me-2"></i> Cancel
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
    };
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
