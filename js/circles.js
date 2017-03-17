/*
var data = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight'];
var numCols = 1;           
    
console.log("test");
console.log(d3);
    
$.each(data, function(i) {
  if(!(i%numCols)) tRow = $('<tr>');
           
  tCell = $('<td>').html(data[i]);

  $('table').append(tRow.append(tCell));
});

var circle = d3.selectAll("circle");
console.log(circle);
circle.style("fill", "steelblue");
circle.attr("r", 30);

var body = d3.select("body");
var nothing = d3.select("#wut");
debugger;
*/


var data = [1,2,3,4,5]

var body = d3.select("body")
var nothing = d3.select("#wut")

//shouldn't be called
var noparent = nothing.selectAll("div").data(data, function(d){
    alert("no parent CALLED"); return d;
})

var nodata = body.selectAll("div").data([], function(d){
    alert("no data CALLED"); 
    return d;
})

var wrongdata = body.selectAll("div").data({banana:2, apple:3}, function(d){
    alert("wrong data CALLED"); 
    return d;
})

//should be called
var noenter = body.selectAll("div").data(data, function(d){
    alert("no enter CALLED"); 
    return d;
})

var nodes = body.selectAll("div").data(data, function(d){
    alert("normal CALLED"); 
    return d;
}).enter().append("div")
  .text(function(d){ return d})
