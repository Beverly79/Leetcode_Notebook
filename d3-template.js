// !preview r2d3 data = diary_group, d3_version = 4, container = "div", options = list(start = 2022, end = 2024)

// Based on https://bl.ocks.org/mbostock/4063318


var height = 200,
    cellSize = height / 10;
    
var formatPercent = d3.format("1");

var color = d3.scaleLinear()
    //.domain(d3.min(data[d]),d3.max(data[d]))
    .domain([-1,10])
    .range(["#FFFFFF","#3a7998"]);
    //.range(["#FFFFFF", "dfecf3", "bad6e4", "#95c1d6", "#70abc8", "#4b95ba", "#3a7998", "#2c5c73", "#1e3e4e", "#102129", "#020304"]);

var svg = div
  .style("line-height", "0")
  .selectAll("svg")
  .data(d3.range(options.start, options.end))
  .enter().append("svg")
    .attr("width", width)
    .attr("height", height)
  .append("g")
    .attr("transform", "translate(" + cellSize * 3.5 + "," + (height - cellSize * 7 - 1) + ")");

svg.append("text")
    .attr("transform", "translate(-" + (6 * height / 60) + "," + cellSize * 3.5 + ")rotate(-90)")
    .attr("font-family", "sans-serif")
    .attr("font-size", 6 * height / 60 - 4)
    .attr("text-anchor", "middle")
    .text(function(d) { return d; });

var rect = svg.append("g")
    .attr("fill", "none")
    .attr("stroke", "#ccc")
    .attr("stroke-width", "0.25")
  .selectAll("rect")
  .data(function(d) { return d3.timeDays(new Date(d, 0, 1), new Date(d + 1, 0, 1)); })
  .enter().append("rect")
    .attr("width", cellSize)
    .attr("height", cellSize)
    .attr("x", function(d) { return d3.timeWeek.count(d3.timeYear(d), d) * cellSize; })
    .attr("y", function(d) { return d.getDay() * cellSize; })
    .datum(d3.timeFormat("%Y-%m-%d"));

svg.append("g")
    .attr("fill", "none")
    .attr("stroke", "#000")
    .attr("stroke-width", "0.25")
  .selectAll("path")
  .data(function(d) { return d3.timeMonths(new Date(d, 0, 1), new Date(d + 1, 0, 1)); })
  .enter().append("path")
    .attr("d", pathMonth);

r2d3.onRender(function(csv, div, width, height, options) {
  var data = d3.nest()
      .key(function(d) { return d.Date; })
      .rollup(function(d) { return d[0].sum; })
    .object(csv);

  rect.filter(function(d) { return d in data; })
      .attr("fill", function(d) { return color(data[d]); })
    .append("title")
      .text(function(d) { return d + ": " + formatPercent(data[d]); });
});

function pathMonth(t0) {
  var t1 = new Date(t0.getFullYear(), t0.getMonth() + 1, 0),
      d0 = t0.getDay(), w0 = d3.timeWeek.count(d3.timeYear(t0), t0),
      d1 = t1.getDay(), w1 = d3.timeWeek.count(d3.timeYear(t1), t1);
  return "M" + (w0 + 1) * cellSize + "," + d0 * cellSize
      + "H" + w0 * cellSize + "V" + 7 * cellSize
      + "H" + w1 * cellSize + "V" + (d1 + 1) * cellSize
      + "H" + (w1 + 1) * cellSize + "V" + 0
      + "H" + (w0 + 1) * cellSize + "Z";
}


// create plot title
// svg.append("text")
//    .attr("text-anchor", "start")
//    .attr("x", margin.middle)
//    .attr("y", margin.top - 520)
//    .attr("font-family", "sans-serif")
//    .text("Leetcode practice calendar")
//    .attr("fill", "black")
//    .attr("font-size", + 7 * height / 60)
