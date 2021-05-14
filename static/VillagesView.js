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
        getData: function(){
            fetch("/getData")
            .then(response => response.json())
            .then(results => {
                this.villagesData = results.villages;
            })
        }
    },
    created(){
        this.getData();
    }
};