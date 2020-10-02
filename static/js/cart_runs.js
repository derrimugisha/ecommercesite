
  $(function () {

    var goToCartIcon = function($addTocartBtn){
      var $cartIcon = $(".my-cart-icon");
      var $image = $('<img width="30px" height="30px" src="' + $addTocartBtn.data("image") + '"/>').css({"position": "fixed", "z-index": "999"});
      $addTocartBtn.prepend($image);
      var position = $cartIcon.position();
      $image.animate({
        top: position.top,
        right: position.right
      }, 500 , "linear", function() {
        $image.remove();
      });
    }
    var empty_array = []
    $.session.set('name',JSON.stringify(empty_array))

    let initial_cart = $.session.get('name')

    $('.my-cart-btn').myCart({
      currencySymbol: 'UGX',
      classCartIcon: 'my-cart-icon',
      classCartBadge: 'my-cart-badge',
      classProductQuantity: 'my-product-quantity',
      classProductRemove: 'my-product-remove',
      classCheckoutCart: 'my-cart-checkout',
      affixCartIcon: true,
      showCheckoutModal: true,
      numberOfDecimals: 2,
      cartItems: initial_cart,
      clickOnAddToCart: function($addTocart){
        goToCartIcon($addTocart);
      },
      afterAddOnCart: function(products, totalPrice, totalQuantity) {
         $.session.set('name',JSON.stringify(products))
         initial_cart = $.session.get('name')
        console.log("afterAddOnCart", products, totalPrice, totalQuantity);
        console.log("****", initial_cart,'****')
        return initial_cart
        
        
      },
      clickOnCartIcon: function($cartIcon, products, totalPrice, totalQuantity) {
        console.log("cart icon clicked", $cartIcon, products, totalPrice, totalQuantity);
      },
      checkoutCart: function(products, totalPrice, totalQuantity) {
        var checkoutString = "Total Price: " + totalPrice + "\nTotal Quantity: " + totalQuantity;
        checkoutString += "\n\n id \t name \t summary \t price \t quantity \t image path";
        $.each(products, function(){
          checkoutString += ("\n " + this.id + " \t " + this.name + " \t " + this.summary + " \t " + this.price + " \t " + this.quantity + " \t " + this.image);
        });
        alert(checkoutString)
        console.log("checking out", products, totalPrice, totalQuantity);

        
        
        //intergrating payment
        function makePayment() {
          FlutterwaveCheckout({
            public_key: "FLWPUBK_TEST-80b26435f9ef9c9f986a66d40594c4e2-X",
            tx_ref: "hooli-tx-1920bbtyt",
            amount: totalPrice,
            currency: "UGX",
            payment_options: "card, mobile_money_uganda, ussd",
            redirect_url: // specified redirect URL
              "http://127.0.0.1:2020/successfull",
            meta: {
              consumer_id: 23,
              consumer_mac: "92a3-912ba-1192a",
            },
            customer: {
              email: "derrimugisha@gmail.com",
              phone_number: "0704838784",
              name: "Mugisha Derrick",
            },
            callback: function (data) {
              console.log(data);
            },
            onclose: function() {
              // close modal
            },
            customizations: {
              title: "ClairesShop",
              description: "Payment for items in cart",
              logo: "{% static 'images/claireslogo.png' %}",
            },
          });
        }
        //end of intergrating payment
        
        // run the function
        makePayment()

      },
    //   getDiscountPrice: function(products, totalPrice, totalQuantity) {
    //     console.log("calculating discount", products, totalPrice, totalQuantity);
    //     return totalPrice * 0.5;
    //   }
    
    });

    

    $("#addNewProduct").click(function(event) {
      var currentElementNo = $(".row").children().length + 1;
      $(".row").append('<div class="col-md-3 text-center"><img src="images/img_empty.png" width="150px" height="150px"><br>product ' + currentElementNo + ' - <strong>$' + currentElementNo + '</strong><br><button class="btn btn-danger my-cart-btn" data-id="' + currentElementNo + '" data-name="product ' + currentElementNo + '" data-summary="summary ' + currentElementNo + '" data-price="' + currentElementNo + '" data-quantity="1" data-image="images/img_empty.png">Add to Cart</button><a href="#" class="btn btn-info">Details</a></div>')
    });

    // $('#cart_show').append('<div>'+full_cart+'</div>')
    detailviewcart()


  });

  $('#ok_btn').click(function(e) {
    e.preventDefault();
    //do other stuff when a click happens
});

$('.my-cart-icon').click(function(e){
  e.preventDefault()
})

// displaying table for the address detailview
function detailviewcart(){

  let products = JSON.parse(localStorage.products);

    let products_leng = products.length

    // let sa = objectholder(products[0])

    

    console.log("**** am there *****")


    for(let x1=0; x1<products_leng; x1++)
    {
      let tablerow = products[x1]
      
      let tabledata = Object.values(tablerow)


      $("#tablebody").append("<tr id='"+x1+ "'>"+
              "</tr>")
      let data_leng = tabledata.length

      console.log("hh "+data_leng+" hh")

      

      $("#"+x1).append("<td>"+"<img src='"+tabledata[5]+"'style='width:60px'>"+"</td>"+
      "<td>"+tabledata[1]+"</td>"+
      "<td>"+tabledata[4]+"</td>"+
      "<td id='ggg'>"+" "+tabledata[3]*tabledata[4]+"</td>" )
  

    }

    var totals=[0];
        $(document).ready(function(){

            var $dataRows=$("table tr");

            $dataRows.each(function() {
                $(this).find('#ggg').each(function(i)
                {        
                    totals[i]+=parseInt( $(this).html());
                });
            });
            $("#total").each(function(i){  
                $(this).html("<b>total:</b>"+totals[i]);
            });

        });
  
}

function add(){

  

}