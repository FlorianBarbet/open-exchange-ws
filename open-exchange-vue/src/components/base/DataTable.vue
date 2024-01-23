<template>
  <div>
    <input type="button" value="<< Prev." @click.prevent="this.decreaseLimit()"  :disabled="!(this.limit > step)" />
    <input type="button" value="Next >>"     @click.prevent="this.increaseLimit()"  :disabled="!(this.limit < (this.rows ?? []).length)" />
  </div>
  <table>
    <thead>
    <tr>
      <th v-for="header of headers" :key="header">{{ header }}</th>
    </tr>
    </thead>
    <tbody>
    <tr v-for="row of limitedContent()" :key="row[0]">
      <td v-for="cells of row" :key="cells">{{ cells }}</td>
    </tr>
    </tbody>
  </table>
</template>

<script lang="ts">
import {Options, Vue} from 'vue-class-component';

@Options({
  computed: {
    step() {
      return DataTable.STEP
    }
  },
  props: {
    rows: {
      type: Array,
      default: [[]]
    },
    headers: {
      type: Array,
      default: []
    },
  }
})
export default class DataTable extends Vue {
  static STEP = 10

  headers!: string[];
  rows!: string[][];

  limit = DataTable.STEP;

  limitedContent(): Array<Array<string>> {
    return this.rows?.slice(this.limit - DataTable.STEP, this.limit) ?? [];
  }

  increaseLimit() {
    if (this.limit < (this.rows ?? []).length) {
      this.limit += DataTable.STEP;
    }
  }

  decreaseLimit() {
    if (this.limit > DataTable.STEP) {
      this.limit -= DataTable.STEP;
    }
  }
}
</script>

<style scoped>
tr:nth-child(even) {
  background-color: #d4cecd;

}

th {
  background-color: #918f8e;
  color: #fff;
}

td:not(:first-child), th:not(:first-child) {
  border: 1px solid #ddd;
  padding: 8px;
}

tr:hover {
  background-color: #a66560;
  color: #fff;
}

table {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

* {
  text-align: center;
}
</style>
