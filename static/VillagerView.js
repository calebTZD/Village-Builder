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
                            <div><input type="number" class="form-control" v-model="item.speed"></div>
                            <div><input type="number" class="form-control" v-model="item.maxHealth"></div>
                            <div><input type="number" class="form-control" v-model="item.enhancemntCost"></div>
                            <div><input type="number" class="form-control" v-model="item.carryCapacity"></div>
                            <div><input type="number" class="form-control" v-model="item.attack"></div>
                            <div><input type="number" class="form-control" v-model="item.defense"></div>
                            <div><input type="number" class="form-control" v-model="item.productionSpeed"></div>
                            <div><input type="number" class="form-control" v-model="item.spawnTime"></div>

                    </div>
                </div>`,
    data() {
        return {
            villagerData: {'type':{'speed': 1, 'maxHealth': 100, 'enhancemntCost': 200, 'carryCapacity': 1, 'attack': 1, 'defense': 1, 'productionSpeed': 1, 'spawnTime': 1, 'spawnCost':{'wood': 60}}}
        }
    },    
    methods: {    
        getData: function(){
            fetch("/getData")
            .then(response => response.json())
            .then(results => {
                this.villagerData = results.villagers;

            })
        },     
        loadVillagers: function(simName){
            console.log("LOAD VILLAGERS");
            let url = new URL('../getVillagers', window.location.href);
            let params = {'simName': simName};
            url.search = new URLSearchParams(params).toString();
            fetch(url)
            .then(response => response.json())
            .then(results => { 
                this.villagerData = results;
                console.log(this.villagerData);
            })
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
            .then(response => response.json())
            .then(results => { 
                let r = results;
            })
        }
    },
    created(){
    }
};