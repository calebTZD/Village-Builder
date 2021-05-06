import {SimulationView} from './SimView.js';
import {WorldView} from './WorldView.js';

const SimApp = Vue.createApp(SimulationView);


SimApp.component('WorldView', WorldView);

export const SimulationApp = SimApp;