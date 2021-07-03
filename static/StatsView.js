import { StatsDataClass } from './StatsData.js';
import { ChartMaker } from './ChartMaker.js';


export const StatsView = {
    template: `<div id="stats-view">
                    <div id="stats-menu">
                            <button type="button" class="list-group-item list-group-item-success list-group-item-action" v-on:click="setCategory('World')">World</button>
                            <button type="button" class="list-group-item list-group-item-success list-group-item-action" v-on:click="setCategory('Village')">Village</button>
                            <button type="button" class="list-group-item list-group-item-success list-group-item-action" v-on:click="setCategory('Villager')">Villager</button>
                            <button type="button" class="list-group-item list-group-item-success list-group-item-action" v-on:click="setCategory('Location')">Location</button>
                            <button type="button" class="list-group-item list-group-item-success list-group-item-action" v-on:click="setCategory('Building')">Building</button>

                    </div>
                    <div id="stats-options">
                        <div class="list-group">
                            <div v-for="option in statsOptions" >
                                <button class="list-group-item list-group-item-primary list-group-item-action" type="button" v-on:click="selectChart(option)">
                                    {{option}}
                                </button>
                            </div>
                        </div>
                    </div>
                    <div id="stats-graphs">
                        <div v-show="statView==='ConfigView'">
                            <div id="sim-config">config {{runStats}}</div>
                        </div>
                        <div v-show="statView==='Chart1View'">
                            <h2>{{chartName}}</h2>
                            <div id="chart1"></div>
                        </div>                       
                    </div>
                </div>
                `,
    data() {
        return {
            simName: "",
            runName: "",
            statView: "ConfigView",
            statsOptions: ["Total Resources", "Total Villagers"],
            category: "",
            chartName: "",
            runStats: {},
            statsData: {}
        }
    },    
    methods: {
        setStatView: function(viewName){
            this.statView = viewName;
        },
        setCategory: function(category){
            this.category = category;
            this.statsOptions = this.statsData.getChartList(category);
        },
        selectChart: function(chartName){
            this.setStatView("Chart1View");
            this.chartName = chartName;
            this.drawCharts(this.category, chartName);
        },
        drawCharts: function(category, chartName){
            let h = 600;
            let w = 800;
            
            let data = this.statsData.getChartData(category, chartName);
            
            if(data.type == "line"){           
            
                ChartMaker.drawLineChart("#chart1", h, w, data.dataSet);
            }
            else if(data.type == "bar"){
                ChartMaker.drawBarChart("#chart1", h, w, data.dataSet);
            }
            else if(data.type == "stacked"){
                ChartMaker.drawHorizontalStackedBarChart("#chart1", h, w, data.dataSet);
            }
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
                this.statsData = new StatsDataClass(results)
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