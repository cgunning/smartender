function pour(drink) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      update(this.responseText)
    }
  };
  xhttp.open("POST", "/pour", true);
  xhttp.setRequestHeader("Content-Type", "application/json")
  xhttp.send(JSON.stringify({"drink": drink}));
}

function update(duration) { 
  var element = document.getElementById("myprogressBar");
  var menu = document.getElementById("scroll-container");
  menu.hidden = true;
  element.hidden = false;   
  var width = 1;
  var identity = setInterval(scene, 10); 
  function scene() { 
    width+=100/duration/100;  
    if (width >= 100) { 
      clearInterval(identity); 
      element.style.width = '100%'; 
      element.hidden = true;
      menu.hidden = false;
    } else { 
      element.style.width = width + '%';  
    } 
  } 
} 