
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
        $ (".header").css({'display':'none'});
        $ (".intro").css({'display':'none'});
        $ (this).css({'display':'none'});
        $ (".footer").css({'display':'none'});
        $ (".footer").css({'border':'none'})
        // window.location("http://www.w3schools.com", _self);
        .queue( function(next){ 
    //          $(".title").css({'transition': '0.1s','height':'70px', 'line-height':'70px', 'font-size':'3em'});
    //           $(".header").css({'height':'108px'});
    
            window.open("game", "_self");
            next(); 
        });

        // $ (".container").css({'display':'none'});
    }); 
    
    resizeButtons();

    $( window ).resize(function(){
        resizeButtons();
    });
    
    function resizeButtons(){
        // console.log('width: ' + $('.button-container').width());;
        var tbw = $('.button-container').width();
        // console.log('resize: ' + tbw);
        $('.toggle-button').css({'height':tbw+'px'});
        $('.button-image').css({'width':tbw+'px','height':tbw+'px'});
        $('.submit').css({'width':tbw+'px','height':tbw+'px'});    
    }


    //todo


    // var name = window.location.pathname.split("/").pop().toLowerCase();
    // console.log(name);
    // console.log(name.indexOf("game"));
    // console.log(name.length);

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

        // Post the button toggle states upon submission
        $("#postClas").submit(function(e) {
                console.log('submit!')
                $('<input />').attr('type', 'hidden')
                        .attr('name', "flowerbool")
                        .attr('value', flowerBool)
                        .appendTo('#postClas');
                $('<input />').attr('type', 'hidden')
                        .attr('name', "budbool")
                        .attr('value', budBool)
                        .appendTo('#postClas');
                $('<input />').attr('type', 'hidden')
                        .attr('name', "fruitbool")
                        .attr('value', fruitBool)
                        .appendTo('#postClas');
        return true;
        })


    $(document).scroll(function() {
    })

});
