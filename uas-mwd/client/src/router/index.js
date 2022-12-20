import { createRouter, createWebHistory } from "vue-router";
import Categories from "../components/CategoryItem.vue";
import ReportSales from "../components/ReportSales.vue";
import PaymentSuccess from "../components/PaymentSuccess.vue";

const routes = [
    {
        path: "/",
        name: "Categories",
        component: Categories,
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
