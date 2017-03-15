var data = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight'];
var numCols = 1;           
    
console.log("test");
    
$.each(data, function(i) {
  if(!(i%numCols)) tRow = $('<tr>');
           
  tCell = $('<td>').html(data[i]);

  $('table').append(tRow.append(tCell));
});

