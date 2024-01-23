import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

createApp(App).use(router).mount('#app');

Array.prototype.deepClone = function() {
    return JSON.parse(JSON.stringify(this));
};

Date.prototype.formatISODate = function() {
    return this.toISOString().split('T')[0];
};

declare global {
    interface Array<T> {
        deepClone():T[];
    }

    interface Date {
        formatISODate(): string;
    }
}