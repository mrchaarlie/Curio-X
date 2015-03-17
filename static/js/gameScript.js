$(document).ready(function (e){

	var isDraw = 0;
	var globalScale = 0;
	var globalImgWidth = 0;
	var globalImgHeight = 0;
	var globalDownX = 0;
	var globalDownY = 0;

	$('#testImage').load(function(e){
		drawCanvas();
		isDraw++;
	})
	setTimeout(function(){ 
		if(!isDraw){
			drawCanvas();
		}
	 }, 1000);

	function drawCanvas(){
		console.log('draw ready');
		var cArray = []
		var radius = 10;
		var canvas = document.getElementById('circleCanvas');
		var ctx = canvas.getContext('2d');

		// var width=720;
		// var height=1080;
		resizeCanvas();
		$( window ).resize(function(){
        	resizeCanvas();
   		});

		function resizeCanvas(){
			var imgWidth = globalImgWidth = $('#testImage').width();
			var imgHeight = globalImgHeight = $('#testImage').height();
			
			// console.log(width+', ' + height);
			// alert(imgWidth+', ' + imgHeight);
			canvas.width=imgWidth;
			canvas.height=imgHeight;

			// canvas.width=420;
			// canvas.height=720;	
			drawCircles();
		}
		
		$('.panzoom-parent').click(function(e){
			var posX = $(this).offset().left,
				posY = $(this).offset().top;
			
			var canvasArray = $("#circleCanvas").attr("style").split(',');
			globalScale = canvasArray[3];
			drawCircles();
		})

		$('.panzoom-parent').on('mousewheel.focal', function( e ) {
			console.log('scrolling')
			var canvasArray = $("#circleCanvas").attr("style").split(',');
			globalScale = canvasArray[3];
			drawCircles();
		})

		$('#circleCanvas').mousedown(function (e) {
			// console.log('mousedown')
			var posX = $(this).offset().left,
				posY = $(this).offset().top;

			globalDownX = e.pageX - posX;
			globalDownY = e.pageY - posY;
		});

		$('#circleCanvas').mouseup(function (e) {
			// console.log('mouseup')
			var posX = $(this).offset().left,
				posY = $(this).offset().top;

			if(e.pageX-posX === globalDownX && e.pageY-posY === globalDownY) {
				// console.log('same spot click')
				var coord = {cType : getType(),
					x : (globalDownX / globalScale)/globalImgWidth,
					y : (globalDownY / globalScale)/globalImgHeight
				};
				cArrayUpdate(coord);
				drawCircles();
			}
		})

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
			var dx = (p2.x-p1.x)*globalImgWidth;
			var dy = (p2.y-p1.y)*globalImgHeight;
			return (Math.sqrt(dx*dx + dy*dy) <= radius);
		}

		
		function drawCircles(){
			// console.log('drawing circles, ' + "(dx,dy) " + globalXOffset + ', ' + globalYOffset);
			ctx.clearRect(0,0, canvas.width, canvas.height);
			$.each(cArray, function(i, data) {
				ctx.beginPath();
				// xScalingFactor = globalXOffset*Math.sqrt(globalScale-1)
				// yScalingFactor = globalYOffset*Math.sqrt(globalScale-1)
				xPos = data.x * globalImgWidth;
				yPos = data.y * globalImgHeight;
				// console.log("(dx,dy) " + xScalingFactor + ', ' + yScalingFactor)
				ctx.arc(xPos, yPos, radius, 0, Math.PI * 2);
				// ctx.arc(data.x, data.y, radius, 0, Math.PI * 2);
				ctx.lineWidth = 2;
				if(data.cType == 'flower'){ ctx.strokeStyle = 'rgb(192, 43, 96)'; }
				else if(data.cType == 'bud'){ ctx.strokeStyle = 'rgb(219, 130, 50)'; }
				else if(data.cType == 'fruit'){ ctx.strokeStyle = 'rgb(52, 214, 18)'; }
				ctx.stroke();
			});
		}

		if ($('.toggle-button').length > 0){

	        var flowerBool = 0;
	        var budBool = 0;
	        var fruitBool = 0;

	        $("#flower-button").click(function(){
	        	$("#flower-button").parent().addClass( "selected" , 1000, "easeOut");
	            if(budBool) { $("#bud-button").parent().removeClass( "selected" , 1000, "easeOut") }
	            if(fruitBool) { $("#fruit-button").parent().removeClass( "selected" , 1000, "easeOut") }
	            
	            flowerBool = 1;
	            budBool = fruitBool = 0;
	            // console.log("{flower:"+flowerBool+", bud:"+budBool+", fruit:"+fruitBool+"}")
	        });
	        $("#bud-button").click(function(){
	        	$("#bud-button").parent().addClass( "selected" , 1000, "easeOut");
	            if(flowerBool) { $("#flower-button").parent().removeClass( "selected" , 1000, "easeOut"); }
	            if(fruitBool) { $("#fruit-button").parent().removeClass( "selected" , 1000, "easeOut"); }
	            budBool = 1;
	            flowerBool = fruitBool = 0;
	            // console.log("{flower:"+flowerBool+", bud:"+budBool+", fruit:"+fruitBool+"}")
	        });
	        $("#fruit-button").click(function(){
	        	$("#fruit-button").parent().addClass( "selected" , 1000, "easeOut");
	            if(flowerBool) { $("#flower-button").parent().removeClass( "selected" , 1000, "easeOut"); }
	            if(budBool) { $("#bud-button").parent().removeClass( "selected" , 1000, "easeOut"); }
	            fruitBool = 1;
	            flowerBool = budBool = 0;
	            // console.log("{flower:"+flowerBool+", bud:"+budBool+", fruit:"+fruitBool+"}")
	        });

	        // $( ".toggle-button" ).click(function() {
	        //     $(this).parent().toggleClass( "selected" , 1000, "easeOut");
	        // });
	    }

	    function getType() {
			if (flowerBool) {return 'flower'}
			else if (budBool) {return 'bud'}
			else if (fruitBool) {return 'fruit'}
		}
	    	// __init
		$('#flower-button').click();

		$("#postForm").submit(function(e) {
			console.log('submit!')

			// send in type, count and location
			// view provides: user, timestamp, imageID?

			$('<input />').attr('type', 'hidden')
				.attr('name', "count")
				.attr('value',cArray.length)
				.appendTo('#postForm')
			$('<input />').attr('type', 'hidden')
				.attr('name', "coords")
				.attr('value',cArray.map(function(c){return '('+c.cType+':'+c.x+','+c.y+')'}).toString())
				.appendTo('#postForm')
	      	return true;
		})
	}
})

