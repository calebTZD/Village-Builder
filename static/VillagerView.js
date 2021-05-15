export const VilligerView = {
    template: `<div class="d-flex">
                    <div class="d-flex flex-column justify-content-between">
                        <div>Type</div>
                        <div>Speed</div>
                        <div>Max Health</div>
                        <div>Upgrade Cost</div>
                        <div>Carry Capacity</div>
                        <div>Attack</div>
                        <div>Defence</div>
                        <div>Production Speed</div>
                        <div>Spawn Time</div>
                    </div>
                    <div v-for="(item, type) in villagerData" class="d-flex flex-column">
                            <h5>{{type}}</h5>
                            <div><input type="number" class="form-control" v-model="item.settings.speed"></div>
                            <div><input type="number" class="form-control" v-model="item.settings.maxHealth"></div>
                            <div><input type="number" class="form-control" v-model="item.settings.enhancemntCost"></div>
                            <div><input type="number" class="form-control" v-model="item.settings.carryCapacity"></div>
                            <div><input type="number" class="form-control" v-model="item.settings.attack"></div>
                            <div><input type="number" class="form-control" v-model="item.settings.defense"></div>
                            <div><input type="number" class="form-control" v-model="item.settings.productionSpeed"></div>
                            <div><input type="number" class="form-control" v-model="item.settings.spawnTime"></div>

                    </div>
                </div>`,
    data() {
        return {
            villagerData: {'type':{'settings':{'speed': 1, 'maxHealth': 100, 'enhancemntCost': 200, 'carryCapacity': 1, 'attack': 1, 'defense': 1, 'productionSpeed': 1, 'spawnTime': 1, 'spawnCost':{'wood': 60}}}}
        }
    },    
    methods: {    
        getData: function(){
            fetch("/getData")
            .then(response => response.json())
            .then(results => {
                this.villagerData = results.villagers;

            })
        }
    },
    created(){
        this.getData();
    }
};