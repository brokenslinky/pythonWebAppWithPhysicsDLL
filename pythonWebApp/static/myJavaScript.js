

var btn = document.getElementById("myButton");
var img = document.getElementById("myImage");
btn.innerHTML = "Click me";

btn.onclick = function () {
    var rate = document.getElementById("rate");
    var mass = document.getElementById("mass");
    var damp = document.getElementById("dampingRatio");
    //$.post("/dampingRatio", { ratio: damp.value }, function () {
    //});
    //$.post("/mass", { mass: mass.value }, function () {
    //});
    //$.post("/rate", { rate: rate.value }, function () {
    //});
    //event.preventDefault();
    img.src = "/plot.png?" + "mass=" + mass.value + "&rate=" + rate.value + "&ratio=" + damp.value;
    //img.contentWindow.location.reload(true);
};

//var t = document.getElementById("myVar");
//setInterval(function () {
//    t.innerHTML = (parseFloat(t.innerHTML) + 0.01).toString();
//    $.post("/dampingRatio", { ratio: t.innerHTML }, function () { });
//    img.src = "/static/plot.png";
//    img.contentWindow.location.reload(true)
//    return t.innerHTML;
//}, 5000);

function sleep(milliseconds) {
    var start = new Date().getTime();
    for (var i = 0; i < 1e7; i++) {
        if ((new Date().getTime() - start) > milliseconds) {
            break;
        }
    }
}