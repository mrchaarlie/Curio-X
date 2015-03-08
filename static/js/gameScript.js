$(document).ready(function (e){
	var cArray = []
	var radius = 15;
	var canvas = document.getElementById('circleCanvas')
	var ctx = canvas.getContext('2d');
	var img = new Image();

	// var width=720;
	// var height=1080;
	var width = $('.main').width();
	var height = $('.main').height();
	canvas.width=width;
	canvas.height=height;
	console.log(canvas);
	// $('#circleCanvas').css({'width':width+'px','height':height+'px'});
	// img.src = document.getElementById('testImage');
	// img.onload = function(){
		// ctx.drawImage(img,0,0)
		// console.log('drawing image')
	// }
	
	$('#circleCanvas').click(function (e) {
		var posX = $(this).offset().left,
			posY = $(this).offset().top;
		
		var coord = {x : (e.pageX - posX) , y : (e.pageY - posY)};
		
		cArrayUpdate(coord);
		drawCircles();
		console.log('coordsArray', cArray)
	});
	
	function cArrayUpdate(newCoord) {
		var noOverlap = true;
		$.each(cArray, function(i, coord) {
			if (isClose(newCoord, coord)) {
				cArray.splice(i,1);
				return noOverlap = false;
			}
		});
		if(noOverlap) { cArray.push(newCoord) }
	}
	
	function isClose(p1, p2){
		var dx = p2.x-p1.x;
		var dy = p2.y-p1.y;
		return (Math.sqrt(dx*dx + dy*dy) <= radius);
	}

	
	function drawCircles(){
		console.log('drawing circles');
		ctx.clearRect(0,0, canvas.width, canvas.height);
		$.each(cArray, function(i, data) {
			ctx.beginPath();
			ctx.arc(data.x, data.y, radius, 0, Math.PI * 2);
			ctx.lineWidth = 2;
			ctx.strokeStyle = 'red';
			ctx.stroke();
		});
	}

	$("#submit-button").click(function() {
		var data = {user: 'user', // get user from context
			coords: cArray}; // etc. everything else
		var url = '/submit/game2_submit_task'
		$.post(url, data)
	})
})


