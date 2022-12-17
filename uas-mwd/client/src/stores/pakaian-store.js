import { defineStore } from "pinia";
import axios from "axios";

export const usePakaianStore = defineStore({
  state: () => {
    return {
      items: [],
    };
  },
  actions: {
    fetchPakaian() {
      this.items = [];
      axios
        .get("http://127.0.0.1:5000/pakaian")
        .then((res) => {
          res.data.forEach(function (obj) {
            obj.img_filepath = "http://127.0.0.1:5000/" + obj.img_filepath;
            obj.product_name =
              obj.product_name.charAt(0).toUpperCase() +
              obj.product_name.slice(1);
            obj.product_price_int = obj.product_price;
            obj.product_price = new Intl.NumberFormat("id-ID", {
              style: "currency",
              currency: "IDR",
            })
              .format(obj.product_price)
              .slice(0, -3);
            this.items.push(obj);
          });
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
});
