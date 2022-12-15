<template>
  <h1>Ini Component Makanan</h1>
  <ul>
    <li v-for="makan in makanan" :key="makan.product_id" :id="makan.product_id">
      {{ makan }}
    </li>
  </ul>
</template>

<script>
import axios from "axios";

export default {
  name: "Makanan",
  data() {
    return {
      makanan: null,
    };
  },

  methods: {
    getMakanan() {
      const path = "http://127.0.0.1:5000/makanan";
      axios
        .get(path)
        .then((res) => {
          this.makanan = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMakanan();
  },
};
</script>

<style></style>
