let locClass = new Vue({
    el: '#locationVue',
    template: `<div>
                    <h2>Location Settings<h2>
                    <br><br>
                    <table>
                        <tr>
                            <th>Location</th>
                            <th>Building Maximum</th>
                            <th>Average Distance</th>
                            <th>Upgrade Cost</th>
                        </tr>
                        <tr>
                            <td>Grassland</td>
                        </tr>
                        <tr>
                            <td>Forrest</td>
                        </tr>
                        <tr>
                            <td>Stone Deposit</td>
                        </tr>
                        <tr>
                            <td>Ore Deposit</td>
                        </tr>
                </div>`,
    data: {
        'simData': [],

    },
    methods: {

    }
  });

export const locationView = locClass;