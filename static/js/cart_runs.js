
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

    var initial_cart = $.session.get('name')

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
  });

  $('#ok_btn').click(function(e) {
    e.preventDefault();
    //do other stuff when a click happens
});
 