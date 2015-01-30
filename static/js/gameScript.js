
$(document).ready(function (e){
	// randomize which game mode it is based on session
	// between classification->counting
	//		   counting->classification
	//		   randomized
	// context reflects which mode

	var coordArray = []

	$('#testImage').click(function (e) { //Offset mouse Position
        var posX = $(this).offset().left,
            posY = $(this).offset().top;
            coordArray.push({x : (e.pageX - posX) , y : (e.pageY - posY)})
            drawCircle(coordArray[coordArray.length - 1], coordArray.length)
    });

    function drawCircle(data, index) {
  //   	var canvas = document.createElement('canvas');
		// canvas.id = "circle" + index;
		// canvas.width = 30;
		// canvas.height = 30;
		// canvas.style.zIndex = 8;
		// canvas.style.position = "absolute";

		var elementID = 'circle' + index;
	    $('<canvas>').attr({
	        id: elementID
	    }).css({
	        width: 20 + 'px',
	        height: 20 + 'px',
	        left: data.x - 10,
	        top : data.y - 10
	    }).appendTo('#panzoomParent');

	    var ctx = document.getElementById(elementID);
	    ctx = ctx.getContext('2d')

    	console.log(data)
    	ctx.beginPath();
	    ctx.arc(data.x, data.y, 10, 0, Math.PI * 2); // 0 - 2pi is a full circle
	    ctx.lineWidth = 2;
	    ctx.stroke();
	}
})


