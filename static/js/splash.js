$(document).ready(function () {


    // window.setTimeout($(".highlight").css({'border':'2px solid #15CABD'}),1000);

    $(".highlight")
    .delay(5000)
      .queue(function(next){ 
        $(this).css({'border':'2px solid #15CABD'});
        next();
      })
    .delay(3000)
      .queue( function(next){ 
        $(this).css({'border':'2px solid #2a2a2a'});
        next();
      });

    $( "#back-button" ).click(function() {
        window.open("index", "_self");
    });

    $( "#game-button" ).click(function() {
        window.open("game", "_self");
    });

    $( "#game2-button" ).click(function() {
        window.open("game2", "_self");
    });
    
});
