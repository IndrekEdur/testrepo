$( document ).ready(function() {

	var html = ""
	    html += "<tr>";
        html += "<th style='width: 10%' >PK</th>";
        html += "<th style='width: 10%' >Image</th>";
        html += "<th style='width: 20%' >Name</th>";
        html += "<th style='width: 10%; text-align: center' >Quantity</th>";
        html += "<th style='text-align: right; padding-right: 20px; width: 10%'>Price €</th>";
        html += "<th style='width: 10%; text-align: center' >Category</th>";
        html += "<th style='text-align: right; padding-right: 20px'; width: 5%>Total €</th>";
        html += "<th style='width: 20%' >Delete</th>";
        html += "</tr>";
	for (product in cart ) {
	    html += "<tr>";
		html += "<td style='width: 10%; vertical-align: middle' >"+ cart[product].pk+"</td>";
		html += "<td style='width: 10%; vertical-align: middle; padding: 1px' ><img src="+ cart[product].image+" height=50 style='padding: 1px' class='product'  alt='My image'></td>"
		html += "<td style='width: 20%; vertical-align: middle' >"+ cart[product].name+"</td>";
		html += "<td style='width: 10%; text-align: center; vertical-align: middle' >"+ cart[product].quantity+"</td>";
		html += "<td style='text-align: right; padding-right: 20px; width: 10%; vertical-align: middle'>"+ cart[product].price+"</td>";
		html += "<td style='width: 10%; text-align: center; vertical-align: middle' >"+ cart[product].category+"</td>";
		html += "<td style='text-align: right; padding-right: 20px; width: 5%; vertical-align: middle'><span id='total-amount'> "+productTotal(product)+"</span></td>";
        html += "<td style='width: 20%; vertical-align: middle' ><button class='btn remove-from-cart' data-id='"+product+"'><i class='fa fa-trash'></i></button></td>"
		html += "<br/>";
		html += "</tr>";
	}
	html += "<tr>";
    html += "<td colspan='5'></td> <td style='text-align: center; padding-right: 0px; padding-left: 0px'> <b style='text-align: right; padding: 0px'>Cart Total:</b></td>"
    html += "<td style='text-align: right; text:bold; padding-right: 20px'; width: 5%><span id='total-amount' ><b> "+calculate_total()+" </b></span></td>"
    html += "</tr>";

	$('#display-cart').html(html)

    $('.remove-from-cart').click(function(){
        if(cart[this.dataset.id].quantity === 1){
            delete cart[this.dataset.id]
        }else{
            cart[this.dataset.id].quantity = cart[this.dataset.id].quantity - 1
        }
        localStorage.setItem('cart', JSON.stringify(cart));
        // reloads the page from cache, faster but not up to date
        // location.reload();
        // reloads the page from server, slower but always uptp date
        location.reload(true);
    });

    function calculate_total(){
        var sum = 0;
        for (item in cart){
            sum += cart[item].quantity * cart[item].price
        }
        return parseFloat(sum).toFixed(2);
    }

    function productTotal(item){
        var sum = 0;
            sum += cart[item].quantity * cart[item].price
        return parseFloat(sum).toFixed(2);
    }

    function cartTotal(obj) {
        var count = 0;
        for ( var key in obj){
            count += obj[key].total
        }
        return count;
    }

    $('#cart-total').html(cartTotal(JSON.parse(localStorage.getItem('cart'))));

});