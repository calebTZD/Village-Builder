//Character Class
class VanillaJSAddClass{
    constructor(){
        this.tabDiv = document.getElementById("vanillaJSTab");
        this.xTB = document.createElement("INPUT");
        this.xTB.setAttribute("type", "text");
        this.tabDiv.appendChild(this.xTB);
        let plusText = document.createElement("SPAN");
        plusText.innerHTML = " + ";
        this.tabDiv.appendChild(plusText);
        this.yTB = document.createElement("INPUT");
        this.yTB.setAttribute("type", "text");
        this.tabDiv.appendChild(this.yTB);
        this.addButton = document.createElement("INPUT");
        this.addButton.setAttribute("type", "button");
        this.addButton.value = "=";
        this.tabDiv.appendChild(this.addButton);
        this.addAsyncButton = document.createElement("INPUT");
        this.addAsyncButton.setAttribute("type", "button");
        this.addAsyncButton.value = "=(async)";
        this.tabDiv.appendChild(this.addAsyncButton);
        this.resultsP = document.createElement("P");
        this.tabDiv.appendChild(this.resultsP);
    }
    init(){
        this.addButton.onclick = function() {this.add()}.bind(this);
        this.addAsyncButton.onclick = (async function(){this.addAsync()}.bind(this));        
    }
    add(){        
        console.log(this.xTB.value + this.yTB.value);
        fetch("/add2?x="+this.xTB.value+"&y="+this.yTB.value)
            .then(function(response){            
                return response.json();
                }.bind(this))
            .then(function(results){
                console.log(JSON.stringify(results));
                this.resultsP.innerHTML = JSON.stringify(results);
                }.bind(this));
    }
    async addAsync(){        
        const response = await fetch("/add2?x="+this.xTB.value+"&y="+this.yTB.value);
        const results = await response.json();
        console.log(JSON.stringify(results));
        this.resultsP.innerHTML = JSON.stringify(results);
    }
}


export const VanillaJSAdder = new VanillaJSAddClass();