export const BuildingView = {
    template: `<div v-for="(item, type) in buildingData">
                    <h5>{{type}}:</h5>
                    Max health: <input type="number" v-model="item.settings.maxHealth"><br>
                    Time to Build: <input type="number" v-model="item.settings.buildTime"><br>
                    Starting Amount of Resources: <input type="number" v-model="item.settings.resourceAmount"><br>
                    Upgrade Cost: <input type="number" v-model="item.settings.enhancemntCost">
                    <br><br>
                </div>`,
    data() {
        return {
            buildingData: {'type': {'settings':{'maxHealth': 100, 'buildTime': 9, 'resourceAmount': 2000, 'enhancemntCost': 200}}}
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