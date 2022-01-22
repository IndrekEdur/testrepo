$( document ).ready(function() {

	var html = ""
	    html += "<tr>";
        html += "<th>Name</th>";
        html += "<th>Price</th>";
        html += "<th>Quantity</th>";
        html += "<th>Total</th>";
        html += "</tr>";
	for (product in cart ) {
	    html += "<tr>";
		html += "<td>"+ cart[product].name+"</td>";
		html += "<td>"+ cart[product].price+"</td>";
		html += "<td>"+ cart[product].quantity+"</td>";
		html += "<td><span id='total-amount'> "+productTotal(product)+"</span></td>";
		html += "<br/>";
		html += "</tr>";
	}


	$('#display-checkout').html(html)

    function productTotal(item){
        var sum = 0;
            sum += cart[item].quantity * cart[item].price
        return parseFloat(sum).toFixed(2);
    }

    function calculate_total(){
        var sum = 0;
        for (item in cart){
            sum += cart[item].quantity * cart[item].price
        }
        return parseFloat(sum).toFixed(2);
    }

    $('#cart-total').html(calculate_total(JSON.parse(localStorage.getItem('cart'))));
});