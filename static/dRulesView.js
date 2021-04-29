Vue.component('VillageRulesView', {
    template: `<div>
    <div class="d-flex flex-column">
        <div v-for="(village, index) in villages">
            <label v-on:click="setVillage(index)">{{village.Name}}</label>
            
        </div>
    </div>
    <div class="d-flex flex-column">
        <label>{{village.Name}}</label>
        <input type="number" v-model="village.ResourcePoints">
    </div>
                </div>`,
    data: function() {
        return {
            "villages": [
                {
                    "Name": "Shire",
                    "ResourcePoints": 200
                },
                {
                    "Name": "Mordor",
                    "ResourcePoints": 20000
                }
            ],
            "village": 
            {
                "Name": "Shire",
                "ResourcePoints": 200
            }
        };
    },
    methods: {
        setVillage: function(index){
            this.village = this.villages[index];      
        }
    }
});

let RulesViewClass = new Vue({
    el: '#RulesView',
    template: `<div>
                    <div class="d-flex flex-row">
                        <div class="d-flex flex-column">
                            <button v-on:click="addVillage">New village</button>
                            <div v-for="name in villages">
                                <button id="name"  v-on:click="village"> {{name}}</button>
                            </div>
                        </div>
                        <component v-bind:is="RulesView" />
                    </div>
                </div>`,
    data: {
        'villages': [],
        RulesView: ""

    },
    methods: {
        village: function(){
            this.RulesView = 'VillageRulesView';
        },
        
        addVillage: function(){
            fetch("/getData")
            .then(response => response.json())
            .then(results => {
                var i = Math.floor(Math.random() * results.villageNames.length)
                this.villages.push(results.villageNames[i])
            })
        }
    }
  });

export const RulesView = RulesViewClass;