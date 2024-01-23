<template>
  <ReloadRates/>
  <hr/>
  <RateSelector/>
  <hr/>
  <RateTable />
</template>

<script lang="ts">
import {Options, Vue} from 'vue-class-component';
import ReloadRates from "@/components/ReloadRates.vue";
import RateTable from "@/components/RateTable.vue";
import RateSelector from "@/components/RateSelector.vue";

@Options({
  components: {
    RateSelector,
    RateTable,
    ReloadRates,
  },
})
export default class Scenario1 extends Vue {}
</script>