// add an active class with different styling to the current page being selected 

let currentLocation = location.href;
const pages = document.querySelectorAll('#nav_bar_links a');
pages.forEach( (page) => {
    // console.log(currentPage.href)
    // page.classList.remove('active');
    if( page.href === currentLocation) {
        page.classList.add('active')
    }
})



// --------------------Help Page-----------------
// dropdown question
let faqs = document.querySelectorAll('.collapsible');
let answer = document.querySelector('.collapsible-ans');

faqs.forEach( (faq) =>{
    faq.addEventListener('click',function(){
        let arrowBtn = this.children[0].querySelector('button')
        let arrow = arrowBtn.getElementsByClassName('fas')
        
        // arrow[0].classList.replace("fa-chevron-down", "fa-chevron-up")
        arrow[0].classList.toggle("fa-chevron-up")
        if(arrow[0].classList.contains("fa-chevron-up")){
            this.children[1].style.display = 'block';
            // this.chidren[0].firstElementChild.background = `linear-gradient(to right, #e84460, #2d2c4a)`;
            // console.dir(this.querySelector('h5 button'))
        } else {
            this.children[1].style.display = 'none';
        }
    })
})

// ------------------------Leagues Page-------------------------
let currentManagerTeam = document.querySelector('.my-team-row');
// console.log(currentManagerTeam)

let allTeams = document.querySelectorAll('.my-team');
allTeams.forEach(team =>{
    // console.log(team.textContent)
    if(team.textContent == currentManagerTeam.textContent){
        team.parentElement.style.backgroundColor = `var(--light)`;
        // team.textContent += ' *';
    }
})



// ------------Fixtures Page-------------
let currentScrollPosition = 0;
let scrollAmount = 650;

const sCont = document.querySelector('.gameweeks');
const hScroll =  document.querySelector('.match-week-scroller');
const btnScrollLeft = document.querySelector('#btn-scroll-left');
const btnScrollRight = document.querySelector('#btn-scroll-right');

btnScrollLeft.style.opacity = '0';

let maxScroll = -sCont.offsetWidth + hScroll.offsetWidth;

function scrollHorizontally(val) {
    currentScrollPosition += (val * scrollAmount);

    if(currentScrollPosition >= 0){
        currentScrollPosition = 0
        btnScrollLeft.style.opacity = '0';
    }else{
        btnScrollLeft.style.opacity = '1';
    }

    if(currentScrollPosition <= maxScroll){
        currentScrollPosition = maxScroll;
        btnScrollRight.style.opacity = '0';
    }else{
        btnScrollRight.style.opacity = '1';
    }

    sCont.style.left = currentScrollPosition + 'px';
}


// ----------show-hide-fixtures--------------
let currentGameweek = 34;
let currentGameweekBtn = document.querySelector(`#gw-${currentGameweek}`)
let gameweekScrollBtns = document.querySelectorAll('.gw-num');
let gameweekFixturesInfo = document.querySelectorAll('.gw');
let clickedWeek;
// console.log(gameweekFixturesInfo);

// add a unique border to current gamewek scroll btn 
currentGameweekBtn.style.border = `1px solid var(--bg-accent)`;
currentGameweekBtn.style.color = 'var(--bg-accent)';
// and show the current btn near to center
if(currentGameweek >= 7){
    sCont.style.left = -currentGameweekBtn.offsetLeft/1.15 + 'px';
    btnScrollLeft.style.opacity = '1';
    btnScrollRight.style.opacity = '1';
}
if(currentGameweek == 38){
    sCont.style.left = -currentGameweekBtn.offsetLeft/1.2 + 'px';
    btnScrollRight.style.opacity = '0';
}



// show current week fixtures at beginning
// document.querySelectorAll(`.gw-${currentGameweek}`).classList.add('gw-show');
document.querySelectorAll(`.gw-${currentGameweek}`).forEach((match)=>{
    match.classList.add('gw-show');
})
document.getElementById('show-gw-no').textContent = currentGameweek;


// show clicked week fixture and hide all others
gameweekScrollBtns.forEach( (weekBtn) =>{
    weekBtn.addEventListener('click',function(){

        clickedWeek = this.id;
        
        gameweekFixturesInfo.forEach( (gw) =>{
            gw.classList.remove('gw-show')
            if(clickedWeek == gw.classList[1]){
                gw.classList.add('gw-show')
            }
        })

        
        gameweekScrollBtns.forEach( (gwBtn) => {
            gwBtn.style.border = 'none';
            gwBtn.style.color = 'initial';

            if(clickedWeek == gwBtn.id){
                gwBtn.style.border = '1px solid var(--bg-accent)'
                gwBtn.style.color = 'var(--bg-accent)';
            }
        })

        // change week no shown accordingly
        document.getElementById('show-gw-no').textContent = clickedWeek.split('-')[1];
        
    })
    
})












