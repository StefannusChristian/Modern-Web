<template>
  <h1>Ini Component Alat Tulis</h1>
  <ul>
    <li v-for="alat in alat_tulis" :key="alat.product_id" :id="alat.product_id">
      {{ alat }}
    </li>
  </ul>
</template>

<script>
import axios from "axios";

export default {
  name: "AlatTulis",
  data() {
    return {
      alat_tulis: null,
    };
  },
  methods: {
    get_alat_tulis() {
      const path = "http://127.0.0.1:5000/alat_tulis";
      axios
        .get(path)
        .then((res) => {
          this.alat_tulis = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.get_alat_tulis();
  },
};
</script>

<style></style>
