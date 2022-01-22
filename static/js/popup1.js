$(document).ready(function() {
    // all your jquery/javscript has to be in this block; if you are using jquery
    var modal = document.getElementById("myModal");
    var modalImg = document.getElementById("img01");
    var captionText = document.getElementById("caption");
    $('.product').click(function() {
        modal.style.display = "block";
        modalImg.src = $(this).attr('src');
        captionText.innerHTML = $(this).attr('alt');
    });
    $('.close').click(function() {
        modal.style.display = "none";
    });

    $('.add_to_cart').click(function() {
        var cart_items = $("#cart_items").html()
        cart_items = parseInt(cart_items) + 1
        $("#cart_items").html(cart_items)
    });

});
     //javascript 
    // var myFunction = function(){
    //     alert("ho ho ho");
    // }
    // var classname = document.getElementsByClassName("product");

    // for (var i = 0; i < classname.length; i++) {
    //     classname[i].addEventListener('click', myFunction);
    // }