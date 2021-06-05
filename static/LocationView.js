export const LocationView = {
    template: `<div class="d-flex">
                    <div class="d-flex flex-column justify-content-between">
                        <div>Type</div>
                        <div>Amount per Village</div>
                        <div>Average Distance</div>
                        <div>Upgrade Cost</div>
                    </div>
                    <div v-for="(item, type) in locationData" class="d-flex flex-column">
                        <h5>{{type}}</h5>
                        <input type="number" class="form-control" v-model="item.numPerVillage">
                        <input type="number" class="form-control" v-model="item.aveDistance">
                        <input type="number" class="form-control" v-model="item.enhancemntCost">
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