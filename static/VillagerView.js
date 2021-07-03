export const VillagerView = {
    template: `<div id="edit-villagers">
                    <div id="edit-villagers-labels">
                        <label class="col-form-label">Type</label>
                        <label class="col-form-label">Speed</label>
                        <label class="col-form-label">Max Health</label>
                        <label class="col-form-label">Upgrade Cost</label>
                        <label class="col-form-label">Carry Capacity</label>
                        <label class="col-form-label">Attack</label>
                        <label class="col-form-label">Defence</label>
                        <label class="col-form-label">Production Speed</label>
                        <label class="col-form-label">Spawn Time</label>
                    </div>
                    <div id="edit-villagers-values">
                        <div v-for="(item, type) in villagerData" class="d-flex flex-column align-items-center">
                            <label class="col-form-label">{{type}}</label>
                            <input type="number" min="1" max="10" class="form-control text-center" v-model="item.speed">
                            <input type="number" min="1" max="100" class="form-control text-center" v-model="item.maxHealth">
                            <input type="number" min="1" max="1000" class="form-control text-center" v-model="item.enhancemntCost">
                            <input type="number" min="1" max="50" class="form-control text-center" v-model="item.carryCapacity">
                            <input type="number" min="1" max="10" class="form-control text-center" v-model="item.attack">
                            <input type="number" min="1" max="10" class="form-control text-center" v-model="item.defense">
                            <input type="number" min="1" max="10" class="form-control text-center" v-model="item.productionSpeed">
                            <input type="number" min="1" max="10" class="form-control text-center" v-model="item.spawnTime">
                        </div>
                    </div>
                </div>`,
    data() {
        return {
            villagerData: {'type':{'speed': 1, 'maxHealth': 100, 'enhancemntCost': 200, 'carryCapacity': 1, 'attack': 1, 'defense': 1, 'productionSpeed': 1, 'spawnTime': 1, 'spawnCost':{'wood': 60}}}
        }
    },    
    methods: {    
        loadVillagers: function(simName){
            console.log("LOAD VILLAGERS");
            let url = new URL('../getVillagers', window.location.href);
            let params = {'simName': simName};
            url.search = new URLSearchParams(params).toString();
            fetch(url)
            .then((response) => {
                if (response.ok){
                    return response.json();
                } else {
                    throw new Error("Failed to Get Sim Villagers");
                }
            })
            .then(results => { 
                this.villagerData = results;
                console.log(this.villagerData);
            })
            .catch((error) => {
              console.log(error);
            });
        },
        updateVillagers: function(simName){            
            console.log("UPDATE VILLAGERS");
            let url = new URL('../updateVillagers', window.location.href);
            let params = {'simName': simName};
            url.search = new URLSearchParams(params).toString();
            fetch(url, {
                method: 'post',
                headers: {'Content-Type' : 'application/json'},
                body: JSON.stringify(this.villagerData)})
            .then((response) => {
                if (response.ok){
                    return response.json();
                } else {
                    throw new Error("Failed to update Sim Villagers");
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