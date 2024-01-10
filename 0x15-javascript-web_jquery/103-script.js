$('document').ready(function () {
  function fetchAndDisplay () {
    const url = 'https://www.fourtonfish.com/hellosalut/hello/';
    const language = $('INPUT#language_code').val();
    $.get(url + $.param({ lang: language }), function (data) {
      $('DIV#hello').text(data.hello);
    });
  }
  $('INPUT#btn_translate').click(fetchAndDisplay);
  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchAndDisplay();
    }
  });
});
