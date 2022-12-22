<template>
  <div class="w-100 mb-5 container py-3">
    <h2 class="mb-3">Report Sales</h2>
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
    <div class="d-flex align-items-start justify-content-between">
      <div class="w-50">
        <div
          v-for="invoice in invoices"
          :key="invoice.invoiceId"
          :id="invoice.invoiceId"
          class="p-3 rounded-2 bg-light mb-1"
        >
          InvoiceID: {{ invoice.invoiceId }}<br />
          <ul>
            <li
              v-for="invoiceDetail in invoice.details"
              :key="invoiceDetail.invoice_detail_id"
            >
              {{ invoiceDetail.product_name }} ({{ invoiceDetail.qty }})
            </li>
          </ul>
          Total: {{ invoice.totalPrice }}
        </div>
      </div>
      <div class="w-50 px-4">
        <h3 class="mb-3">Sales per Category</h3>
        <div class="container p-3 rounded-3">
          <h5 class="fw-600">Pakaian</h5>
          <table class="table table-striped">
            <tr>
              <th>Product</th>
              <th>Quantity</th>
              <th>Sales</th>
            </tr>
            <tr>
              <td>Kaos</td>
              <td>120</td>
              <td>Rp 3.000.000</td>
            </tr>
            <tr>
              <td>Hoodie</td>
              <td>120</td>
              <td>Rp 3.000.000</td>
            </tr>
            <tr>
              <td>Sweater</td>
              <td>120</td>
              <td>Rp 3.000.000</td>
            </tr>
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
          { username: username },
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
  },
};
</script>
