document.addEventListener('DOMContentLoaded',  () => {

    const hamburger = document.querySelector(".hamburger");
    const navLinks = document.querySelector(".header-nav-items");

    hamburger.addEventListener("click", () => {
        navLinks.classList.toggle("active");
    });

    //footer

    let year = new Date().getFullYear();
    document.getElementById('year').innerText = year;

    //profile search page 

    const searchInput = document.getElementById("username-search");
    const suggestionsBox = document.getElementById("username-suggestions");
    if(searchInput) {
        searchInput.addEventListener("input", function () {

            const query = this.value.trim();
            console.log(query);

            if (query.length === 0) {
                suggestionsBox.innerHTML = "";
                return;
            }

            fetch(`/profile/suggestions/?q=${encodeURIComponent(query)}`)
                .then(response => response.json())
                .then(users => {

                    suggestionsBox.innerHTML = "";
                    console.log("js working");

                    users.forEach(user => {

                        const suggestion = document.createElement("a");

                        suggestion.textContent = user.username;

                        suggestion.href = `/profile/${user.username}`;

                        suggestionsBox.appendChild(suggestion);
                    });

                });
        });
    }

});


