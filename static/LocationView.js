export const LocationView = {
    template: `<div id="edit-locations">
                    <div id="edit-locations-labels">
                        <label class="col-form-label">Type</label>
                        <label class="col-form-label">Amount per Village</label>
                        <label class="col-form-label">Average Distance</label>
                        <label class="col-form-label">Upgrade Cost</label>
                    </div>
                    <div id="edit-locations-values">
                        <div v-for="(item, type) in locationData" class="d-flex flex-column align-items-center">
                            <label class="col-form-label">{{type}}</label>
                            <input type="number" class="form-control text-center" v-model="item.numPerVillage" v-if="type==='Village'" readonly>
                            <input type="number" min="1" max="100" class="form-control text-center" v-model="item.numPerVillage" v-else>
                            <input type="number" class="form-control text-center" v-model="item.aveDistance" v-if="type==='Village'" readonly>
                            <input type="number" min="1" max="100" class="form-control text-center" v-model="item.aveDistance" v-else>
                            <input type="number" min="1" max="1000" class="form-control text-center" v-model="item.enhancemntCost">
                        </div>
                    </div>
                </div>`,
    data() {
        return {
            locationData: {'type':{'name': "",'numPerVillage': 1, 'aveDistance': 1, 'enhancemntCost': 200}}
        }
    },    
    methods: {    
        loadLocations: function(simName){
            console.log("LOAD LOCATIONS");
            let url = new URL('../getLocations', window.location.href);
            let params = {'simName': simName};
            url.search = new URLSearchParams(params).toString();
            fetch(url)
            .then((response) => {
                if (response.ok){
                    return response.json();
                } else {
                    throw new Error("Failed to Get Sim Locations");
                }
            })
            .then(results => { 
                this.locationData = results;
                console.log(this.locationData);
            })
            .catch((error) => {
              console.log(error);
            });
        },
        updateLocations: function(simName){            
            console.log("UPDATE LOCATIONS");
            let url = new URL('../updateLocations', window.location.href);
            let params = {'simName': simName};
            url.search = new URLSearchParams(params).toString();
            fetch(url, {
                method: 'post',
                headers: {'Content-Type' : 'application/json'},
                body: JSON.stringify(this.locationData)})
            .then((response) => {
                if (response.ok){
                    return response.json();
                } else {
                    throw new Error("Failed to Update Sim Locations");
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