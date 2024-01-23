import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'
import Scenario1 from "@/views/Scenario1.vue";
import Scenario2 from "@/views/Scenario2.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: '/scenario1', // route=/#/scenario1/
    name: 'scenario1',
    component: Scenario1
  },
  {
    path: '/scenario2', // route=/#/scenario2/
    name: 'scenario2',
    component: Scenario2
  },

];

const router = createRouter({
  history: createWebHashHistory(),
  routes
});

export default router;
