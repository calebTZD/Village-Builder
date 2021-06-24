class ChartMakerClass {
    constructor(){
    }
    init() {
    }
    
    drawBarChart(elemID, h, w, data){
        $(elemID).empty();
        let spacing = 1;    
        let max = 0;
        for (let i = 1; i < data.length; i++) {
            if (data[i].value > max) max = data[i].value;
        }
        let yScale = (h-10)/max;
        let svg = d3.select(elemID)
                    .append("svg")
                    .attr("width", w)
                    .attr("height", h);
        svg.selectAll("rect")
            .data(data)
            .enter()
            .append("rect")
            .attr("x", function(d, i) { return i * (w / data.length); })
            .attr("y", function(d) { return h-(d.value * yScale); })
            .attr("width", w / data.length - spacing)
            .attr("height", function(d) { return d.value * yScale;})
            .attr("fill", function(d) { return "rgb(0, 0, " + (d.value * 10) + ")";});
        svg.selectAll("text")
            .data(data)
            .enter()
            .append("text")
            .text(function(d) {return d.label;})
            .attr("text-anchor", "middle")
            .attr("x", function(d, i) {return i * (w / data.length) + (w / data.length - spacing) / 2;})
            .attr("y", function(d) { return h - (d.value * yScale) + 10;})
            .attr("font-family", "sans-serif")
            .attr("font-size", "11px")
            .attr("fill", "white");
            //.attr("transform", "rotate(-90)");
    }

    drawLineChart(elemID, h, w, dataSet){
        // append the svg object to the body of the page
        var svg = d3.select(elemID)
            .append("svg")
            .attr("width", w+20)
            .attr("height", h+40)
            .append("g")
            .attr("transform",
                  "translate(" + 20 + "," + 20 + ")");
        
        // let dataSet = [{key: "Brad", values: [{tick:1,value:1},{tick:2,value:2},{tick:3,value:2},{tick:4,value:2},{tick:5,value:2}]},
        //             {key: "Caleb", values: [{tick:1,value:1},{tick:2,value:5},{tick:3,value:7},{tick:4,value:3},{tick:5,value:2}]}];
        let res = dataSet.map(function(d){ return d.key })
        let color = d3.scaleOrdinal()
                        .domain(res)
                        .range(['#e41a1c','#377eb8','#4daf4a','#984ea3','#ff7f00','#ffff33','#a65628','#f781bf','#999999']);

        let maxX = 0;
        let maxY = dataSet[0].values.length;
        for(let set of dataSet){
            for (let datum of set.values) {
                if (datum.value > maxX) maxX = datum.value;
            }
        }
        // Add X axis --> it is a date format
        let x = d3.scaleLinear()
            .domain([0, maxX])
            .range([ 0, w ]);
        svg.append("g")
            .attr("transform", "translate(0," + h + ")")
            .call(d3.axisBottom(x));

        // Add Y axis
        let y = d3.scaleLinear()
            .domain([0, maxY])
            .range([ h, 0 ]);
        svg.append("g")
            .call(d3.axisLeft(y));


        svg.selectAll(".line")
            .data(dataSet)
            .enter()
            .append("path")
            .attr("fill", "none")
            .attr("stroke", function(d){ return color(d.key) })
            .attr("stroke-width", 1.5)
            .attr("d", function(d){
            return d3.line()
                .x(function(d) { return x(d.tick); })
                .y(function(d) { return y(d.value); })
                (d.values)
            });
    }
}
export const ChartMaker = new ChartMakerClass();