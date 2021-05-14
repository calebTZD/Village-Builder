import {SimulationView} from './SimView.js';
import {WorldView} from './WorldView.js';
import {VillagesView} from './VillagesView.js';

const SimApp = Vue.createApp(SimulationView);

SimApp.component('WorldView', WorldView);
SimApp.component('VillagesView', VillagesView);

export const SimulationApp = SimApp;