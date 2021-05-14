export const VillagesView = {
    template: `<div>
                    >>>>>>>>>>>>>test
                    <div v-if="loaded">
                        {{villagesData.fixed.name}}
                    </div>
                </div>`,
    data() {
        return {
            loaded: false,
            villagesData: {}
        }
    },    
    methods: {    
        getData: async function(){
            const response = await fetch("/getData");
            const results = await response.json();
            this.villagesData = results.villages;
            this.loaded = true;
        }
    },
    created(){
        this.getData();
    }
};