let SimRulesClass = new Vue({
    el: '#SimRules',
    template: `<div>
                <input v-model="simData['numVillages']"> 
                <ul>
                    <li v-for="r in resources">
                        <input type="checkbox" :value="r" :id="r" v-model="simData['checkedResources']" @click="check($event)"> {{r}}
                    </li>
                </ul>
                <div v-for="r in resources">
                    <input type="checkbox" :value="r" :id="r" v-model="simData['checkedResources']" @click="check($event)"> {{r}}
                </div>
                <p>{{simData}}</p
                </div>`,
    data: {
        resources: [],
        simData: {
            numVillages: 1,
            checkedResources: []
        }
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
        },
        addAsync: async function(){
            const response = await fetch("/add2?x="+this.x+"&y="+this.y);
            const results = await response.json();
            console.log(JSON.stringify(results));
            this.value = JSON.stringify(results);
        }
    },
    mounted(){
        this.getResources();
    }
  });

export const SimRules = SimRulesClass;