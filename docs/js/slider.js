// Range for Christianity count
var sliderChrstCount = document.getElementById("RangeChrstCount");
var outputChrstCount = document.getElementById("contentChrstCount");
var valChrstCount = document.getElementById("valChrstCount");
outputChrstCount.innerHTML = sliderChrstCount.value;
valChrstCount.innerHTML = sliderChrstCount.value;

sliderChrstCount.oninput = function() {
    valChrstCount.innerHTML = this.value;
    tablinks = document.getElementsByClassName("display");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    document.getElementById('"' + this.value + '"').style.display = "block";
    evt.currentTarget.className += " active";
}

// Range for Christianity percent
var sliderChrstPercent = document.getElementById("RangeChrstPercent");
var outputChrstPercent = document.getElementById("contentChrstPercent");
var valChrstPercent = document.getElementById("valChrstPercent");
outputChrstPercent.innerHTML = sliderChrstPercent.value;
valChrstPercent.innerHTML = sliderChrstPercent.value;

sliderChrstPercent.oninput = function() {
var container = outputChrstPercent;
valChrstPercent.innerHTML = this.value;
container.src = "graphics/christianity/percent/christianity_map_" + this.value + "_percent.html";
var content = container.innerHTML;
comtainer.innerHTML = content;
}