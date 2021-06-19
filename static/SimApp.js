import {SimulationView} from './SimView.js';
import {WorldView} from './WorldView.js';
import {VillagesView} from './VillagesView.js';
import {LocationView} from './LocationView.js';
import {BuildingView} from './BuildingView.js';
import {VillagerView} from './VillagerView.js';
import {SimListView} from './SimListView.js';
import {StatsView} from './StatsView.js';


const SimApp = Vue.createApp(SimulationView);

SimApp.component('WorldView', WorldView);
SimApp.component('VillagesView', VillagesView);
SimApp.component('LocationView', LocationView);
SimApp.component('BuildingView', BuildingView);
SimApp.component('VillagerView', VillagerView);
SimApp.component('SimListView', SimListView);
SimApp.component('StatsView', StatsView);


export const SimulationApp = SimApp;