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
        getData: function(){
            fetch("/getData")
            .then(response => response.json())
            .then(results => {
                this.buildingData = results.buildings;

            })
        }
    },
    created(){
        this.getData();
    }
};