$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const url = 'https://www.fourtonfish.com/hellosalut/hello/';
    const language = $('INPUT#language_code').val();
    $.get(url + $.param({ lang: language }),
      function (data) {
        $('DIV#hello').text(data.hello);
      });
  });
});
