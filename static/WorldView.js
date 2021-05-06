export const WorldView = {
    template: `<div>
                    <div class="d-flex flex-row">
                        <div class="d-flex flex-column flex-fill">
                            <h2>Simulation Settings:</h2>
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
                            <h4>Starting Villagers</h4>
                            <div>
                                <input type="checkbox" id="lumberjack">
                                <label for="lumberjack"> Lumberjack </label>
                            </div>
                            <div>
                                <input type="checkbox" id="farmer">
                                <label for="farmer"> Farmer </label>
                            </div>
                            <div>
                                <input type="checkbox" id="hunter">
                                <label for="hunter"> Hunter </label>
                            </div>
                            <div>
                                <input type="checkbox" id="stonemason">
                                <label for="stonemason"> Stonemason </label>
                            </div>
                            <div>
                                <input type="checkbox" id="miner">
                                <label for="miner"> Miner </label>
                            </div>
                            <div>
                                <input type="checkbox" id="merchant">
                                <label for="merchant"> Merchant </label>
                            </div>
                            <div>
                                <input type="checkbox" id="researcher">
                                <label for="researcher"> Researcher </label>
                            </div>
                            <div>
                                <input type="checkbox" id="warrior">
                                <label for="warrior"> Warrior </label>
                            </div>
                        </div>
                    </div>
                </div>
                {{worldData}}`,
    data() {
        return {
            worldData: {'settings':{'days':1, 'maxVillagersPerVillage': 1, 'maxBuildingsPerVillage': 1}}
        }
    },    
    methods: {    
        getData: async function(){
            const response = await fetch("/getData");
            const results = await response.json();
            this.worldData = results.world;
            console.log(JSON.stringify(results));
            this.value = JSON.stringify(results);
        }
    },
    created(){
        this.getData();
    }
  };