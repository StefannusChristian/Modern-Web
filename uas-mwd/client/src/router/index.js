import { createRouter, createWebHistory } from "vue-router";
import Pakaian from "../components/Pakaian.vue";
import Makanan from "../components/Makanan.vue";
import AlatTulis from "../components/AlatTulis.vue";

const routes = [
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
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;
