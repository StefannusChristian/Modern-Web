import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "./assets/global.css";
import mitt from "mitt";
import { createPinia } from "pinia";

let app = createApp(App);
app.use(createPinia());
const emitter = mitt();
app.config.globalProperties.emitter = emitter;
app.use(router).mount("#app");
