<template>
  <ul class="nav justify-content-end">
    <li
      v-for="category in all_categories"
      :key="category.category_id"
      class="nav-link text-dark"
      style="cursor: pointer"
      @click="select_category(category.category_id)"
    >
      {{ category.category_name }}
    </li>

    <li class="nav-item">
      <a href="#" class="nav-link text-dark" @click="logout">
        Logout <i class="bi bi-box-arrow-right ms-2"></i
      ></a>
    </li>
  </ul>
</template>

<script>
import axios from "axios";
export default {
  name: "ProductNavigation",
  data() {
    return {
      all_categories: [],
    };
  },
  methods: {
    get_category() {
      const path = "http://127.0.0.1:5000/categories";
      axios
        .get(path)
        .then((res) => {
          let all_categories = [];
          res.data.forEach((obj) => {
            all_categories.push(obj);
          });
          this.all_categories = all_categories;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    select_category(category_id) {
      this.emitter.emit("select_category", category_id);
    },
    logout() {
      sessionStorage.clear();
      this.emitter.emit("logged-out");
      this.$router.push("/");
    },
  },
  created() {
    this.get_category();
  },
};
</script>

<style></style>
