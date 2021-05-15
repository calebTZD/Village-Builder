export const WorldView = {
    template: `<div>
                    <div class="d-flex">
                        <div class="d-flex flex-column flex-fill">
                            <h4>Simulation Settings:</h4>
                            <br><br>
                            <div>
                                Days to Run: <input type="number" v-model="worldData.settings.days">
                            </div>
                            <div>
                                Villeger Maximum: <input type="number" v-model="worldData.settings.maxVillagersPerVillage">
                            </div>
                            <div>
                                Building Maximum: <input type="number" v-model="worldData.settings.maxBuildingsPerVillage">
                            </div>
                        </div>
                        <div class="d-flex flex-column flex-fill">
                            <h5>Starting Villagers</h5>
                            <div>
                                <input type="checkbox" id="lumberjack" value="lumberjack" v-model="worldData.settings.startingVillagers">
                                <label for="lumberjack"> Lumberjack </label>
                            </div>
                            <div>
                                <input type="checkbox" id="farmer" value="farmer" v-model="worldData.settings.startingVillagers">
                                <label for="farmer"> Farmer </label>
                            </div>
                            <div>
                                <input type="checkbox" id="hunter" value="hunter" v-model="worldData.settings.startingVillagers">
                                <label for="hunter"> Hunter </label>
                            </div>
                            <div>
                                <input type="checkbox" id="stonemason" value="stonemason" v-model="worldData.settings.startingVillagers">
                                <label for="stonemason"> Stonemason </label>
                            </div>
                            <div>
                                <input type="checkbox" id="miner" value="miner" v-model="worldData.settings.startingVillagers">
                                <label for="miner"> Miner </label>
                            </div>
                            <div>
                                <input type="checkbox" id="merchant" value="merchant" v-model="worldData.settings.startingVillagers">
                                <label for="merchant"> Merchant </label>
                            </div>
                            <div>
                                <input type="checkbox" id="researcher" value="researcher" v-model="worldData.settings.startingVillagers">
                                <label for="researcher"> Researcher </label>
                            </div>
                            <div>
                                <input type="checkbox" id="warrior" value="warrior" v-model="worldData.settings.startingVillagers">
                                <label for="warrior"> Warrior </label>
                            </div>
                        </div>
                    </div>
                </div>`,
    data() {
        return {
            worldData: {'settings':{'days':1, 'maxVillagersPerVillage': 1, 'maxBuildingsPerVillage': 1, 'startingVillagers': []}}
        }
    },    
    methods: {    
            getData: function(){
                fetch("/getData")
                .then(response => response.json())
                .then(results => {
                    this.worldData = results.world;
                })
            }
    },
    created(){
        this.getData();
    }
  };