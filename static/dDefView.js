Vue.component('VillageDefView', {
    template: `<div>
        Starting Villagers <input type="number" id="NoVillagers" value="10"> 
        <br> Starting size <input type="number" id="Size" value="1">
        <br><br> Starting resource amounts: 
        <div v-for="resource in resources">
            <label>{{resource.type}}</label><input type="number" id="resource.type" value="100">
        </div>
        <br><br>
        <div class="d-flex flex-column">
            <div v-for="name in villages">
                <input id="name" type="text" v-model="name">
            </div>
            <button v-on:click="addVillage">New village</button>
        </div>
    </div>`,
    data: function() {
        return {
            'resources': [],
            'villages': []

        };
    },
    methods: {
        getResources: function(){
            fetch("/getData")
                .then(response => response.json())
                .then(results => {
                    this.resources = results.resources;
                    console.log(this.resources);})
        },

        addVillage: function(){
            fetch("/getData")
            .then(response => response.json())
            .then(results => {
                var i = Math.floor(Math.random() * results.villageNames.length)
                this.villages.push(results.villageNames[i])
            })
        }
    },    
    created(){
        this.getResources();
    }
});
Vue.component('VillagerDefVeiw', {
    template: `<div>
        Base Work Speed <input type="number" id="WorkSpeed" value="5"> 
        
    </div>`,
    data: function() {
        return {};
    },
    methods: {
        
    }
});

Vue.component('ResourceDefView', {
    template: `<div>
                    <input type="checkbox" id="buildingcheck" @click="check($event)"> Use buildings for resources
                    <div v-for="resource in resources">
                    <input type="checkbox" id="resource.type" @click="check($event)"><label>{{resource.type}}</label>
                    </div>                    
                </div>`,
    data: function() {
        return {
            'resources': []
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
                    this.resources = results.resources;
                    console.log(this.resources);})
        }
    },    
    created(){
        this.getResources();
    }
});

let DefViewClass = new Vue({
    el: '#DefView',
    template: `<div>
                    <div class="d-flex fles-row">
                        <div class="d-flex flex-column">
                            <button v-on:click="village">Village</button>
                            <button v-on:click="resource">Resource</button>
                            <button v-on:click="Villager">Villager</button>
                        </div>
                        <component v-bind:is="defView" />
                    </div>
                </div>`,
    data: {
        defView: 'VillageDefView'
    },
    methods: {
        village: function(){
            this.defView = 'VillageDefView';
        },
        resource: function(){
            this.defView = 'ResourceDefView';
        },
        Villager: function(){
            this.defView = 'VillagerDefVeiw';
        }
    }
  });

export const DefView = DefViewClass;