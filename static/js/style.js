
$(document).ready(function () {

    $( ".login-button" ).click(function() {
    //TODO

    });

    $( ".toggle-button" ).click(function() {
    //TODO
       
    });

    $( ".begin-button" ).click(function() {
      // $("#beginButton").animate({
      
      //   height: "200px",
      //   },500);
      // $( this ).css({'border-radius':'100px','width':'100px', 'height':'100px'});
        $ ("body").css({'background-color':'#dadede', 'color':'#dadede'});
        $ ("h1").css({'border':'none'});
        $ (".header").css({'display':'none'})
        $ (".footer").css({'border':'none'}).delay(250)
        // window.location("http://www.w3schools.com", _self);
        .queue( function(next){ 
    //          $(".title").css({'transition': '0.1s','height':'70px', 'line-height':'70px', 'font-size':'3em'});
    //           $(".header").css({'height':'108px'});
    
            window.open("game", "_self");
            next(); 
        });

        // $ (".container").css({'display':'none'});
    });

    var tbw = $('.toggle-button').width();
    $('.toggle-button').css({'height':tbw+'px'});
    $('.button-image').css({'width':tbw+'px','height':tbw+'px'});
    $('.submit').css({'width':tbw+'px','height':tbw+'px'});

    // $( "toggle-button" ).on( "click", function() {
    //   var tc = this.className || undefined;
    //   divs.toggleClass( tc );
    //   appendClass();
    // });

    $( ".toggle-button" ).click(function() {
        $(this).parent().toggleClass( "selected" , 1000, "easeOut");
    });

    $(document).scroll(function() {
    })

});
