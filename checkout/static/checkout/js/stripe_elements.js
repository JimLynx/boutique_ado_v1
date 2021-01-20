/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// Script elements in checkout.html contain values with text 
// Get their ids and using the .text function.
// Slice off first and last character on to remove quotation marks
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
//  client secret from the template using a jQuery
var client_secret = $('#id_client_secret').text().slice(1, -1);

// gets JS from stripe script
var stripe = Stripe(stripe_public_key);

// instance of stripe elements
var elements = stripe.elements();

// add style variable
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

//create a card element
var card = elements.create('card', {style: style});

// mount the card element to the div in payment fieldset
card.mount('#card-element');





