import { createRouter, createWebHistory } from "vue-router";
import Index from "../components/Index.vue";
import Pakaian from "../components/Pakaian.vue";

const routes = [
  {
    path: "/",
    name: "Index",
    component: Index,
  },
  {
    path: "/pakaian",
    name: "Pakaian",
    component: Pakaian,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
