<template>
  <div class="container mt-5">
    <h1 class="mb-5 text-center fw-800">Point of Sales App</h1>
    <h3 class="fw-600 mb-4 text-center">Log In</h3>
    <div class="container w-50">
      <div class="form-floating mb-3">
        <input
          type="text"
          class="form-control"
          id="username"
          placeholder="admin_username"
          v-model="username"
          required
        />
        <label for="floatingInput">Username:</label>
      </div>
      <div class="form-floating mb-3">
        <input
          type="password"
          class="form-control"
          id="password"
          placeholder="Password"
          v-model="password"
          required
        />
        <label for="floatingPassword">Password</label>
      </div>
      <button
        class="btn btn-dark w-100 text-center mb-3"
        @click="sendLoginData"
      >
        Log In
      </button>
      <div
        v-if="login_error"
        class="alert alert-danger alert-dismissible fade show"
        role="alert"
      >
        <strong>Invalid credentials.</strong>
        <button
          type="button"
          class="btn-close"
          data-bs-dismiss="alert"
          aria-label="Close"
        ></button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      login_error: false,
    };
  },
  methods: {
    sendLoginData() {
      if (this.username !== "" && this.password !== "") {
        axios
          .post(
            "http://127.0.0.1:5000/login",
            { username: this.username, password: this.password },
            {
              headers: {
                "Content-Type": "application/json",
              },
            }
          )
          .then((res) => {
            if (res.data.message === "login-success") {
              sessionStorage.setItem("currentLoggedIn", res.data.username);
              //   console.log(sessionStorage.getItem("currentLoggedIn"));
              this.$emit("login-detected");
            } else {
              console.log(res.data.message);
              this.login_error = true;
            }
          })
          .catch((error) => console.log(error));
      }
    },
  },
  emits: ["login-detected"],
};
</script>

<style></style>
