export const VilligerView = {
    template: `<div v-for="(item, type) in villagerData">
                    <div>
                        <div>
                            <h5>{{type}}:</h5>
                            <label>Speed: </label><input type="number" v-model="item.settings.speed"><br>
                            <label>Max health: </label><input type="number" v-model="item.settings.maxHealth"><br>
                            <label>Upgrade Cost: </label><input type="number" v-model="item.settings.enhancemntCost"><br>
                            <label>Carry Capacity: </label><input type="number" v-model="item.settings.carryCapacity"><br>
                            <label>Attack: </label><input type="number" v-model="item.settings.attack"><br>
                            <label>Defence Cost: </label><input type="number" v-model="item.settings.defense"><br>
                            <label>Production Speed: </label><input type="number" v-model="item.settings.productionSpeed"><br>
                            <label>Spawn Time: </label><input type="number" v-model="item.settings.spawnTime">
                        </div>
                        <h6> Spawn Cost: </h6>
                        <div v-for="(cost, typea) in item.settings.spawnCost">
                            {{typea}}:  
                            <input type="number" v-model="item.settings.spawnCost[typea]">
                        </div>
                    </div>
                    <br>
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