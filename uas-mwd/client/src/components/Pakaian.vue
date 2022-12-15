<template>
  <ul>
    <li v-for="pakai in pakaian" :key="pakai.product_id" :id="pakai.product_id">
      {{ pakai }}
    </li>
  </ul>
</template>

<script>
import axios from "axios";

export default {
  name: "Pakaian",
  data() {
    return {
      pakaian: null,
    };
  },
  methods: {
    getPakaian() {
      const path = "http://127.0.0.1:5000/pakaian";
      axios
        .get(path)
        .then((res) => {
          this.pakaian = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getPakaian();
  },
};
</script>

<style></style>
