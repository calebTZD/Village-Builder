import {SimulationView} from './SimView.js';
import {WorldView} from './WorldView.js';
import {VillagesView} from './VillagesView.js';
import {LocationView} from './LocationView.js';

const SimApp = Vue.createApp(SimulationView);

SimApp.component('WorldView', WorldView);
SimApp.component('VillagesView', VillagesView);
SimApp.component('LocationView', LocationView);

export const SimulationApp = SimApp;