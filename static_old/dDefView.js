Vue.component('VillageDefView', {
    template: `<div>
        Starting Villagers <input type="number" id="NoVillagers" value="10"> 
        <br> Starting size <input type="number" id="Size" value="1">
        <br><br> Starting resource amounts: 
        <div v-for="resource in resources">
            <label>{{resource.type}}</label><input type="number" id="resource.type" value="100">
        </div>
        <br><br>
        
    </div>`,
    data: function() {
        return {
            'resources': [],

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

        
    },    
    created(){
        this.getResources();
    }
});
Vue.component('VillagerDefVeiw', {
    template: `<div>
        Base Work Speed <input type="number" id="WorkSpeed" value="5"><br> 
        Allow villager types? <input type="checkbox" id="VillagerType">
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
                    <br><br>Select which resources are available:<br>
                    <div v-for="resource in resources">
                        <input type="checkbox" id="resource.type" @click="check($event)"><label>{{resource.type}}</label>
                        <input type="number" class="resource.type" value=500>
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