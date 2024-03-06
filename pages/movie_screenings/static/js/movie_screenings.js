function getQueryParams() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const params = {};
    for (const [key, value] of urlParams.entries()) {
        params[key] = value;
    }

    return params;
}

document.addEventListener("DOMContentLoaded", function () {

    const params = getQueryParams();

    if (params["movie"]) {
        const movieName = document.getElementById("movie-name");

        movieName.textContent = params["movie"];
    }
});
