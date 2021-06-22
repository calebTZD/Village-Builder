import { ChartMaker } from './ChartMaker.js';

export const StatsView = {
    template: `<div id="stats-view">
                    <div id="stats-menu">
                        <div class="list-group">
                            <button type="button" class="list-group-item list-group-item-success list-group-item-action" v-on:click="setStatView('ConfigView')">Config</button>
                            <button type="button" class="list-group-item list-group-item-success list-group-item-action" v-on:click="setStatView('Chart1View')">Chart1View</button>
                            <button type="button" class="list-group-item list-group-item-success list-group-item-action" v-on:click="setStatView('Chart2View')">Chart2View</button>
                        </div>
                    </div>
                    <div id="stats-graphs">
                        <div v-show="statView==='ConfigView'">
                            <div id="sim-config">config {{runStats}}</div>
                        </div>
                        <div v-show="statView==='Chart1View'">
                            <H2>Chart 1</H2>
                            <div id="chart1"></div>
                        </div> 
                        <div v-show="statView==='Chart2View'">
                            <H2>Chart 2</H2>
                            <div id="chart2"></div>
                        </div>                         
                    </div>
                </div>
                `,
    data() {
        return {
            simName: "",
            runName: "",
            statView: "ConfigView",
            runStats: {}
        }
    },    
    methods: {
        setStatView: function(viewName){
            this.statView = viewName;
        },
        drawCharts: function(){
            let h = 600;
            let w = 800;
            let data = [{label: 'Rock', value: 5},
                        {label: 'Bacon', value: 10},
                        {label: 'Asteroid', value: 17},
                        {label: 'Launch', value: 29},
                        {label: 'Sword', value: 21}];
            self.runStats.world.Villages.foreach(function(item, index){
                data.push({label: index, value: item.score})
            })
            ChartMaker.drawBarChart("#chart1", h, w, data);
            data = [{label: 'Legolas', value: 15},
                        {label: 'Gimli', value: 8},
                        {label: 'Gandalf', value: 90},
                        {label: 'Frodo', value: 6},
                        {label: 'Elron', value: 25}];
            //ChartMaker.drawBarChart("#chart2", h, w, data);
            ChartMaker.drawLineChart("#chart2", h, w, data);
        },
        loadStats: function(simName, runName){
            
            console.log("LOAD STATS");
            this.runName = runName;
            this.simName = simName;
            let url = new URL('../getSimRun', window.location.href);
            let params = {'simName': simName, 'simRun': runName};
            url.search = new URLSearchParams(params).toString();
            fetch(url)
            .then((response) => {
                if (response.ok){
                    return response.json();
                } else {
                    throw new Error("Failed to Get Run Stats");
                }
            })
            .then(results => { 
                this.runStats = results;
                this.drawCharts();
                console.log(this.runStats);
            })
            .catch((error) => {
              console.log(error);
            });
        }
    },
    created(){
    }
  };