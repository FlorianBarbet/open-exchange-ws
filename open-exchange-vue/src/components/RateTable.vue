<template>
  <slot></slot>
  <DataTable :rows="this.rows" :headers="this.headers"/>
</template>

<script lang="ts">
import {Options, Vue} from 'vue-class-component';

import DataTable from "@/components/base/DataTable.vue";
import {watch} from "vue";
import useEventsBus from "@/core/event-bus";

const {bus: receiver} = useEventsBus()

@Options({
  components: {DataTable},
  props: {
    headers: {
      type: Array,
      default: ['Date', 'EUR', 'USD', 'JPY', 'GBP']
    },
    scenario: {
      type: Number,
      default: 1
    }
  }
})
export default class RateTable extends Vue {
  rows: string[][] = [];
  headers!: string[];
  scenario!: number;

  beforeMount() {
    watch(() => receiver.value.get('updated:rates'), (date) => {
      console.log(date);
      this.load();
    });
    this.load();
  }

  addIndexAtFirstColumn() {
    if (this.headers?.[0] !== '#') {
      this.headers.unshift('#');
    }

    if (this.rows?.[0]?.length < this.headers.length) {
      this.rows.map((row, index) => {
        row?.unshift(`${index + 1}`);
        return row;
      });
    }
  }


  load() {
    this.rows = Object.keys(localStorage).filter((key) => !key.startsWith('rates')).map(this.buildRow, this);
    this.addIndexAtFirstColumn();
  }

  buildRow(date: string, index: number) {
    const resultOfDate = JSON.parse(localStorage.getItem(date) ?? '{}');

    // to extract a
    if (this.scenario === 2) {
      const splitDate = String(date).split(':');

      return [
        index,
        splitDate.length === 1 ? splitDate[0]:splitDate[1],
        ...this.headers
            .filter((rateKey) => rateKey !== 'Date' && rateKey !== '#')
            .map((rateKey) => resultOfDate.rates[rateKey.toUpperCase()] ?? 'N/A')
      ];
    }

    return [
      index,
      date,
      ...this.headers
          .filter((rateKey) => rateKey !== 'Date' && rateKey !== '#')
          .map((rateKey) => resultOfDate.rates[rateKey.toUpperCase()] ?? 'N/A')
    ];
  }


}
</script>