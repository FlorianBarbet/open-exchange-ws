<template>
  <div>
    <label> Reload Data </label>
    <input type="button" value="Reload" @click.prevent="strategy"/>
  </div>
</template>

<script lang="ts">
import {Options, Vue} from 'vue-class-component';
import useEventsBus from "@/core/event-bus";
import {loadAll, getRates} from "@/core/rates";

const {emit} = useEventsBus();

@Options({
  props: {
    scenario: {
      type: Number,
      default: 1
    }
  }
})
export default class ReloadRates extends Vue {
  scenario!: number;

  strategy() {
    if (this.scenario === 2) {
      return this.treatIndex();
    }

    return this.registerFile();
  }

  async treatIndex() {
    await loadAll(String(this.scenario))
  }

  async registerFile() {
    const today = new Date().formatISODate();
    if (localStorage.getItem(today)) {
      return;
    }

    const ratesOfDay = await getRates(today);
    if (ratesOfDay) {
      localStorage.setItem(today, ratesOfDay as string);
      emit('updated:rates', today);
    }
  }
}
</script>

<style scoped>
div {
  display: flex;
  flex: 1 1 auto;
  gap: 10px;
  justify-content: flex-start;
  align-items: center;
}
</style>
