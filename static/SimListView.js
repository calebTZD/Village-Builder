export const SimListView = {
    template: `
                <div id="sim-list-pane" >
                    <div id="sim-list-items">
                        <div class="input-group mb-3">
                            <input type="text" class="form-control" placeholder="New Simulation Name"  v-model="createName" v-on:keyup.enter="createSimulation()">
                            <div class="input-group-append">
                                <button class="btn btn-outline-secondary" type="button" v-on:click="createSimulation()">Create</button>
                            </div>
                        </div>
                        <div class="list-group">
                            <div v-for="sim in simulations" >
                                <button class="list-group-item list-group-item-primary list-group-item-action" type="button" v-on:click="selectSimulation(sim)">
                                    {{sim}}
                                </button>
                            </div>
                        </div>
                    </div>                                               
                    <div id="sim-list-options" v-if="simulation!==null">
                        <h4>{{simulation}}</h4>
                        <button type="button" class="btn btn-primary" v-on:click="deleteSimulation()">
                            Delete
                        </button>                                    
                        <button type="button" class="btn btn-primary" v-on:click="editSimulation()">
                            Edit
                        </button>
                        <button type="button" class="btn btn-primary"  v-on:click="runSimulation()">
                            Run Simulation ({{simState}})
                        </button>
                        <button type="button" class="btn btn-primary"  v-on:click="viewSimulation()" v-if="simComplete2">
                            View Results
                        </button>
                    </div>
                </div>`,
    data() {
        return {
            simulations: [],
            createName: "",
            simulation: null,
            simState: "",
            simComplete: false,
            simComplete2: true      
        }
    },    
    methods: {
        createSimulation: function(){
            console.log("Create: " + this.createName);
            let url = new URL('../createSim', window.location.href);
            let params = {'simName': this.createName};
            url.search = new URLSearchParams(params).toString();
            fetch(url)
            .then((response) => {
                if (response.ok){
                    return response.json();
                } else {
                    throw new Error("Failed to Create Simulation");
                }
            })
            .then(results => {
                this.loadSimulations();
                this.selectSimulation(this.createName);
            })
            .catch((error) => {
              console.log(error);
            });
        },
        deleteSimulation: function(){
            console.log("Delete: " + this.simulation);
            let url = new URL('../deleteSim', window.location.href);
            let params = {'simName': this.simulation};
            url.search = new URLSearchParams(params).toString();
            fetch(url)            
            .then((response) => {
                if (response.ok){
                    return response.json();
                } else {
                    throw new Error("Failed to Delete Simulation");
                }
            })
            .then(results => {
                this.createName = "";
                this.simulation = null;
                this.simState = "";
                this.simComplete = false;;
                this.loadSimulations();
            })
            .catch((error) => {
              console.log(error);
            });
        },
        runSimulation: function(){
            console.log("running " + this.simulation)
            this.simState = "Running"
            let url = new URL('../runSim', window.location.href);
            let params = {'simName': this.simulation};
            url.search = new URLSearchParams(params).toString();
            fetch(url)            
            .then((response) => {
                if (response.ok){
                    this.simState = "Complete"
                    return response.json();                    
                } else {
                    throw new Error("Failed to Run Simulation");
                }
            })
            .catch((error) => {
                console.log(error);
              });
        },
        selectSimulation: function(sim){
            console.log("Select: " + sim);
            let url = new URL('../getSimStatus', window.location.href);
            let params = {'simName': sim};
            url.search = new URLSearchParams(params).toString();
            fetch(url)            
            .then((response) => {
                if (response.ok){
                    return response.json();
                } else {
                    throw new Error("Failed to Select Simulation");
                }
            })
            .then(results => {
                this.simState = results.state;
                if (this.simState == "complete"){
                    this.simComplete = true;
                } else {
                    this.simComplete = false;
                }
                this.simulation = sim;
            })
            .catch((error) => {
              console.log(error);
            });
        },
        editSimulation: function(){
            this.$emit('edit', this.simulation);
        },
        viewSimulation: function(){
            this.$emit('view', this.simulation);
        },
        loadSimulations: function(){
            fetch("/getSims")           
            .then((response) => {
                if (response.ok){
                    return response.json();
                } else {
                    throw new Error("Failed to Get Simulations");
                }
            })
            .then(results => {
                this.simulations = results;
            })
            .catch((error) => {
              console.log(error);
            });
        }
    },
    created(){
        this.loadSimulations();
    }
};