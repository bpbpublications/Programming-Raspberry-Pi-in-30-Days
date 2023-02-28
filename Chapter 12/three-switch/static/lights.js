// When the button is pressed the function is referenced
$('#kitchen').on('mousedown', function(){
       $.get('/kitchen')
       });
$('#livingroom').on('mousedown', function(){
       $.get('/livingroom')
       });
$('#bedroom').on('mousedown', function(){
       $.get('/bedroom')
       });
$('#off').on('mousedown', function(){
       $.get('/off')
       });