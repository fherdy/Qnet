<template>
  <div class="contact">
    <div class="title mb-3">
      Here are the Contact Information of the developers
    </div>
    <table class="mx-auto">
      <tr>
        <th>Name</th>
        <th>Email</th>
        <th>Phone Number</th>
      </tr>
      <tr>
        <td>Amier Hajyassin</td>
        <td>amierhajyassin89@gmail.com</td>
        <td>347-764-2080</td>
      </tr>
      <tr>
        <td>Anya Komarovska</td>
        <td>ankakom3@gmail.com</td>
        <td>716-237-0357</td>
      </tr>
      <tr>
        <td>Kevin Wong </td>
        <td>kevinwong1997@hotmail.com</td>
        <td>718-219-9785</td>
      </tr>
      <tr>
        <td>Ferdinand Tettey</td>
        <td>ferdinandowusu13@gmail.com</td>
        <td>347-757-7315</td>
      </tr>
      <tr>
        <td>Jonathan Raysor </td>
        <td>jonathan.raysorbc@gmail.com</td>
        <td>347-760-5966</td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'Contact',
  data() {
    return {
    };
  },
};
</script>

<style lang="scss" scoped>
.contact {
  .title {
    font-size: 20px;
    font-weight: 600;
  }
  table {
    text-align: left;
  }
}
</style>
