export const SimulationView = {
    template: 
    `<div>                    
        <div class="d-flex flex-column">
            <div class="d-flex">
                <div id="sim" class="flex-fill">                
                    <WorldView></WorldView>
                </div>
                <div id="villages" class="flex-fill">                  
                    <VillagesView></VillagesView>  
                </div>
            </div>
            <div class="d-flex">
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
    </div>
    `,
    data() {
      return {
        simData: {}
      }
    },
    methods: {      
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