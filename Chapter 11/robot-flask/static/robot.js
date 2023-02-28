// When the button is pressed the robot moves
// When the button is released the button stops
$('#forward').on('mousedown', function(){
	$.get('/forward');
	});
$('#forward').on('mouseup', function(){
	$.get('/stop');
	});
$('#backward').on('mousedown', function(){
	$.get('/backward');
	});
$('#backward').on('mouseup', function(){
	$.get('/stop');
	});
$('#left').on('mousedown', function(){
	$.get('/left');
	});
$('#left').on('mouseup', function(){
	$.get('/stop');
	});
$('#right').on('mousedown', function(){
	$.get('/right');
	});
$('#right').on('mouseup', function(){
	$.get('/stop');
	});

// This posts the value of the sliders when moved

// PWM values
var slider = document.getElementById("pwmRange");
var output = document.getElementById("pwm");
output.innerHTML = slider.value;

slider.oninput = function() {
  output.innerHTML = this.value;
};
var slider2 = document.getElementById("pwmRange2");
var output2 = document.getElementById("pwm2");
output2.innerHTML = slider4.value;

slider2.oninput = function() {
  output2.innerHTML = this.value;
}