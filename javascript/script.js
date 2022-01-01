let navLink = document.getElementById("nav_bar_links")
console.log(navLink)

let navLinks = document.getElementById("nav_bar_links").getElementsByTagName('li')
console.log(navLinks)


for(let i=0; i<navLinks.length; i++) {
    navLinks[i].addEventListener("click", function(){

        document.getElementsByClassName("active")[0].classList.remove('active');

        navLinks[i].getElementsByTagName('a')[0].classList.add('active');

        // doesnt work 
        // works fine in mouseover instead of click 
    })
}
