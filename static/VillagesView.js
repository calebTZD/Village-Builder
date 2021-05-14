export const VillagesView = {
    template: `<div>
                    <button type="button" class="btn btn-success px-3" v-on:click="showAllVillages()" v-show="!showAll">
                        <i class="bi bi-plus-square" style="font-size: 1rem; color: white;"></i>
                    </button>
                    <button type="button" class="btn btn-success px-3" v-on:click="hideAllVillages()" v-show="showAll">
                        <i class="bi bi-minus-square" style="font-size: 1rem; color: white;">Done</i>
                    </button>
                    <div class="container">
                        <div class="row">
                            <div class="col-sm" v-show="showAll">
                                <div class="list-group">
                                    <button type="button" class="list-group-item list-group-item-action" v-for="villageName in allNames" v-on:click="addVillage(villageName)" >
                                        {{villageName}}
                                    </button>
                                </div>
                            </div>
                            <div class="col-sm">
                                <li v-for="village in simVillages">
                                    {{village.fixed.name}}
                                </li>
                            </div>
                            <div class="col-sm">
                                {{villageData.fixed.name}}
                            </div>
                        </div>
                    <div>
                    {{simVillages}}
                </div>`,
    data() {
        return {
            showAll: false,
            allNames:[],
            allVillages: [],
            simVillages:[],
            villageData: {'fixed':{'name': "test"}}
        }
    },    
    methods: {
        showAllVillages: function(){
            this.showAll = true;
        },
        hideAllVillages: function(){
            this.showAll = false;
        },
        addVillage: function(villageName){
            this.simVillages[villageName] = this.allVillages[villageName];
        },
        getData: function(){
            fetch("/getData")
            .then(response => response.json())
            .then(results => {
                this.simVillages = results.villages;
            });
            fetch("/getVillages")
            .then(response => response.json())
            .then(results => {
                this.allVillages = results;
                this.allNames = Object.keys(this.allVillages);
            });
        }
    },
    created(){
        this.getData();
    }
};