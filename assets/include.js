let d = document.getElementById("search")
let f = document.getElementById("query")

d.onmouseleave = () => {
    console.log()
    if (f.value.length != 0) {
        d.classList.remove("canclose")
    } else {
        d.classList.add("canclose")
        f.blur()
    }
}