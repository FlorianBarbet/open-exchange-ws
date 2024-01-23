<template>
  <input type="date" v-model = "this.selectedDate" @change="$emit('selectDate', this.selectedDate)" onfocus="this.showPicker()" />
</template>

<script lang="ts">
import {Options, Vue} from 'vue-class-component';

@Options({
  emits: ['selectDate']
})
export default class DatePicker extends Vue {
  selectedDate: string = this.today();

  today() {
    return new Date().formatISODate();
  }

  mounted() {
    this.$emit('selectDate', this.selectedDate);
  }
}
</script>