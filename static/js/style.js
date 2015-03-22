
$(document).ready(function () {

    $( ".login-button" ).click(function() {
    //TODO
    });

    resizeSplash();

    if ($('.intro').length>0){
        $('.intro').append('<div class="preload"></div>');
    }

    function resizeSplash(){
        if ($('.splash').length > 0){
            var mainHeight = $(window).height();
            $('.splash').css({'height':mainHeight-220});
        };
    }

    //remove loading icon
    $('#testImage').load(function(e){
        $('.loading').remove();
    })

    $( ".login-button" ).click(function() {
    //TODO
    });

    $( ".toggle-button" ).click(function() {
    //TODO
    });

    $( ".begin-button" ).click(function() {
     
    //     $ ("body").css({'background-color':'#dadede', 'color':'#dadede'});
    //     $ ("h1").css({'border':'none'});
    //     $ (".header").css({'display':'none'});
    //     $ (".intro").css({'display':'none'});
    //     $ (this).css({'display':'none'});
    //     $ (".footer").css({'display':'none'});
    //     $ (".footer").css({'border':'none'})
        // .queue( function(next){ 
    
            // window.open("game-splash", "_self");
            // next(); 
        // });

    }); 
    
    resizeButtons();
    
    function resizeButtons(){
        // console.log('width: ' + $('.button-container').width());;
        var tbw = $('.button-container').width();
        // console.log('resize: ' + tbw);
        $('.toggle-button').css({'height':tbw+'px'});
        $('.button-image').css({'width':tbw+'px','height':tbw+'px'});
        $('.submit').css({'width':tbw+'px','height':tbw+'px'});    
    }

    $( window ).resize(function(){
        resizeButtons();
        resizeSplash();
    });

    //todo


    // var name = window.location.pathname.split("/").pop().toLowerCase();
    // console.log(name);
    // console.log(name.indexOf("game"));
    // console.log(name.length);

    if ($('.toggle-button').length > 0){

        var flowerBool = 0;
        var budBool = 0;
        var fruitBool = 0;

        $(".button-container").click(function(){
            if ($(this).find(".toggle-button").is('#flower-button')){
                flowerBool += 1;
                flowerBool = flowerBool % 2;
            }else if($(this).find(".toggle-button").is('#bud-button')){

                budBool += 1;
                budBool = budBool % 2;
            }else if($(this).find(".toggle-button").is('#fruit-button')){
                fruitBool += 1;
                fruitBool = fruitBool % 2;
            }
            $(this).toggleClass( "selected" , 1000, "easeOut");
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
