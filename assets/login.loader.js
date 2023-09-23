
let c = document.getElementById("continue")

c.onclick = () => {
    c.innerHTML = `<i class="fa fa-circle-o-notch fa-spin"></i>`

    fetch("/api/")
}