/* Toggle Style Switcher */ /* Toggle Style Switcher */ /* Toggle Style Switcher */
/* Toggle Style Switcher */ /* Toggle Style Switcher */ /* Toggle Style Switcher */
/* Toggle Style Switcher */ /* Toggle Style Switcher */ /* Toggle Style Switcher */

const styleSwitcherToggler = document.querySelector(".style-switcher-toggler");
styleSwitcherToggler.addEventListener("click",() =>
    {
        // console.log("Hi");
        document.querySelector(".style-switcher").classList.toggle("open");
    }
)

/* Hide Style Switcher On Scroll */
window.addEventListener("scroll",() =>
{
    // console.log("Hi");
    if (document.querySelector(".style-switcher").classList.contains("open"))
    {
        document.querySelector(".style-switcher").classList.remove("open");
    }
})



/* Theme Light and Dark Mode */ /* Theme Light and Dark Mode */  /* Theme Light and Dark Mode */ 
/* Theme Light and Dark Mode */ /* Theme Light and Dark Mode */  /* Theme Light and Dark Mode */ 
/* Theme Light and Dark Mode */ /* Theme Light and Dark Mode */  /* Theme Light and Dark Mode */ 
const dayNight = document.querySelector(".day-night");

dayNight.addEventListener("click", () =>
{
    // console.log("Hi");
    document.body.classList.toggle("dark");
    if (document.body.classList.contains("dark")) 
    {
        localStorage.setItem("theme", "dark");
    }
    else
    {
        localStorage.setItem("theme", "light");
    }
    updateIcon();
})

function themeMode()
{
    // Checking if Theme Key Exists
    if (localStorage.getItem("theme") !== null) 
    {
        // console.log("Exists");
        if (localStorage.getItem("theme") === "light")
        {
            document.body.classList.remove("dark");
        }
        else
        {
            document.body.classList.add("dark");
        }
    }
    else
    {
        // console.log("Not Exists");
    }
    // console.log("Hi");
    updateIcon();
}
themeMode();
function updateIcon()
{
    if (document.body.classList.contains("dark")) 
    {
        // console.log("True");
        dayNight.querySelector("i").classList.remove("fa-moon");
        dayNight.querySelector("i").classList.add("fa-sun");
    }
    else
    {
        // console.log("False");
        dayNight.querySelector("i").classList.remove("fa-sun");
        dayNight.querySelector("i").classList.add("fa-moon");
    }
}