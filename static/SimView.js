export const SimulationView = {
    template: 
    `<div>
        <div class="flex-column">              
            <div v-on:click="load()">LOAD</div>              
            <div v-on:click="update()">UPDATE</div>
        </div>                  
        <div class="d-flex flex-column">
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
                <VilligerView></VilligerView>
            </div>
            <div id='locations' class="flex-fill">
                <h4> Location Settings: </h4><br>
                <LocationView></LocationView>
            </div>
            <div id="buildings" class="flex-fill">
                <h4> building Settings: </h4><br>
                <BuildingView></BuildingView>
            </div>
            
        </div>
    </div>
    `,
    data() {
      return {
        simData: {}
      }
    },
    methods: {      
        load: function(){
            console.log("LOAD");
            this.$refs.world.loadWorld("The Myst");
            this.$refs.villages.loadVillages("The Myst");
        },      
        update: function(){
            console.log("UPDATE");
            this.$refs.world.updateWorld("The Myst");
            this.$refs.villages.updateVillages("The Myst");
        },
        getData: function(){
            fetch("/getData")
            .then(response => response.json())
            .then(results => {
                this.simData = results;
            })
        }
    },
    mount(){
        this.getData();
    }
  }  