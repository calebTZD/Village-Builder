export const VillagesView = {
    template: `<div>
                    >>>>>>>>>>>>>test
                    <div>
                        {{villagesData.fixed.name}}
                        <div> test </div>
                    </div>
                </div>`,
    data() {
        return {
            villagesData: {'fixed':{'name': ""}}
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