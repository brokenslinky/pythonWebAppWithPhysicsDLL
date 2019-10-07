

var img = document.getElementById("myImage");

var t = document.getElementById("myVar");
setInterval(function () {
    t.innerHTML = (parseFloat(t.innerHTML) + 0.01).toFixed(2);
    img.src = "/plot.png?rate=49033&mass=272&ratio=" + t.innerHTML;
    return t.innerHTML;
}, 1000);
