export const VillagesView = {
    template: `<div>                    
                    <div class="container">
                        <div class="row">
                            <button type="button" class="btn btn-success px-3" v-on:click="showAllVillages()" v-show="!showAll">
                                <i class="bi bi-plus-square" style="font-size: 1rem; color: white;"></i>
                            </button>
                            <button type="button" class="btn btn-success px-3" v-on:click="hideAllVillages()" v-show="showAll">
                                <i class="bi bi-minus-square" style="font-size: 1rem; color: white;">Done</i>
                            </button>
                        </div>
                        <div class="row">
                            <div class="col-md-2" v-show="showAll">
                                <div class="list-group">
                                    <button type="button" class="list-group-item list-group-item-action" v-for="villageName in allNames" v-on:click="addVillage(villageName)">
                                        {{villageName}}
                                    </button>
                                </div>
                            </div>
                            <div class="col-md-3">
                                <div class="list-group">
                                    <button type="button" class="list-group-item list-group-item-action" v-for="village in simVillages" v-on:click="setVillage(village.fixed.name)">
                                        {{village.fixed.name}}
                                        <button type="button" class="btn btn-success px-3 float-right" v-on:click="removeVillage(village.fixed.name)" >
                                            <i class="bi bi-minus-square" style="font-size: 1rem; color: white;">Done</i>
                                        </button>
                                    </button>
                                </div>
                            </div>
                            <div class="col-sm" v-if="villageData">                                
                                <label>Name: </label><input type="text" v-model="villageData.fixed.name"><br>
                                <div v-for="(value, priority) in villageData.settings.priorities">
                                    {{priority}}:  
                                <input type="number" v-model="villageData.settings.priorities[priority]">
                        </div>
                            </div>
                        </div>
                    </div>
                    {{simVillages}}
                </div>`,
    data() {
        return {
            showAll: false,
            allNames:[],
            allVillages: [],
            simVillages:[],
            villageData: null
        }
    },    
    methods: {
        showAllVillages: function(){
            this.showAll = true;
        },
        hideAllVillages: function(){
            this.showAll = false;
        },
        addVillage: function(villageName){
            this.simVillages[villageName] = this.allVillages[villageName];
            let index = this.allNames.indexOf(villageName);
            this.allNames.splice(index, 1);
        },
        setVillage: function(villageName){
            this.villageData = this.simVillages[villageName];
        },
        removeVillage: function(villageName){
            delete this.simVillages[villageName];
            this.allNames.push(villageName);
            this.villageData = null;
        },
        getData: function(){
            fetch("/getData")
            .then(response => response.json())
            .then(results => {
                this.simVillages = results.villages;
            });
            fetch("/getVillages")
            .then(response => response.json())
            .then(results => {
                this.allVillages = results;
                this.allNames = Object.keys(this.allVillages);
            });
        }
    },
    created(){
        this.getData();
    }
};