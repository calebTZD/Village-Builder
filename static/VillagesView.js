let VillagesViewClass = new Vue({
    el: '#VillagesView',
    props: ['simData'],
    template: `<div>
                    {{simData}}
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

export const VillagesView = VillagesViewClass;