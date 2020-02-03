function myFunction() {
    var x = document.getElementById("navbar");
    if (x.className === "menubar") {
      x.className += " responsive";
    } else {
      x.className = "menubar";
    }
  }