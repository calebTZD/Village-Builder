let ResourceClass = new Vue({
    el: '#VueResource',
    template: `<div >
                    <label>{{type}}</label>
                    <input type="number" v-model="priority">
                </div>`,
    data: {
        // resources: [
        //     {
        //     resource: {
                type: 'wood',
                priority: 1
            //   }
            // }
        // ]

    },
    methods: {
        add: function(){
            fetch("/add2?x="+this.x+"&y="+this.y)
                .then(response => response.json())
                .then(results => (this.value = JSON.stringify(results.value)))
        },
        addAsync: async function(){
            const response = await fetch("/add2?x="+this.x+"&y="+this.y);
            const results = await response.json();
            console.log(JSON.stringify(results));
            this.value = JSON.stringify(results);
        }
    }
  });

export const resource = ResourceClass;