let btn = document.querySelector('.application.second .btn.btn-secondary.btn-block'),
  text = document.querySelector('.application.second .result input'),
  input = document.querySelector('.application.second .start input'),
  currency = document.querySelectorAll('.application.second .start a'),
  currency2 = document.querySelectorAll('.application.second .result a'),
  start, result;

currency.forEach(function (element) {
  element.addEventListener('click', function () {
    start = element.textContent;
  });
});
currency2.forEach(function (element) {
  element.addEventListener('click', function () {
    result = element.textContent;
  });
});

btn.addEventListener('click', function () {
  $.get(
    'http://data.fixer.io/api/latest?access_key=afcc2a59554340029d77f0a6a690e74a&format=1',
    function (data) {
      let money, money_after_conversion, new_currency;
      money = input.value;
      if (start != 'EUR') {

        if (data['rates'][start] > 1) {
          new_currency = money / +data['rates'][start];
          money_after_conversion = new_currency * data['rates'][result];
          text.value = money_after_conversion.toFixed(1);
        } else {
          new_currency = money * +data['rates'][start];
          money_after_conversion = new_currency * data['rates'][result];
          text.value = money_after_conversion.toFixed(1);
        }
      } else {
        money_after_conversion = money * +data['rates'][result];
        text.value = money_after_conversion.toFixed(1);
      }
    }
  )
});