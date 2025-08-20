function blink()
{
    let alr = document.querySelector('.alert')
    if (alr.style.visibility === "hidden")
    {
        alr.style.visibility = "visible";
    }
    else
    {
        alr.style.visibility = "hidden";
    }
}

window.setInterval(blink, 5000);