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
        let adj = (h-10)/max;
        let svg = d3.select(elemID)
                    .append("svg")
                    .attr("width", w)
                    .attr("height", h);
        svg.selectAll("rect")
            .data(data)
            .enter()
            .append("rect")
            .attr("x", function(d, i) { return i * (w / data.length); })
            .attr("y", function(d) { return h-(d.value * adj); })
            .attr("width", w / data.length - spacing)
            .attr("height", function(d) { return d.value * adj;})
            .attr("fill", function(d) { return "rgb(0, 0, " + (d.value * 10) + ")";});
        svg.selectAll("text")
            .data(data)
            .enter()
            .append("text")
            .text(function(d) {return d.label;})
            .attr("text-anchor", "middle")
            .attr("x", function(d, i) {return i * (w / data.length) + (w / data.length - spacing) / 2;})
            .attr("y", function(d) { return h - (d.value * adj) + 10;})
            .attr("font-family", "sans-serif")
            .attr("font-size", "11px")
            .attr("fill", "white");
    }
}
export const ChartMaker = new ChartMakerClass();