<template>
  <div>
    <DatePicker @select-date="load"/>
    <p> EUR: {{ eur }}, USD: {{ usd }}, JPY: {{ jpy }}, GBP:{{ gbp }} {{scenario}}</p>
  </div>
</template>

<script lang="ts">
import {Options, Vue} from 'vue-class-component';
import DatePicker from "@/components/base/DatePicker.vue";
import {getRates, PrintedRates} from "@/core/rates";
import useEventsBus from "@/core/event-bus";
const {emit} = useEventsBus();

@Options({
  components: {DatePicker},
  props: {
    scenario: {
      type: Number,
      default: 1
    }
  }

})
export default class RateSelector extends Vue {
  scenario!: number;

  eur = 1;
  usd = 2;
  jpy = 3;
  gbp = 4;


  async load(date: string) {
    const resultOfDate = localStorage.getItem(date) ?? await (async () => {
        const ratesToStore = (await getRates(date, {scenario: this.scenario}));
        console.log(ratesToStore, this.scenario)
        if (ratesToStore) {

          if (this.scenario === 2) {
            localStorage.setItem(date, JSON.stringify(ratesToStore));
            emit('updated:rates', 'refresh');
            return JSON.stringify(ratesToStore);
          }

          if (this.scenario === 1) {
            localStorage.setItem(date, ratesToStore as string);
            emit('updated:rates', 'refresh');
            return ratesToStore as string;
          }

        }
    })();
    const {rates: {EUR=-1, USD=-1, JPY=-1, GBP=-1}} = JSON.parse(resultOfDate ?? '{}') as PrintedRates;

    this.eur = +EUR;
    this.usd = +USD;
    this.jpy = +JPY;
    this.gbp = +GBP;
  }
}
</script>

<style scoped>
div {
  margin-left: 5%;
  display: flex;
  justify-content: flex-start;
  gap: 10px;
}
</style>