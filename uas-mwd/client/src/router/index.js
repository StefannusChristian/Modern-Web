import { createRouter, createWebHistory } from "vue-router";
import Pakaian from "../components/Pakaian.vue";
import Makanan from "../components/Makanan.vue";
import AlatTulis from "../components/AlatTulis.vue";
import Home from "../components/Home.vue";
import ReportSales from "../components/ReportSales.vue";
import PaymentSuccess from "../components/PaymentSuccess.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/pakaian",
    name: "Pakaian",
    component: Pakaian,
  },
  {
    path: "/makanan",
    name: "Makanan",
    component: Makanan,
  },
  {
    path: "/alat_tulis",
    name: "AlatTulis",
    component: AlatTulis,
  },
  {
    path: "/report_sales",
    name: "ReportSales",
    component: ReportSales,
  },
  {
    path: "/payment_success",
    name: "PaymentSucess",
    component: PaymentSuccess,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
