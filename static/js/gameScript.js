$(document).ready(function (e){

	var isDraw = 0;
	var globalScale = 0;
	var globalXOffset = 35;
	var globalYOffset = -140;
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
		var radius = 15;
		var canvas = document.getElementById('circleCanvas');
		var ctx = canvas.getContext('2d');

		// var width=720;
		// var height=1080;
		resizeCanvas();
		$( window ).resize(function(){
        	resizeCanvas();
   		});

		function resizeCanvas(){
			var width = $('.main').width();
			var height = $('.main').height();
			
			canvas.width=width;
			canvas.height=height;
			// canvas.width=420;
			// canvas.height=720;	
			drawCircles();
		}		
		// $('#circleCanvas').css({'width':width+'px','height':height+'px'});
		// img.src = document.getElementById('testImage');
		// img.onload = function(){
			// ctx.drawImage(img,0,0)
			// console.log('drawing image')
		// }
		
		$('#circleCanvas').mousedown(function (e) {
			// console.log('mousedown')
			var posX = $(this).offset().left,
				posY = $(this).offset().top;

			globalDownX = e.pageX - posX
			globalDownY = e.pageY - posY
		});

		$('#circleCanvas').mouseup(function (e) {
			// console.log('mouseup')
			var posX = $(this).offset().left,
				posY = $(this).offset().top;

			if(e.pageX-posX == globalDownX && e.pageY-posY == globalDownY) {
				// console.log('same spot click')
				var coord = {cType : getType() , x : (globalDownX) , y : (globalDownY)};
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
			var dx = p2.x-p1.x;
			var dy = p2.y-p1.y;
			return (Math.sqrt(dx*dx + dy*dy) <= radius);
		}

		
		function drawCircles(){
			console.log('drawing circles, ' + "(dx,dy) " + globalXOffset + ', ' + globalYOffset);
			ctx.clearRect(0,0, canvas.width, canvas.height);
			$.each(cArray, function(i, data) {
				ctx.beginPath();
				xScalingFactor = globalXOffset*(globalScale-1)
				yScalingFactor = globalYOffset*(globalScale-1)
				xPos = data.x + xScalingFactor;
				yPos = data.y + yScalingFactor;
				// console.log("(dx,dy) " + xScalingFactor + ', ' + yScalingFactor)
				ctx.arc(xPos, yPos, radius, 0, Math.PI * 2);
				ctx.arc(data.x, data.y, radius, 0, Math.PI * 2);
				ctx.lineWidth = 2;
				if(data.cType == 'flower'){ ctx.strokeStyle = 'rgb(192, 43, 96)'; }
				else if(data.cType == 'bud'){ ctx.strokeStyle = 'rgb(219, 130, 50)'; }
				else if(data.cType == 'fruit'){ ctx.strokeStyle = 'rgb(52, 214, 18)'; }
				ctx.stroke();
			});
		}

		$('.panzoom-parent').click(function(e){
			var posX = $(this).offset().left,
				posY = $(this).offset().top;
			
			// globalXOffset = (e.pageX - globalDownX)
			// globalYOffset = (e.pageY - globalDownY)

			var canvasArray = $("#circleCanvas").attr("style").split(',');
			// console.log("scale: "+canvasArray[3]);
			// console.log("x: "+canvasArray[4]);
			// console.log("y: "+canvasArray[5].split(')')[0]);
			globalScale = canvasArray[3];
			// globalXOffset = canvasArray[4];
			// globalYOffset = canvasArray[5].split(')')[0];
			drawCircles();
		})
		$('.panzoom-parent').scroll(function(e) {
			console.log('scrolling')
			drawCircles();
		})


		if ($('.toggle-button').length > 0){

	        var flowerBool = 0;
	        var budBool = 0;
	        var fruitBool = 0;

	        $("#flower-button").click(function(){
	        	$("#flower-button").parent().addClass( "selected" , 1000, "easeOut");
	            if(budBool) { $("#bud-button").parent().toggleClass( "selected" , 1000, "easeOut") }
	            if(fruitBool) { $("#fruit-button").parent().toggleClass( "selected" , 1000, "easeOut") }
	            
	            flowerBool = 1;
	            budBool = fruitBool = 0;
	            console.log("{flower:"+flowerBool+", bud:"+budBool+", fruit:"+fruitBool+"}")
	        });
	        $("#bud-button").click(function(){
	        	$("#bud-button").parent().addClass( "selected" , 1000, "easeOut");
	            if(flowerBool) { $("#flower-button").parent().toggleClass( "selected" , 1000, "easeOut"); }
	            if(fruitBool) { $("#fruit-button").parent().toggleClass( "selected" , 1000, "easeOut"); }
	            budBool = 1;
	            flowerBool = fruitBool = 0;
	            console.log("{flower:"+flowerBool+", bud:"+budBool+", fruit:"+fruitBool+"}")
	        });
	        $("#fruit-button").click(function(){
	        	$("#fruit-button").parent().addClass( "selected" , 1000, "easeOut");
	            if(flowerBool) { $("#flower-button").parent().toggleClass( "selected" , 1000, "easeOut"); }
	            if(budBool) { $("#bud-button").parent().toggleClass( "selected" , 1000, "easeOut"); }
	            fruitBool = 1;
	            flowerBool = budBool = 0;
	            console.log("{flower:"+flowerBool+", bud:"+budBool+", fruit:"+fruitBool+"}")
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

