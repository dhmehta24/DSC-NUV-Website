window.onscroll = function() {shadow()}


var h = document.getElementById("myheader");

var shdw = h.offsetTop;


function shadow(){
    if(window.pageYOffset > shdw){
        h.classList.add("shadoweffect");
    }
    else{
        h.classList.remove("shadoweffect");
    }
}