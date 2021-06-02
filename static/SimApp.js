import {SimulationView} from './SimView.js';
import {WorldView} from './WorldView.js';
import {VillagesView} from './VillagesView.js';
import {LocationView} from './LocationView.js';
import {BuildingView} from './BuildingView.js';
import {VilligerView} from './VillagerView.js';
import {SimListView} from './SimListView.js';


const SimApp = Vue.createApp(SimulationView);

SimApp.component('WorldView', WorldView);
SimApp.component('VillagesView', VillagesView);
SimApp.component('LocationView', LocationView);
SimApp.component('BuildingView', BuildingView);
SimApp.component('VilligerView', VilligerView);
SimApp.component('SimListView', SimListView);


export const SimulationApp = SimApp;