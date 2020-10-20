document.addEventListener("DOMContentLoaded", main);

function main() {
    document.querySelector("#todo")
        .addEventListener("mousedown", e => e.preventDefault());
}
