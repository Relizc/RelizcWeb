
let c = document.getElementById("continue")
let g = document.getElementById("error")

function done(d) {
    console.log(d)
    c.innerHTML = "Continue"

    g.innerHTML = d.message
}

c.onclick = () => {
    g.innerHTML = ""
    c.innerHTML = `<i class="fa fa-circle-o-notch fa-spin"></i>`

    xml = new XMLHttpRequest();
    xml.open("GET", "/api/auth")
    xml.setRequestHeader("username", document.getElementById("username").value)
    xml.setRequestHeader("password", document.getElementById("password").value)
    xml.send()

    xml.onreadystatechange = () => {
        if (xml.readyState == 4) {
            done(JSON.parse(xml.responseText))
        }
    }
}