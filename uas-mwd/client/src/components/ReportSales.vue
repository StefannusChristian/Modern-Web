<template>
  <div class="w-100 mb-5 container py-3">
    <h2 class="mb-3 fw-800 fs-1">Report Sales</h2>
    <div
      class="mb-3 d-flex justify-content-between align-items-center container"
    >
      <div>
        <span>Admin:</span><br /><span class="fs-2 fw-600">{{ username }}</span>
      </div>
      <div>
        <small>Total Sales: </small><br /><span class="fw-600 fs-3">{{
          total_sales_display
        }}</span>
      </div>
    </div>
    <div class="d-flex justify-content-between align-items-start">
      <div class="w-50 container px-2 d-flex flex-wrap">
        <div
          v-for="invoice in invoices"
          :key="invoice.invoiceId"
          :id="invoice.invoiceId"
          class="p-3 rounded-3 bg-light mb-2 mx-1"
          style="width: 48%"
        >
          <div class="mb-2">InvoiceID: {{ invoice.invoiceId }}</div>
          <ul class="list-group mb-3">
            <li
              v-for="invoiceDetail in invoice.details"
              :key="invoiceDetail.invoice_detail_id"
              class="list-group-item d-flex justify-content-between"
            >
              <div>{{ invoiceDetail.product_name }}</div>
              <div>x{{ invoiceDetail.qty }}</div>
            </li>
          </ul>
          Total: <br /><span class="fw-600">{{ invoice.totalPrice }}</span>
        </div>
      </div>
      <div class="w-50 container px-3">
        <h3 class="mb-3">Sales Per Category</h3>
        <div class="my-3">
          <h5>Pakaian</h5>
          <table class="table table-striped">
            <thead>
              <tr class="table-dark">
                <th>Product Name</th>
                <th>Quantity</th>
                <th>Sales</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="item in categorySales.Pakaian"
                :key="item.product_name"
              >
                <td class="w-25">{{ item.product_name }}</td>
                <td>{{ item.sum_qty }}</td>
                <td>
                  {{
                    new Intl.NumberFormat("id-ID", {
                      style: "currency",
                      currency: "IDR",
                    })
                      .format(parseInt(item.sum_qty) * item.product_price)
                      .slice(0, -3)
                  }}
                </td>
              </tr>
              <tr>
                <td></td>
                <td>Total Sales</td>
                <td>Rp 1.000.000</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="my-4">
          <h5>Makanan</h5>
          <table class="table table-striped">
            <thead>
              <tr class="table-dark">
                <th>Product Name</th>
                <th>Quantity</th>
                <th>Sales</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="item in categorySales.Makanan"
                :key="item.product_name"
              >
                <td class="w-25">{{ item.product_name }}</td>
                <td>{{ item.sum_qty }}</td>
                <td>
                  {{
                    new Intl.NumberFormat("id-ID", {
                      style: "currency",
                      currency: "IDR",
                    })
                      .format(parseInt(item.sum_qty) * item.product_price)
                      .slice(0, -3)
                  }}
                </td>
              </tr>
              <tr>
                <td></td>
                <td>Total Sales</td>
                <td>Rp 1.000.000</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="my-3">
          <h5>Alat Tulis</h5>
          <table class="table table-striped">
            <thead>
              <tr class="table-dark">
                <th>Product Name</th>
                <th>Quantity</th>
                <th>Sales</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="item in categorySales.AlatTulis"
                :key="item.product_name"
              >
                <td class="w-25">{{ item.product_name }}</td>
                <td>{{ item.sum_qty }}</td>
                <td>
                  {{
                    new Intl.NumberFormat("id-ID", {
                      style: "currency",
                      currency: "IDR",
                    })
                      .format(parseInt(item.sum_qty) * item.product_price)
                      .slice(0, -3)
                  }}
                </td>
              </tr>
              <tr>
                <td></td>
                <td>Total Sales</td>
                <td>Rp 1.000.000</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "ReportSales",
  data() {
    return {
      invoices: [],
      total_user_sales: 0,
      total_sales_display: null,
      username: sessionStorage.getItem("currentLoggedIn"),
      categorySales: { Pakaian: [], AlatTulis: [], Makanan: [] },
    };
  },
  methods: {
    getInvoices() {
      const username = sessionStorage.getItem("currentLoggedIn");
      console.log(username);
      const path = "http://127.0.0.1:5000/report_sales";
      axios
        .post(
          path,
          { username: this.username },
          {
            headers: {
              "Content-Type": "application/json",
            },
          }
        )
        .then((res) => {
          // console.log(res);
          this.processInvoiceData(res.data);
          console.log(this.invoices);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getSalesPerCategory() {
      const path = "http://127.0.0.1:5000/sales_per_category";
      axios
        .post(
          path,
          { username: this.username },
          {
            headers: {
              "Content-Type": "application/json",
            },
          }
        )
        .then((res) => {
          // console.log(res);
          let data = res.data;
          for (let i = 0; i < data.length; i++) {
            if (data[i].category_id === 1) {
              this.categorySales.Pakaian.push(data[i]);
            } else if (data[i].category_id === 2) {
              this.categorySales.Makanan.push(data[i]);
            } else if (data[i].category_id === 3) {
              this.categorySales.AlatTulis.push(data[i]);
            }
          }
          console.log(this.categorySales);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    processInvoiceData(data) {
      for (let i = 0; i < data.invoices.length; i++) {
        let invoiceObj = {};
        this.total_user_sales += data.invoices[i].total_price;
        invoiceObj = data.invoice_details[data.invoices[i].invoice_id];
        // console.log(invoiceObj);

        let invoice = {
          invoiceId: data.invoices[i].invoice_id,
          totalPrice: new Intl.NumberFormat("id-ID", {
            style: "currency",
            currency: "IDR",
          })
            .format(data.invoices[i].total_price)
            .slice(0, -3),
          details: invoiceObj,
        };

        this.invoices.push(invoice);
      }
      this.total_sales_display = new Intl.NumberFormat("id-ID", {
        style: "currency",
        currency: "IDR",
      })
        .format(this.total_user_sales)
        .slice(0, -3);
    },
  },
  created() {
    this.getInvoices();
    this.getSalesPerCategory();
  },
};
</script>
