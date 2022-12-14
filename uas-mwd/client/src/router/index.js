import { createRouter, createWebHistory } from "vue-router";
import Ping from "../components/Ping.vue";
import Books from "../components/Books.vue";

const routes = [
  {
    path: "/ping",
    name: "Ping",
    component: Ping,
  },
  {
    path: "/books",
    name: "Books",
    component: Books,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
