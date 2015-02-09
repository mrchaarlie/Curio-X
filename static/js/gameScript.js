
$(document).ready(function (e){
	// randomize which game mode it is based on session
	// between classification->counting
	//		   counting->classification
	//		   randomized
	// context reflects which mode
	//
	// 

	var coordArray = []

	$('#testImage').click(function (e) { //Offset mouse Position
        var posX = $(this).offset().left,
            posY = $(this).offset().top;
            coordArray.push({x : (e.pageX - posX) , y : (e.pageY - posY)})
            drawCircle(coordArray[coordArray.length - 1], coordArray.length)
            // each circle is a canvas element
            // TODO: need to delete circle when it is clicked, and delete associated coordinates in coordArray
            // TODO: post coordArray to persist when next image is requested
    });

    function drawCircle(data, index) {
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
	    ctx.arc(10, 10, 10, 0, Math.PI * 2); // draws a circle
	    ctx.lineWidth = 2;
	    ctx.stroke();
	}
})


