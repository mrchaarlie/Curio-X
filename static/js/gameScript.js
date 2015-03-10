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

	if ($('.toggle-button').length > 0){

        var flowerBool = 0;
        var budBool = 0;
        var fruitBool = 0;

        if($("#flower-button").click(function(){
            flowerBool += 1;
            flowerBool = flowerBool % 2;
        }));
        if($("#bud-button").click(function(){
            budBool += 1;
            budBool = budBool % 2;
        }));
        if($("#fruit-button").click(function(){
            fruitBool += 1;
            fruitBool = fruitBool % 2;
        }));

        $( ".toggle-button" ).click(function() {
            $(this).parent().toggleClass( "selected" , 1000, "easeOut");
        }); 

        //Submit click code:
        var clickSubmit = "{flower:"+flowerBool+", bud:"+budBool+", fruit:"+fruitBool+"}";
    }

	$("#postForm").submit(function(e) {
		console.log('submit!')

		// send in type, count and location
		// view provides: user, timestamp, imageID?

		$('<input />').attr('type', 'hidden')
			.attr('name', "count").attr('value',cArray.length).appendTo('#postForm')
		$('<input />').attr('type', 'hidden')
			.attr('name', "coords").attr('value',cArray.map(function(c){return '('+c.x+','+c.y+')'}).toString())
			.appendTo('#postForm')
        $('<input />').attr('type', 'hidden')
	        .attr('name', "flowerbool")
	        .attr('value', flowerBool)
	        .appendTo('#postForm');
        $('<input />').attr('type', 'hidden')
            .attr('name', "budbool")
            .attr('value', budBool)
            .appendTo('#postForm');
        $('<input />').attr('type', 'hidden')
            .attr('name', "fruitbool")
            .attr('value', fruitBool)
            .appendTo('#postForm');

      	return true;
	})
})

