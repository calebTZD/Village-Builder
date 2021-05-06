let VillagesViewClass = new Vue({
    el: '#VillagesView',
    props: ['simData'],
    template: `<div>
                    {{villagesData}}
                    <H1>{{villagesData.fixed.name}}</H1>
                </div>`,
    data: {
        'simData':{},
        'villagesData': {}     
    },
    methods: {      
        getData: function(){
            fetch("/getData")
            .then(response => response.json())
            .then(results => {
                this.simData = results;
                this.villagesData = this.simData.villages;
            })
        }
    },
    mounted(){
        this.getData();
    }
});

export const VillagesView = VillagesViewClass;