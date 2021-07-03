export const BuildingView = {
    template: `<div id="edit-buildings">
                    <div id="edit-buildings-labels">
                        <label class="col-form-label">Type</label>
                        <label class="col-form-label">Max health</label>
                        <label class="col-form-label">Time to Build</label>
                        <label class="col-form-label">Raw Resources</label>
                        <label class="col-form-label">Upgrade Cost</label>
                    </div>
                    <div id="edit-buildings-values">
                        <div v-for="(item, type) in buildingData" class="d-flex flex-column align-items-center">
                            <label class="col-form-label">{{type}}</label>
                            <input type="number" min="1" max="100" class="form-control text-center" v-model="item.maxHealth">
                            <input type="number" min="1" max="50" class="form-control text-center" v-model="item.buildTime">
                            <input type="number" min="1000" max="100000" class="form-control text-center" v-model="item.resourceAmount">
                            <input type="number" min="1" max="10000" class="form-control text-center" v-model="item.enhancemntCost">
                        </div>
                    </div>
                </div>`,
    data() {
        return {
            buildingData: {'type': {'maxHealth': 100, 'buildTime': 9, 'resourceAmount': 2000, 'enhancemntCost': 200}}
        }
    },    
    methods: {     
        loadBuildings: function(simName){
            console.log("LOAD BUILDINGS");
            let url = new URL('../getBuildings', window.location.href);
            let params = {'simName': simName};
            url.search = new URLSearchParams(params).toString();
            fetch(url)
            .then((response) => {
                if (response.ok){
                    return response.json();
                } else {
                    throw new Error("Failed to Get Sim Buildings");
                }
            })
            .then(results => { 
                this.buildingData = results;
                console.log(this.buildingData);
            })
            .catch((error) => {
              console.log(error);
            });
        },
        updateBuildings: function(simName){            
            console.log("UPDATE BUILDINGS");
            let url = new URL('../updateBuildings', window.location.href);
            let params = {'simName': simName};
            url.search = new URLSearchParams(params).toString();
            fetch(url, {
                method: 'post',
                headers: {'Content-Type' : 'application/json'},
                body: JSON.stringify(this.buildingData)})
            
            .then((response) => {
                if (response.ok){
                    return response.json();
                } else {
                    throw new Error("Failed to Update Sim Buildings");
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