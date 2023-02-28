// Here it references the button id
// Mousedown means that when the mouse is clicked
// The click route is referenced
// In other words when the button is clicked the
// Action is performed
$('#button').on('mousedown', function(){
       $.get('/click')
       });