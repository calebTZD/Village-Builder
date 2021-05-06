window.onload = init


function init(){
}

const TodoList = {
    template: 
    `<ol>
    <!--
      Now we provide each todo-item with the todo object
      it's representing, so that its content can be dynamic.
      We also need to provide each component with a "key",
      which will be explained later.
    -->
    <todo-item
      v-for="item in groceryList"
      v-bind:todo="item"
      v-bind:key="item.id"
    ></todo-item>
  </ol>
  <datacomp v-bind:mydata="simData.villages"></datacomp>`,
    data() {
      return {
        groceryList: [
          { id: 0, text: 'Vegetables' },
          { id: 1, text: 'Cheese' },
          { id: 2, text: 'Whatever else humans are supposed to eat' }
        ],
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
  
  const app = Vue.createApp(TodoList)
  
  app.component('todo-item', {
    props: ['todo'],
    template: `<li>{{ todo.text }}</li>`
  })

  app.component('datacomp', {
    props: ['mydata'],
    template: `***{{ mydata }}`
  })
  
  app.mount('#RulesView')