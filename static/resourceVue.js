let ResourceClass = new Vue({
    el: '',
    template: `<div>
                    <div v-for="resource in resources">
                        <label>{{resource.type}}</label>
                        <input type="number" v-model="resource.priority">
                    </div>
                </div>`,
    data: {
        resources: []

    },
    methods: {
        getResources: function(){
            fetch("/getData")
            .then(response => response.json())
            .then(results => {
                this.resources = results.resources;
                console.log(this.data)
                console.log(this.resources);})
        }

    },
    created(){
        this.getResources();
    }
  });

export const resource = ResourceClass;