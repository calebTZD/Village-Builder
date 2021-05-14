export const VillagesView = {
    template: `<div>
                    <button type="button" class="btn btn-success px-3"><i class="bi bi-plus-square" style="font-size: 1rem; color: white;"></i></button>
                    <div>
                        <li v-for="village in allVillages">
                            {{village.fixed.name}}
                        </li>
                    </div>
                    <div>
                        <li v-for="village in simVillages">
                            {{village.fixed.name}}
                        </li>
                    </div>
                    <div>
                        {{villageData.fixed.name}}
                    </div>
                    {{simVillages}}
                </div>`,
    data() {
        return {
            allVillages: [],
            simVillages:[],
            villageData: {'fixed':{'name': "test"}}
        }
    },    
    methods: {    
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
            });
        }
    },
    created(){
        this.getData();
    }
};