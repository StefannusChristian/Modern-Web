<template>
  <div>
    {{ books }}
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Books",
  data() {
    return {
      books: null,
    };
  },
  methods: {
    getBooks() {
      const path = "http://127.0.0.1:5000/books";
      axios
        .get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getBooks();
  },
};
</script>

<style></style>
