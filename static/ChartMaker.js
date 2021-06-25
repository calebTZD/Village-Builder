class ChartMakerClass {
    constructor(){
    }
    init() {
    }
    
    drawBarChart(elemID, h, w, data){
        // data = [{label: 'Legolas', value: 15},
        //                 {label: 'Gimli', value: 8},
        //                 {label: 'Gandalf', value: 90},
        //                 {label: 'Frodo', value: 6},
        //                 {label: 'Elron', value: 25}];
        
        let spacing = 1;    
        let max = 0;
        for (let i = 1; i < data.length; i++) {
            if (data[i].value > max) max = data[i].value;
        }
        let yScale = (h-10)/max;

        $(elemID).empty();
        let padX = 100;
        let padY = 100;
        let padLegend = 15;
        let padLeftLabels = 50;
        let offsetX = 40;
        let offsetY = 40;

        $(elemID).empty();
        let svg = d3.select(elemID)
            .append("svg")
            .attr("width", w+padX+padLegend+padLeftLabels+padLeftLabels)
            .attr("height", h+padY)
            .append("g")
            .attr("transform",
                    "translate(" + (offsetX+padLeftLabels) + "," + offsetY + ")"); 

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

    drawBarChartNew(elemID, h, w, data){
        // data = [{label: 'Legolas', value: 15},
        //                 {label: 'Gimli', value: 8},
        //                 {label: 'Gandalf', value: 90},
        //                 {label: 'Frodo', value: 6},
        //                 {label: 'Elron', value: 25}];
        
        let spacing = 1;    
 
        $(elemID).empty();
        let padX = 100;
        let padY = 100;
        let padLegend = 15;
        let padLeftLabels = 50;
        let offsetX = 40;
        let offsetY = 40;

        $(elemID).empty();
        let svg = d3.select(elemID)
            .append("svg")
            .attr("width", w+padX+padLegend+padLeftLabels+padLeftLabels)
            .attr("height", h+padY)
            .append("g")
            .attr("transform",
                    "translate(" + (offsetX+padLeftLabels) + "," + offsetY + ")"); 

        // Ranges
        let maxX = data.length;
        let maxY = 0;
        let xDomain = [];
        for (let i = 1; i < data.length; i++) {
            if (data[i].value > maxY) maxY = data[i].value;
            xDomain.push(data[i].label);
        }

        // X axis
        let x = d3.scaleLinear()
            .domain(xDomain)
            .range([ 0, w ]);
        svg.append("g")
            .attr("class", "chartAxis")
            .attr("transform", "translate(0," + h + ")")
            .call(d3.axisBottom(x));

        // Y axis
        let y = d3.scaleLinear()
            .domain([0, maxY])
            .range([ h, 0 ]);
        svg.append("g")
            .attr("class", "chartAxis")
            .call(d3.axisLeft(y));

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

    drawHorizontalStackedBarChart(elemID, h, w, dataSet){
        // let dataSet = [{"key":"Brad", "Swords":5,"Knifes":8, "Axes":13},
        //                 {"key":"Caleb", "Swords":5,"Knifes":8, "Axes":13}];

        let padX = 100;
        let padY = 100;
        let padLegend = 15;
        let padLeftLabels = 50;
        let offsetX = 40;
        let offsetY = 40;

        $(elemID).empty();
        let svg = d3.select(elemID)
            .append("svg")
            .attr("width", w+padX+padLegend+padLeftLabels+padLeftLabels)
            .attr("height", h+padY)
            .append("g")
            .attr("transform",
                    "translate(" + (offsetX+padLeftLabels) + "," + offsetY + ")");  
            
        //remove "key" from list of keys to get stack labels
        let stackItems = Object.keys(dataSet[0]);
        stackItems.splice(stackItems.indexOf("key"), 1);

        // colors for stack
        let color = d3.scaleOrdinal()
                        .domain(stackItems)
                        .range(['#FF0000','#0000FF','#00FF00','#FFFF00','#FF00FF','#FFA500','#008000','#00FFFF','#A52A2A', 'FF1493', 'A52A2A', '7FFFD4', 'A0522D']);

        // List of columns
        let columns = d3.map(dataSet, function(d){return(d.key)}).keys();

        // Ranges
        let maxY = 0;
        for(let set of dataSet){
            let stackSum = 0;
            for (let item of stackItems) {
                stackSum += set[item];
            }
            if (stackSum > maxY) maxY = stackSum;
        }

        // Add X axis
        let y = d3.scaleBand()
            .domain(columns)
            .range([0, h])
            .padding([0.2]);
        svg.append("g")
            .attr("class", "chartAxis")
            .call(d3.axisLeft(y));

        // Add Y axis
        let x = d3.scaleLinear()
            .domain([0, maxY])
            .range([ 0, w ]);
        svg.append("g")
            .attr("class", "chartAxis")
            .attr("transform", "translate(0," + h + ")")
            .call(d3.axisBottom(x).tickSizeOuter(0));


        //stack the data
        let stackedData = d3.stack()
            .keys(stackItems)
            (dataSet)

        // Show the bars
        svg.append("g")
            .selectAll("g")
            .data(stackedData)
            .enter().append("g")
                .attr("fill", function(d) { return color(d.key); })
                .selectAll("rect")
                // enter again to loop through stack items and build rectangles
                .data(function(d) { return d; })
                .enter().append("rect")
                    .attr("y", function(d) { 
                        return y(d.data.key); })
                    .attr("x", function(d) { 
                        return x(d[0]); })
                    .attr("width", function(d) { 
                        return x(d[1]) - x(d[0]); })
                    .attr("height",
                        y.bandwidth())

        //legend
        svg.append("g").selectAll("text")
            .data(stackItems)
            .enter()
            .append("text")
            .attr("transform", function(d){ return "translate(" + (w+3) + "," + 30 * stackItems.indexOf(d) + ")"})
		    .attr("dy", ".35em")
            .attr("fill", function(d){ return color(d) })
            .text(function(d) { return d });
    }

    drawVerticalStackedBarChart(elemID, h, w, dataSet){
        // let dataSet = [{"key":"Brad", "Swords":5,"Knifes":8, "Axes":13},
        //                 {"key":"Caleb", "Swords":5,"Knifes":8, "Axes":13}];

        let padX = 100;
        let padY = 100;
        let padLegend = 15;
        let offsetX = 40;
        let offsetY = 40;

        $(elemID).empty();
        let svg = d3.select(elemID)
            .append("svg")
            .attr("width", w+padX+padLegend)
            .attr("height", h+padY)
            .append("g")
            .attr("transform",
                    "translate(" + offsetX + "," + offsetY + ")");  
            
        //remove "key" from list of keys to get stack labels
        let stackItems = Object.keys(dataSet[0]);
        stackItems.splice(stackItems.indexOf("key"), 1);

        // colors for stack
        let color = d3.scaleOrdinal()
                        .domain(stackItems)
                        .range(['#FF0000','#0000FF','#00FF00','#FFFF00','#FF00FF','#FFA500','#008000','#00FFFF','#A52A2A', 'FF1493', 'A52A2A', '7FFFD4', 'A0522D']);

        // List of columns
        let columns = d3.map(dataSet, function(d){return(d.key)}).keys();

        // Ranges
        let maxY = 0;
        for(let set of dataSet){
            let stackSum = 0;
            for (let item of stackItems) {
                stackSum += set[item];
            }
            if (stackSum > maxY) maxY = stackSum;
        }

        // Add X axis
        let x = d3.scaleBand()
            .domain(columns)
            .range([0, w])
            .padding([0.2]);
        svg.append("g")
            .attr("class", "chartAxis")
            .attr("transform", "translate(0," + h + ")")
            .call(d3.axisBottom(x).tickSizeOuter(0));

        // Add Y axis
        let y = d3.scaleLinear()
            .domain([0, maxY])
            .range([ h, 0 ]);
        svg.append("g")
            .attr("class", "chartAxis")
            .call(d3.axisLeft(y));

        //stack the data
        let stackedData = d3.stack()
            .keys(stackItems)
            (dataSet)

        // Show the bars
        svg.append("g")
            .selectAll("g")
            .data(stackedData)
            .enter().append("g")
                .attr("fill", function(d) { return color(d.key); })
                .selectAll("rect")
                // enter again to loop through stack items and build rectangles
                .data(function(d) { return d; })
                .enter().append("rect")
                    .attr("x", function(d) { return x(d.data.key); })
                    .attr("y", function(d) { return y(d[1]); })
                    .attr("height", function(d) { return y(d[0]) - y(d[1]); })
                    .attr("width",x.bandwidth())

        //legend
        svg.append("g").selectAll("text")
            .data(stackItems)
            .enter()
            .append("text")
            .attr("transform", function(d){ return "translate(" + (w+3) + "," + 30 * stackItems.indexOf(d) + ")"})
		    .attr("dy", ".35em")
            .attr("fill", function(d){ return color(d) })
            .text(function(d) { return d });
    }

    drawLineChart(elemID, h, w, dataSet){
        // let dataSet = [{key: "Brad", values: [{tick:1,value:1},{tick:2,value:2},{tick:3,value:2},{tick:4,value:2},{tick:5,value:2}]},
        //             {key: "Caleb", values: [{tick:1,value:1},{tick:2,value:5},{tick:3,value:7},{tick:4,value:3},{tick:5,value:2}]}];
        let padX = 100;
        let padY = 100;
        let padText = 15;
        let offsetX = 40;
        let offsetY = 40;

        $(elemID).empty();
        var svg = d3.select(elemID)
            .append("svg")
            .attr("width", w+padX)
            .attr("height", h+padY)
            .append("g")
            .attr("transform",
                  "translate(" + offsetX + "," + offsetY + ")");        

        // Line Color Map
        let keys = dataSet.map(function(d){ return d.key })
        let color = d3.scaleOrdinal()
                        .domain(keys)
                        .range(['#FF0000','#0000FF','#00FF00','#FFFF00','#FF00FF','#FFA500','#008000','#00FFFF','#A52A2A', 'FF1493', 'A52A2A', '7FFFD4', 'A0522D']);

        // Ranges
        let maxX = dataSet[0].values.length;
        let maxY = 0;
        for(let set of dataSet){
            for (let datum of set.values) {
                if (datum.value > maxY) maxY = datum.value;
            }
        }
        
        // X axis
        let x = d3.scaleLinear()
            .domain([0, maxX])
            .range([ 0, w ]);
        svg.append("g")
            .attr("class", "chartAxis")
            .attr("transform", "translate(0," + h + ")")
            .call(d3.axisBottom(x));

        // Y axis
        let y = d3.scaleLinear()
            .domain([0, maxY])
            .range([ h, 0 ]);
        svg.append("g")
            .attr("class", "chartAxis")
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

        //legend
        svg.append("g").selectAll("text")
            .data(dataSet)
            .enter()
            .append("text")
            .attr("transform", function(d){ return "translate(" + (w+3) + "," + 30 * keys.indexOf(d.key) + ")"})
		    .attr("dy", ".35em")
            .attr("fill", function(d){ return color(d.key) })
            .text(function(d) { return d.key });
    }
}
export const ChartMaker = new ChartMakerClass();