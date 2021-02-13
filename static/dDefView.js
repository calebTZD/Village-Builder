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
                </div>`,
    data: function() {
        return {
            'name': "resource"
        };
    },
    methods: {
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