let RulesViewClass = new Vue({
    el: '#RulesView',
    template: `<div>                    
                    <div class="d-flex flex-column">
                        <div class="d-flex">
                            <div id="sim" class="flex-fill">                
                                <div id="SimVue"></div>
                            </div>
                            <div id="villages" class="flex-fill">
                                <div id="VillagesView" v-bind:simData="simData"></div>
                            </div>
                        </div>
                        <div class="d-flex">
                            <div id="villagers" class="flex-fill">
                                <div id="VillagersVue"></div>
                            </div>
                            <div id='locations' class="flex-fill">
                                <div id="LocationsVue"></div>
                            </div>
                            <div id="buildings" class="flex-fill">
                                <div id="BuildingsVue"></div>
                            </div>
                        </div>
                    </div>
                </div>`,
    data: {
        'simData':{}      
    },
    methods: {      
        getData: function(){
            fetch("/getData")
            .then(response => response.json())
            .then(results => {
                this.simData = results;
            })
        }
    },
    mounted(){
        this.getData();
    }
});

export const RulesView = RulesViewClass;