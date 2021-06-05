export const SimulationView = {
    template: 
    `<div>
        <div class="flex-column" v-show="showList">              
            <div id="simlist" class="flex-fill">                
                <SimListView ref="simlist" @edit="onEdit"></SimListView>
            </div>
        </div> 
        <div v-show="showEdit">
            <div class="d-flex flex-column" >
                <h4>{{simName}}</h4>
                <div v-on:click="update()">UPDATE</div>
                <div class="d-flex">
                    <div id="sim" class="flex-fill">                
                        <WorldView ref="world"></WorldView>
                    </div>
                    <div id="villages" class="flex-fill">                  
                        <VillagesView ref="villages"></VillagesView>  
                    </div>
                </div>            
                <div id="villagers" class="flex-fill">
                    <h4> Villager Settings: </h4><br>
                    <VilligerView ref="villagers"></VilligerView>
                </div>
                <div id='locations' class="flex-fill">
                    <h4> Location Settings: </h4><br>
                    <LocationView ref="locations"></LocationView>
                </div>
                <div id="buildings" class="flex-fill">
                    <h4> building Settings: </h4><br>
                    <BuildingView ref="buildings"></BuildingView>
                </div>            
            </div>
        </div>
    </div>
    `,
    data() {
      return {
        simName: "The Myst",
        simData: {},
        showEdit: false,
        showList: true
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
        load: function(){
            console.log("LOAD");
            this.$refs.world.loadWorld(this.simName);
            this.$refs.villages.loadVillages(this.simName);
            this.$refs.villagers.loadVillagers(this.simName);
            this.$refs.locations.loadLocations(this.simName);
            this.$refs.buildings.loadBuildings(this.simName);
        },      
        update: function(){
            console.log("UPDATE");
            this.$refs.world.updateWorld(this.simName);
            this.$refs.villages.updateVillages(this.simName);
            this.$refs.villagers.updateVillagers(this.simName);
            this.$refs.locations.updateLocations(this.simName);
            this.$refs.buildings.updateBuildings(this.simName);
            this.showList = true;
            this.showEdit = false;
        }
    },
    mounted(){
    }
  }  