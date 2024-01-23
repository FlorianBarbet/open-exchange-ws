<template>
  <ReloadRates :scenario="2"/>
  <hr/>
  <RateSelector :scenario="2"/>
  <hr/>
  <RateTable :headers="rateTableColumnShow" :scenario="2">
    <input type="button" value="Configure" @click="turnOnConfiguration"/>
    <div class="control-pad" v-show="showConfig">
      <div>
        <input type="text" v-model="this.rateTableColumnConfiguration"/>
        <input type="button" value="Close" @click="turnOffConfiguration"/>
      </div>
    </div>
  </RateTable>
</template>

<script lang="ts">
import {Options, Vue} from 'vue-class-component';
import ReloadRates from "@/components/ReloadRates.vue";
import RateTable from "@/components/RateTable.vue";
import RateSelector from "@/components/RateSelector.vue";
import useEventsBus from "@/core/event-bus";
const {emit} = useEventsBus();
@Options({
  components: {
    RateSelector,
    RateTable,
    ReloadRates,
  },
})
export default class Scenario1 extends Vue {
  rateTableColumnShow = localStorage.getItem('rates:configuration')?.split(',') ?? ['Date', 'EUR'];
  rateTableColumnConfiguration = "";
  showConfig = false;

  turnOnConfiguration() {
    this.showConfig = true;
    this.rateTableColumnConfiguration = this.rateTableColumnShow.toString();
  }

  turnOffConfiguration() {
    this.showConfig = false;
    // to avoid mis-manipulation
    if (this.rateTableColumnConfiguration.endsWith(',')) {
      this.rateTableColumnConfiguration = this.rateTableColumnConfiguration.substring(0, this.rateTableColumnConfiguration.length - 1)
    }

    this.rateTableColumnShow = this.rateTableColumnConfiguration.split(',');
    localStorage.setItem("rates:configuration", this.rateTableColumnConfiguration);
    emit('updated:rates', 'refresh');
  }
}
</script>