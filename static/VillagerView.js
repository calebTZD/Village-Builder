export const VilligerView = {
    template: `<div class="d-flex width flex-fill">
                    <div class="d-flex flex-column justify-content-between ">
                        <div class="flex-fill">Type</div>
                        <div class="flex-fill">Speed</div>
                        <div class="flex-fill">Max Health</div>
                        <div class="flex-fill">Upgrade Cost</div>
                        <div class="flex-fill">Carry Capacity</div>
                        <div class="flex-fill"> Attack</div>
                        <div class="flex-fill">Defence</div>
                        <div class="flex-fill">Production Speed</div>
                        <div class="flex-fill">Spawn Time</div>
                    </div>
                    <div v-for="(item, type) in villagerData" class="d-flex flex-column justify-content-around ">
                            <div class="flex-fill ">{{type}}</div>
                            <div><input type="number" class="form-control flex-fill" v-model="item.settings.speed"></div>
                            <div><input type="number" class="form-control flex-fill" v-model="item.settings.maxHealth"></div>
                            <div><input type="number" class="form-control flex-fill" v-model="item.settings.enhancemntCost"></div>
                            <div><input type="number" class="form-control flex-fill" v-model="item.settings.carryCapacity"></div>
                            <div><input type="number" class="form-control flex-fill" v-model="item.settings.attack"></div>
                            <div><input type="number" class="form-control flex-fill" v-model="item.settings.defense"></div>
                            <div><input type="number" class="form-control flex-fill" v-model="item.settings.productionSpeed"></div>
                            <div><input type="number" class="form-control flex-fill" v-model="item.settings.spawnTime"></div>

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