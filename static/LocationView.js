export const LocationView = {
    template: `<div class="d-flex">
                    <div class="d-flex flex-column justify-content-between">
                        <div>Type</div>
                        <div>Amount per Village</div>
                        <div>Avewrage Distance</div>
                        <div>Upgrade Cost</div>
                    </div>
                    <div v-for="(item, type) in locationData" class="d-flex flex-column">
                        <h5>{{type}}</h5>
                        </label><input type="number" class="form-control" v-model="item.settings.numPerVillage">
                        </label><input type="number" class="form-control" v-model="item.settings.aveDistance">
                        </label><input type="number" class="form-control" v-model="item.settings.enhancemntCost">
                    </div>
                </div>`,
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
                this.locationData = results.locations;

            })
        }
    },
    created(){
        this.getData();
    }
};