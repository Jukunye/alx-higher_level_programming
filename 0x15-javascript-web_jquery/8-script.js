$.get('https://swapi-api.alx-tools.com/api/films/?format=json',
  function (data) {
    $.each(data.results, function (index, movie) {
      $('UL#list_movies').append('<LI>' + movie.title + '</LI>');
    });
  }
);
