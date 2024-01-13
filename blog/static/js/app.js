document.addEventListener("DOMContentLoaded", function () {
    let progressBar = document.querySelector(".js-progress-line");

    // Show the progress bar
    progressBar.style.display = "block";

    document.onscroll = function () {
        let progressLine = (window.scrollY / (document.body.clientHeight - window.innerHeight)) * 100;
        progressBar.style.width = progressLine + '%';
    };
});
