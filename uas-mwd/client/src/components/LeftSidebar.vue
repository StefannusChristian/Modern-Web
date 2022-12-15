<template>
  <div class="container w-25">
    <div class="p-3 bg-light">
      <div class="mb-3">
        <h3>Invoice Header</h3>
        <div class="bg-dark text-white p-2 m-2 rounded-3">
          Admin:<br />
          <span class="fw-semibold">John Doe</span>
        </div>
      </div>
      <div class="mb-3">
        <h4>Invoice Body</h4>
        <ul class="list-group">
          <li class="list-group-item">Item 1</li>
          <li class="list-group-item">Item 2</li>
          <li class="list-group-item">Item 3</li>
        </ul>
      </div>
      <button class="btn btn-success d-block w-100 mb-1">
        <i class="bi bi-credit-card-2-back-fill me-2"></i>Pay
      </button>
      <button class="btn btn-danger d-block w-100">
        <i class="bi bi-x-square-fill me-2"></i> Cancel
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "LeftSidebar",
};
</script>
