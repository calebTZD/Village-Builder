export const BuildingView = {
    template: `<div class="d-flex">
                    <div class="d-flex flex-column justify-content-between">
                        <div>Type</div>
                        <div>Max health</div>
                        <div>Time to Build</div>
                        <div>Raw Resources</div>
                        <div>Upgrade Cost</div>
                    </div>
                    <div v-for="(item, type) in buildingData" class="d-flex flex-column">
                        <h5>{{type}}</h5>
                        <input type="number" class="form-control" v-model="item.maxHealth">
                        <input type="number" class="form-control" v-model="item.buildTime">
                        <input type="number" class="form-control" v-model="item.resourceAmount">
                        <input type="number" class="form-control" v-model="item.enhancemntCost">
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