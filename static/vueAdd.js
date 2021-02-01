let VueAdderClass = new Vue({
    el: '#VueAdder',
    template: `<div>
                    <input v-model="x">
                    <input v-model="y">
                    <button v-on:click="add">=</button>
                    <button v-on:click="addAsync">=(async)</button>
                    <p>Results: {{value}}</p>
                </div>`,
    data: {
        x: 0,
        y:0,
        value: 0
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

export const VueAdder = VueAdderClass;