import {SimulationView} from './SimView.js';

const SimApp = Vue.createApp(SimulationView);

SimApp.component('datacomp', {
  props: ['mydata'],
  template: `***{{ mydata }}`
});

export const SimulationApp = SimApp;