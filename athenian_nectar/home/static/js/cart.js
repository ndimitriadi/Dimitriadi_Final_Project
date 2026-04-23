document.addEventListener('DOMContentLoaded', function() {
    const cardName = document.querySelector('#card-name');
    const cardNumber = document.querySelector('#card-number');
    const cardExpiry = document.querySelector('#card-expiry');
    const cardCvv = document.querySelector('#card-cvv');
    const paymentForm = document.querySelector('#payment-form');
    const errorBox = document.querySelector('#payment-error');

    

    //card number
    cardNumber.addEventListener('input', function(e) {
        //only numbers allowed
        let value = e.target.value.replace(/\D/g, '');
        //space after every 4 numbers
        value = value.replace(/(.{4})/g, '$1 ').trim();
        e.target.value = value;

        cardNumber.style.borderColor = '#ddd'; 
        errorBox.style.display = 'none';
    });

    cardNumber.addEventListener('blur', function(e) {
 
        if (cardNumber.value.length > 0 && cardNumber.value.length < 19) {
            cardNumber.style.borderColor = '#dc3545'; 
            
            errorBox.innerHTML = "Incomplete card number. Please enter all 16 digits.";
            errorBox.style.display = 'block';
        }
    });

    //card expiration date
    cardExpiry.addEventListener('input', function(e) {
        let value = e.target.value.replace(/\D/g, '');

        if (value.length >= 2) {
            let month = parseInt(value.substring(0, 2));
  
            if (month > 12) {
                value = '12' + value.substring(2);
            } 
            else if (month === 0) {
                value = '01' + value.substring(2);
            }
        }
        
        if (value.length > 2) {
            value = value.substring(0, 2) + '/' + value.substring(2, 4);
        }
        e.target.value = value;
    });

    //cvv only numbers
    cardCvv.addEventListener('input', function(e) {
        e.target.value = e.target.value.replace(/\D/g, '');
    });

    //errors
    paymentForm.addEventListener('submit', function(e) {
        errorBox.style.display = 'none';
        errorBox.innerText = '';
        let errors = [];

        if (cardNumber.value.length < 19) {
            errors.push("Please enter a valid 16-digit card number.");
        }

        if (errors.length > 0) {
            e.preventDefault(); 
            errorBox.innerHTML = errors.join('<br>');
            errorBox.style.display = 'block';
        }
    });

});