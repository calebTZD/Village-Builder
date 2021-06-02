export const SimListView = {
    template: `
                <div class="d-flex flex-column">
                    <h4>Simulations</h4>
                    <div class="d-flex">                        
                            <div class="flex-fill">
                                <div class="d-flex flex-column">
                                    <label>Create</label>
                                    <input v-model="createName">                            
                                    <i class="bi bi bi-plus-square" style="font-size: 1rem; color: blue;" v-on:click="createSimulation()"></i>
                                    <div class="list-group">
                                        <div v-for="sim in simulations" >
                                            <button class="list-group-item list-group-item-action" type="button" v-on:click="selectSimulation(sim)">
                                                {{sim}}
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>                                               
                            <div class="flex-fill" v-if="simulation">
                                <h4>{{simulation}}</h4>
                                <div class="d-flex flex-column">
                                    <button type="button" v-on:click="deleteSimulation()">
                                        Delete
                                    </button>                                    
                                    <button type="button" v-on:click="editSimulation()">
                                        Edit
                                    </button>
                                    <button type="button" v-on:click="runSimulation()">
                                        Run Simulation ({{simState}})
                                    </button>
                                    <button type="button" v-on:click="viewSimulation()" v-if="simComplete">
                                        View Results
                                    </button>
                                </div>
                            </div>
                        </div>
                </div>`,
    data() {
        return {
            simulations: [],
            createName: "",
            simulation: null,
            simState: "",
            simComplete: false          
        }
    },    
    methods: {
        createSimulation: function(){
            console.log("Create: " + this.createName);
            let url = new URL('../createSim', window.location.href);
            let params = {'simName': this.createName};
            url.search = new URLSearchParams(params).toString();
            fetch(url)
            .then(response => response.json())
            .then(results => {
                this.loadSimulations();
                this.selectSimulation(this.createName);
            });
        },
        deleteSimulation: function(){
            console.log("Delete: " + this.simulation);
            let url = new URL('../deleteSim', window.location.href);
            let params = {'simName': this.simulation};
            url.search = new URLSearchParams(params).toString();
            fetch(url)
            .then(response => response.json())
            .then(results => {
                this.createName = "";
                this.simulation = null;
                this.simState = "";
                this.simComplete = false;;
                this.loadSimulations();
            });
        },
        selectSimulation: function(sim){
            console.log("Select: " + sim);
            let url = new URL('../getSimStatus', window.location.href);
            let params = {'simName': sim};
            url.search = new URLSearchParams(params).toString();
            fetch(url)
            .then(response => response.json())
            .then(results => {
                this.simState = results.state;
                if (this.simState == "complete"){
                    this.simComplete = true;
                } else {
                    this.simComplete = false;
                }
                this.simulation = sim;
            });
        },
        editSimulation: function(){
            this.$emit('edit', this.simulation);
        },
        loadSimulations: function(){
            fetch("/getSims")
            .then(response => response.json())
            .then(results => {
                this.simulations = results;
            });
        }
    },
    created(){
        this.loadSimulations();
    }
};