let VillageBuilder = new Vue({
    el: '',
    template: `<div>
    <div id="bdy" class="d-flex flex-row justify-content-left">
        <div id="sidebar" class="d-flex flex-column justify-content-center">
            <div id="villager" class="d-flex flex-row justify-content-center"S>
                <label id="body-content">Villagers in Village: </label>
                <input type="number"> 
            </div>
            <div v-for="resource in resources">
                <input type="checkbox" id="resource.type">
                <label for="resource.type">{{resource.type}}</label>               
            </div>
        </div>
        <div class="d-flex flex-column">
            <button v-on:click="addVillage">New village</button>
            <div v-for="name in villages">
                <button>{{name}}</button>
            </div>
        </div>
    </div>
</div>`,
    data: {
        resources: [],
        villages: []
    },
    methods: {
        getResources: function(){
            fetch("/getData")
            .then(response => response.json())
            .then(results => {
                this.resources = results.resources;
                console.log(this.data)
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

export const VBuilder = VillageBuilder;