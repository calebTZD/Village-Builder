export const SimulationView = {
    template: 
    `<div id="sim-main">
        <div id="banner">
            <h2>RPG Simulation</h2>
        </div>
        <div v-show="showList">
            <SimListView ref="simlist" @edit="onEdit" @view="onView"></SimListView>
        </div> 
        <div v-show="showEdit" id="edit-pane">   
            <div id="edit-banner">            
                <h4 class="flex-row-gap">Editing: {{simName}}</h4>    
                <button type="button" class="btn btn-primary flex-row-gap" v-on:click="done()">Done</button>
                <button type="button" class="btn btn-success flex-row-gap" v-on:click="update()">Update</button>   
            </div>
            <div id="edit-menu">
                <div class="list-group">
                    <button type="button" class="list-group-item list-group-item-primary list-group-item-action" v-on:click="setEdit('WorldView')">World</button>
                    <button type="button" class="list-group-item list-group-item-primary list-group-item-action" v-on:click="setEdit('VillagesView')">Village</button>
                    <button type="button" class="list-group-item list-group-item-primary list-group-item-action" v-on:click="setEdit('VillagerView')">Villagers</button>
                    <button type="button" class="list-group-item list-group-item-primary list-group-item-action" v-on:click="setEdit('LocationView')">Locations</button>
                    <button type="button" class="list-group-item list-group-item-primary list-group-item-action" v-on:click="setEdit('BuildingView')">Buildings</button>
                </div>
            </div>
            <div id="edit-simulation">
                <div v-show="editView==='WorldView'">
                    <WorldView ref="world" ></WorldView>
                </div>
                <div v-show="editView==='VillagesView'">
                    <VillagesView ref="villages"></VillagesView> 
                </div> 
                <div v-show="editView==='VillagerView'">
                    <VillagerView ref="villagers"></VillagerView>
                </div>
                <div v-show="editView==='LocationView'">
                    <LocationView ref="locations"></LocationView>
                </div>
                <div v-show="editView==='BuildingView'">
                    <BuildingView ref="buildings"></BuildingView>
                </div>
            </div>
        </div>

        <div v-show="showStats" id="stats-pane">   
            <div id="stats-banner">            
                <h4 class="flex-row-gap">Simulation Results: {{simName}} : {{runName}}</h4>    
                <button type="button" class="btn btn-primary flex-row-gap" v-on:click="finishedView()">Done</button>   
            </div>
            <div id="stats-run-list">
                <div class="list-group">
                    <div v-for="run in simulationRuns" >
                        <button class="list-group-item list-group-item-primary list-group-item-action" type="button" v-on:click="selectRun(run)">
                            {{run.timeStamp}}
                        </button>
                    </div>
                </div>
            </div>
            <div id="stats-simulation">
                <StatsView ref="stats" ></StatsView>
            </div>
        </div>
    </div>
    `,
    data() {
      return {
        simName: "",
        runName: "",
        simData: {},
        showEdit: false,
        showStats: false,
        showList: true,
        editView: "WorldView",
        simulationRuns: ['asdfasda', 'basdlf']
      }
    },
    methods: {
        onEdit: function(simName){
            console.log("EDIT EVENT: " + simName);
            this.simName = simName;
            this.showList = false;
            this.showEdit = true;
            this.load();
        },
        onView: function(simName){
            console.log("VIEW EVENT: " + simName);
            this.simName = simName;
            this.showList = false;
            this.showStats = true;
            this.load();
        },
        setEdit: function(view){
            this.editView = view;
        },
        finishedView: function(){
            this.showList = true;
            this.showStats = false;      
        },
        done: function(){
            this.showList = true;
            this.showEdit = false;          
        },
        selectRun: function(run){
            console.log("LOAD Simulation Stats");
            this.runName = run["timeStamp"];
            this.$refs.stats.loadStats(this.simName, this.runName);
        },
        load: function(){
            console.log("LOAD");
            this.$refs.world.loadWorld(this.simName);
            this.$refs.villages.loadVillages(this.simName);
            this.$refs.villagers.loadVillagers(this.simName);
            this.$refs.locations.loadLocations(this.simName);
            this.$refs.buildings.loadBuildings(this.simName);
            this.loadSimRuns(this.simName)
        },      
        update: function(){
            console.log("UPDATE");
            this.$refs.world.updateWorld(this.simName);
            this.$refs.villages.updateVillages(this.simName);
            this.$refs.villagers.updateVillagers(this.simName);
            this.$refs.locations.updateLocations(this.simName);
            this.$refs.buildings.updateBuildings(this.simName);
        },
        loadSimRuns: function(simName){
            console.log("LOAD Sim Runs");
            let url = new URL('../getSimRuns', window.location.href);
            let params = {'simName': simName};
            url.search = new URLSearchParams(params).toString();
            fetch(url)
            .then((response) => {
                if (response.ok){
                    return response.json();
                } else {
                    throw new Error("Failed to Get Sim");
                }
            })
            .then(results => { 
                this.simulationRuns = results;
                console.log(this.simulationRuns);
            })
            .catch((error) => {
              console.log(error);
            });
        }        
    },
    mounted(){
    }
  }  