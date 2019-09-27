$.get('https://swapi.co/api/films/?format=json', function (data) {
  $.each(data.results, function (index, movie) {
    $('ul#list_movies').append('<li>' + movie.title + '</li>');
  });
});
