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
                    Villagers
                </div>
                <div id='locations' class="flex-fill">
                    locations
                </div>
                <div id="buildings" class="flex-fill">
                    buildings
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