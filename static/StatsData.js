export class StatsDataClass {
    constructor(data){
        this.name = data.name;
        this.config = data.config;
        this.ticks = data.ticks;
        this.tickData = data.tickStats;
        this.worldData = data.world;

        this.stats = {
            'Village': {}
        };

        this.init();
    }

    init() {
        this.initVillagesData();
        console.log(this.getChartList('Village'));
        console.log(this.getChartData('Village', 'Total Villagers'));
        console.log(this.getChartData('Village', 'Food'));
    }

    getChartList(catagory){
        return Object.keys(this.stats[catagory]);
    }
    getChartData(catagory, chartName){
        return this.stats[catagory][chartName];
    }

    //****************************** Villages *******************************/
    initVillagesData() {
        this.initVillagesNumVillagers();
        this.initVillagesFood();
    }

    initVillagesNumVillagers(){
        let dataSet = [];
        for(let v of this.worldData.villages){  
            this.addBarDatum(dataSet, v.name, v.villagers.length);
        }
        this.stats['Village']['Total Villagers'] = {'type': 'bar', 'dataSet': dataSet};
    }

    initVillagesFood(){
        let dataSet = [];
        for(let v of this.worldData.villages){
            this.addLineData(dataSet, v.name, v.tickStats.resources.Food);
        }
        this.stats['Village']['Food'] = {'type': 'line', 'dataSet': dataSet};
    }

    //****************************** Villagers *******************************/
    //****************************** Buildings *******************************/
    //****************************** Locations *******************************/
    //****************************** World  *******************************/
    addBarDatum(dataSet, label, value){
        dataSet.push({label: label, value: value});
    }

    addLineData(dataSet, key, values){
        let lineValues = [];
        for (let tick=0; tick < values.length; tick++){
            lineValues.push({'tick': tick, 'value': values[tick]});
        }
        dataSet.push({"key": key, "values": lineValues});
        //EXAMPLE:
        //[{key: "Brad", values: [{tick:1,value:1},{tick:2,value:2},{tick:3,value:2},{tick:4,value:2},{tick:5,value:2}]},
        // {key: "Caleb", values: [{tick:1,value:1},{tick:2,value:5},{tick:3,value:7},{tick:4,value:3},{tick:5,value:2}]}];
    }
}