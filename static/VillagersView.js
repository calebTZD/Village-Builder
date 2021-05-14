export const VilligerView = {
    template: `<div v-for="item in locationData">
                    <h5>{{item.fixed.type}}:</h5>
                    <label>Amount per Village: </label><input type="number" v-model="item.settings.numPerVillage"><br>
                    <label>Average Distance: </label><input type="number" v-model="item.settings.aveDistance"><br>
                    <label>Upgrade Cost: </label><input type="number" v-model="item.settings.enhancemntCost">

                </div>
                {{locationData}}`,
    data() {
        return {
            locationData: {'type':{'fixed':{'name': ""},'settings':{'numPerVillage': 1, 'aveDistance': 1, 'enhancemntCost': 200}}}
        }
    },    
    methods: {    
        getData: function(){
            fetch("/getData")
            .then(response => response.json())
            .then(results => {
                this.locationData = results.villagers;

            })
        }
    },
    created(){
        this.getData();
    }
};