export const SimulationView = {
    template: 
    `<datacomp v-bind:mydata="simData.villages"></datacomp>`,
    data() {
      return {
        simData: {}
      }
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
  }  