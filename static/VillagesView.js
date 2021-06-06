export const VillagesView = {
    template: `
                <div id="edit-villages">
                    <div id="edit-villages-icons">                           
                            <i class="bi bi bi-plus-square" style="font-size: 1rem; color: blue;" v-on:click="showAllVillages()" v-show="!showAll"></i>
                    </div> 
                    <div v-if="showAll">                   
                        <div id="edit-villages-list">
                            <div class="list-group">
                                <div v-for="village in allVillages">
                                    <button class="list-group-item list-group-item-action" type="button" v-if="isNotInSim(village)" v-on:click="addVillage(village)">
                                        {{village.name}}({{village.simulationName}})
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div v-else>
                        <div id="edit-villages-list">
                            <div class="list-group">
                                <button type="button" class="list-group-item list-group-item-action" v-for="village in simVillages" v-on:click="setVillage(village)">
                                    {{village.name}}
                                    <i class="bi bi-x-square  float-right" style="font-size: 1rem; color: red;" v-on:click.stop="removeVillage(village)" ></i>
                                </button>
                            </div>
                        </div>
                    </div>
                    <div id="edit-villages-data" class="form-group" v-if="villageData">
                        <div class="form-group row">
                            <label class="col-sm-2 col-form-label">Name: </label>
                            <input class="form-control col-sm-2" type="text" v-model="villageData.name"><br>
                        </div>
                        <div v-for="(value, priority) in villageData.priorities">
                            <div class="form-group row">
                                <label class="col-sm-2 col-form-label">{{priority}}: </label>  
                                <input type="number" class="form-control col-sm-2" v-model="villageData.priorities[priority]">
                            </div>
                        </div>
                    </div>
                    <div id="edit-villages-data" v-else> 
                        <p>No Village Selected</p> 
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
        isNotInSim: function(village){
            let found = this.simVillages.find(e => e["name"] == village["name"]);
            return (!found);
        },
        addVillage: function(village){
            let found = this.simVillages.find(e => e["name"] == village["name"]);
            if (!found){
                this.simVillages.push(village);
            }
            this.showAll = false;
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
        loadVillages: function(simName){
            console.log("LOAD VILLAGES");

            fetch("/getAllVillages")
            .then((response) => {
                if (response.ok){
                    return response.json();
                } else {
                    throw new Error("Failed to Get All Villages");
                }
            })
            .then(results => {
                this.allVillages = results;
            })
            .catch((error) => {
              console.log(error);
            });

            let url = new URL('../getVillages', window.location.href);
            let params = {'simName': simName};
            url.search = new URLSearchParams(params).toString();
            fetch(url)
            .then((response) => {
                if (response.ok){
                    return response.json();
                } else {
                    throw new Error("Failed to Get Sim Villages");
                }
            })
            .then(results => { 
                this.simVillages = results;
                console.log(this.simVillages);
            })
            .catch((error) => {
              console.log(error);
            });
        },
        updateVillages: function(simName){            
            console.log("UPDATE VILLAGES");
            let url = new URL('../updateVillages', window.location.href);
            let params = {'simName': simName};
            url.search = new URLSearchParams(params).toString();
            fetch(url, {
                method: 'post',
                headers: {'Content-Type' : 'application/json'},
                body: JSON.stringify(this.simVillages)})
            .then((response) => {
                if (response.ok){
                    return response.json();
                } else {
                    throw new Error("Failed to Update Sim Villages");
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