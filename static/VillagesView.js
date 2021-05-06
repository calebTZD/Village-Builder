let VillagesViewClass = new Vue({
    el: '#VillagesView',
    props: ['simdata'],
    template: `<div>
                    test
                    {{simdata}}
                </div>`,
    data: {
    },
    methods: {      
    },
    mounted(){        
    }
});

export const VillagesView = VillagesViewClass;