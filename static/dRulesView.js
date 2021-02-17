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

Vue.component('VillagerRulesView', {
    template: `<div>
                    Villager                  
                </div>`,
    data: function() {
        return {};
    },
    methods: {
    }
});

Vue.component('ResourceRulesView', {
    template: `<div>
                    R: {{name}}
                    <input v-model="simData['numVillages']"> 
                    <ul>
                        <li v-for="r in resources">
                            <input type="checkbox" :value="r" :id="r" v-model="simData['checkedResources']" @click="check($event)"> {{r}}
                        </li>
                    </ul>
                    <div v-for="r in resources">
                        <input type="checkbox" :value="r" :id="r" v-model="simData['checkedResources']" @click="check($event)"> {{r}}
                    </div>
                    <p>{{simData}}</p>                
                </div>`,
    data: function() {
        return {
            'name': "resource",
            'resources': [],
            'simData': {
                'numVillages': 1,
                'checkedResources': []
            }
        };
    },
    methods: {    
        check: function(e){
            if (e.target.checked){
                console.log(e.target.value);
            }
        },
        getResources: function(){
            fetch("/getData")
                .then(response => response.json())
                .then(results => {
                    this.resources = results;
                    console.log(this.resources);})
        }
    },    
    created(){
        this.getResources();
    }
});

let RulesViewClass = new Vue({
    el: '#RulesView',
    template: `<div>
                    <div class="d-flex flex-column">
                        <button v-on:click="village">Village</button>
                        <button v-on:click="resource">Resource</button>
                        <button v-on:click="villager">Villager</button>
                    </div>
                    <component v-bind:is="RulesView" />
                </div>`,
    data: {
        RulesView: 'VillageRulesView'
    },
    methods: {
        village: function(){
            this.RulesView = 'VillageRulesView';
        },
        villager: function(){
            this.RulesView = 'VillagerRulesView';
        },
        resource: function(){
            this.RulesView = 'ResourceRulesView';
        },
        addAsync: async function(){
            const response = await fetch("/add2?x="+this.x+"&y="+this.y);
            const results = await response.json();
            console.log(JSON.stringify(results));
            this.value = JSON.stringify(results);
        }
    }
  });

export const RulesView = RulesViewClass;