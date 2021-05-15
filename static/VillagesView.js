export const VillagesView = {
    template: `
                <div class="d-flex flex-column">
                    <h4>Villages</h4>
                    <div class="d-flex">
                        <div class="flex-column">                            
                            <i class="bi bi bi-plus-square" style="font-size: 1rem; color: blue;" v-on:click="showAllVillages()" v-show="!showAll"></i>
                            <i class="bi bi-chevron-double-left" style="font-size: 1rem; color: blue;" v-on:click="hideAllVillages()" v-show="showAll"></i>
                        </div>                    
                        <div class="flex-column" v-show="showAll">
                            <div class="list-group">
                                <div v-for="village in allVillages" >
                                    <button class="list-group-item list-group-item-action" type="button" v-if="isNotInSim(village)" v-on:click="addVillage(village)">
                                        {{village.fixed.name}}(Sim1)
                                    </button>
                                </div>
                            </div>
                        </div>
                        <div class="flex-column">
                            <div class="list-group">
                                <button type="button" class="list-group-item list-group-item-action" v-for="village in simVillages" v-on:click="setVillage(village)">
                                    {{village.fixed.name}}
                                    <i class="bi bi-x-square  float-right" style="font-size: 1rem; color: red;" v-on:click.stop="removeVillage(village)" ></i>
                                </button>
                            </div>
                        </div>
                        <div class="flex-column" v-if="villageData" :key="villageData">                                
                            <label>Name: </label><input type="text" v-model="villageData.fixed.name"><br>
                            <div v-for="(value, priority) in villageData.settings.priorities">
                                {{priority}}:  
                                <input type="number" v-model="villageData.settings.priorities[priority]">
                            </div>
                        </div>
                        <div class="flex-column" v-else> 
                            <p>No Village Selected</p> 
                        </div
                    </div>
                </div>`,
    data() {
        return {
            showAll: false,
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
        isNotInSim: function(village){
            let index = this.simVillages.indexOf(village);
            return (index === -1);
        },
        addVillage: function(village){
            let index = this.simVillages.indexOf(village);
            if (index === -1){
                this.simVillages.push(village);
            }
        },
        setVillage: function(village){
            this.villageData = village;
        },
        removeVillage: function(village){
            if (village === this.villageData){
                this.villageData = null;
            }
            let index = this.simVillages.indexOf(village);
            this.simVillages.splice(index, 1);
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
            });
        }
    },
    created(){
        this.getData();
    }
};