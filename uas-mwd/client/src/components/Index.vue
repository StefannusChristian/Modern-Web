<template>
  <ul>
    <li v-for="product in products" :key="product.id">
      {{ product }}
    </li>
  </ul>
</template>

<script>
import axios from "axios";

export default {
  name: "Index",
  data() {
    return {
      products: null,
    };
  },
  methods: {
    getMessage() {
      const path = "http://127.0.0.1:5000/";
      axios
        .get(path)
        .then((res) => {
          this.products = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>

<style></style>
