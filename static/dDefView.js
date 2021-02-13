Vue.component('VillageDefView', {
    template: `<div>
                    Village                  
                </div>`,
    data: function() {
        return {};
    },
    methods: {
    }
});

Vue.component('ResourceDefView', {
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
            fetch("/getResourceTypes")
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

let DefViewClass = new Vue({
    el: '#DefView',
    template: `<div>
                    <button v-on:click="village">Village</button>
                    <button v-on:click="resource">Resource</button>
                    <component v-bind:is="defView" />
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
        addAsync: async function(){
            const response = await fetch("/add2?x="+this.x+"&y="+this.y);
            const results = await response.json();
            console.log(JSON.stringify(results));
            this.value = JSON.stringify(results);
        }
    }
  });

export const DefView = DefViewClass;