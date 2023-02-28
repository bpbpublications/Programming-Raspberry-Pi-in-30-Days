// When the button is pressed the function is referenced
$('#on').on('mousedown', function(){
       $.get('/on')
       });
$('#off').on('mousedown', function(){
       $.get('/off')
       });