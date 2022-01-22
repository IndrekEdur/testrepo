console.log('working')
if(localStorage.getItem('cart') == null)
{
	var cart={};
}
else{
	cart= JSON.parse(localStorage.getItem('cart'));
}

$( document ).ready(function() {

    function cartLength(obj) {
        var count = 0;
        for ( var key in obj){
            count += obj[key].quantity
        }
        return count;
    }

    //javascript
    // document.getElementById("cart-items").innerHTML = cartLength(JSON.parse(localStorage.getItem('cart')));
    // jquery
    $('#cart-items').html(cartLength(JSON.parse(localStorage.getItem('cart'))));

    // jquery
    $('.add-to-cart').click(function(){
		console.log(this.dataset.pk);
        var idstr= this.dataset.pk.toString();
		// the cart attributes(quantity) is being updated
        if(cart[idstr]!= undefined) {

			quantity = cart[idstr].quantity
			price = cart[idstr].price
            cart[idstr].quantity =  quantity + 1;
            total =  cart[idstr].quantity * parseFloat(price);
            cart[idstr].total =  parseFloat(total);
        }
        else {
			// cart being inititlzied
            cart[idstr] = {quantity: 1, pk: this.dataset.pk, name: this.dataset.name,price: this.dataset.price,category: this.dataset.category,image:this.dataset.image, total:parseFloat(this.dataset.price)};
        }

        console.log(cart)
        localStorage.setItem('cart', JSON.stringify(cart));
        $('#cart-items').html(cartLength(cart));

    });
});