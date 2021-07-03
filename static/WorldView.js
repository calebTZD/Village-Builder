export const WorldView = {
    template: `<div id="edit-world">
                    <div id="edit-world-labels">
                        <h5>Settings</h5>
                        <label class="col-form-label">Days to Run: </label>
                        <label class="col-form-label">Distance Between Villages: </label>
                        <label class="col-form-label">Villeger Maximum: </label>
                        <label class="col-form-label">Building Maximum: </label>
                    </div>
                    <div id="edit-world-values">
                        <h5>:</h5>
                        <input type="number" min="1" max="1000" class="form-control" v-model="worldData.days">
                        <input type="number" min="1" max="100" class="form-control" v-model="worldData.distanceBetweenVillages">
                        <input type="number" min="1" max="50" class="form-control" v-model="worldData.maxVillagersPerVillage">
                        <input type="number" min="1" max="100" class="form-control" v-model="worldData.maxBuildingsPerVillage">
                    </div>
                    <div id="edit-world-villagers">
                        <h5>Starting Villagers</h5>
                        <div class="form-group">
                            <div v-for="villager in villagers">
                                <input type="checkbox" v-bind:id="villager" v-bind:value="villager" v-model="worldData.startingVillagers">
                                <label v-bind:for="villager"> {{villager}} </label>
                            </div>
                        </div>
                    </div>
                </div>`,
    data() {
        return {
            villagers: ["Farmer", "Lumberjack", "Stonemason", "Miner", "Warrior", "Guard", "DrX", "Merchant", "Researcher", "Scout"],
            worldData: {'days':1, 'maxVillagersPerVillage': 1, 'maxBuildingsPerVillage': 1, 'startingVillagers': []}
        }
    },    
    methods: {       
        loadWorld: function(simName){
            console.log("LOAD WORLD");
            let url = new URL('../getWorld', window.location.href);
            let params = {'simName': simName};
            url.search = new URLSearchParams(params).toString();
            fetch(url)
            .then((response) => {
                if (response.ok){
                    return response.json();
                } else {
                    throw new Error("Failed to Get Sim World");
                }
            })
            .then(results => { 
                this.worldData = results;
                console.log(this.worldData);
            })
            .catch((error) => {
              console.log(error);
            });
        },
        updateWorld: function(simName){            
            console.log("UPDATE WORLD");
            let url = new URL('../updateWorld', window.location.href);
            let params = {'simName': simName};
            url.search = new URLSearchParams(params).toString();
            fetch(url, {
                method: 'post',
                headers: {'Content-Type' : 'application/json'},
                body: JSON.stringify(this.worldData)})
            .then((response) => {
                if (response.ok){
                    return response.json();
                } else {
                    throw new Error("Failed to Update Sim World");
                }
            })
            .then(results => { 
                let r = results;
            })
            .catch((error) => {
              console.log(error);
            });
        }
    },
    created(){
    }
  };