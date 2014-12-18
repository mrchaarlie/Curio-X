(function ($) {

var isSmall = 0;

$.fn.myfunction = function() {
      alert('hello world');
      return this;
   }; 

$(document).scroll(function() {

    // console.log($(document).scrollTop());
    // console.log(isSmall);
    if($(document).scrollTop() >= 90 && isSmall == 0){
    	// $().myfunction();
    	isSmall = 1;
    	$(".title").css({'position':'fixed', 'width': '100%', 'box-shadow':'none', 'text-shadow':'rgb(59, 59, 59) 2px 2px'})
    	.delay(300)
    	.queue( function(next){ 
    		$(".title").css({'transition': '0.3s ease','height':'70px', 'line-height':'70px', 'font-size':'3em'});
    		next();
    	});
 
    }else if ($(document).scrollTop() < 90 && isSmall == 1){
    	isSmall = 0;
    	$(".title").css({'position':'relative', 'height':'150px', 'line-height':'145px', 'font-size':'4em', 'box-shadow':'0px 0px 61px 4px rgba(34,34,34,0.73)', 'text-shadow':'rgb(59, 59, 59) 1px 1px,rgb(59, 59, 59) 2px 2px,rgb(59, 59, 59) 3px 3px,rgb(60, 60, 60) 4px 4px,rgb(60, 60, 60) 5px 5px,rgb(61, 61, 61) 6px 6px,rgb(61, 61, 61) 7px 7px,rgb(62, 62, 62) 8px 8px,rgb(62, 62, 62) 9px 9px,rgb(62, 62, 62) 10px 10px,rgb(63, 63, 63) 11px 11px,rgb(63, 63, 63) 12px 12px,rgb(64, 64, 64) 13px 13px,rgb(64, 64, 64) 14px 14px,rgb(65, 65, 65) 15px 15px,rgb(65, 65, 65) 16px 16px,rgb(65, 65, 65) 17px 17px,rgb(66, 66, 66) 18px 18px,rgb(66, 66, 66) 19px 19px,rgb(67, 67, 67) 20px 20px,rgb(67, 67, 67) 21px 21px,rgb(68, 68, 68) 22px 22px' })
		.delay(300)
    	.queue( function(next){ 
    		$(".title").css({'transition': '0.3s ease','width': '300px'});
    		next();
    	});
    }
})



})(jQuery);

