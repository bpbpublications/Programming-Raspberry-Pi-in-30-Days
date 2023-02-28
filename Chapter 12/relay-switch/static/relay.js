// When the button is pressed the function is referenced
$('#relay1').on('mousedown', function(){
       $.get('/relay1')
       });
$('#relay2').on('mousedown', function(){
       $.get('/relay2')
       });
$('#relay3').on('mousedown', function(){
       $.get('/relay3')
       });
$('#off').on('mousedown', function(){
       $.get('/off')
       });