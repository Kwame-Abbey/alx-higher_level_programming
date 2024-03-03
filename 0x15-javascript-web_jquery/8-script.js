const titles = [];
$.get(
  "https://swapi-api.alx-tools.com/api/films/?format=json",
  (data, status) => {
    if (status === "success") {
      const films = data.results;
      films.forEach((film) => {
        titles.push(film.title);
      });
      titles.forEach((title) => {
        $("UL#list_movies").append(`<li>${title}</li>`);
      });
    }
  }
);
