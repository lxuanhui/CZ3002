var prevButton = 0; //The button that was clicked before: 0 if no button has been clicked yet
var buttonCount = 15; // How many buttons do you want
var contentList = [];
var timeArray = [];
var timeResults = [];
var timeTotal = 0;
var halfcount = 0;
var errors = 0;

// Get the modal
var dialog = document.getElementById("dialog");
// Get the <span> element that closes the modal
var finishbox = document.getElementById("finish");
var proceed = document.getElementById("proceed");
var lastBtn;

// A function that is called when a button is clicked with a (this) sent to it
function checkButtonA(clickedButton) {
    // check if id of current button is one ahead of the prevButton such as 3 - 1 == 2
    if (Number(clickedButton.id) - 1 == prevButton) {
        // If it is then change the background color of it to red
        clickedButton.style.background = "#0FFF50";
        clickedButton.style.color = "black"

        document.getElementById(clickedButton.id).style.opacity = "0";
        timer = (new Date()).getTime();
        timeArray.push(timer);

        if (prevButton + halfcount < buttonCount) {
            document.getElementById(contentList[prevButton + halfcount]).style.visibility = "visible";
        }
        prevButton++;
    }
    else {
        clickedButton.style.animation = "incorrect 1s";
        errors++;
    }
    if (Number(clickedButton.id) === buttonCount) {
        for (var i = 0; i < timeArray.length; i++) {
            timeResults.push(timeArray[i + 1] - timeArray[i]);
        }
    }
}

// function to generate buttons
function createButtons() {
    // Write a div tag to document with class name (game)
    document.write("<div class='buttongridA'>");
    // Loop to generate buttons
    for (var i = 1; i <= buttonCount; i++) {
        // write button tags to document with id=i when i = 1, 2, 3, 4, .. and call checkButtonA function when clicked and pass (this) to it
        document.write("<button class='tmtbutton' id=" + i + " onclick='checkButtonA(this)'>" + i + "</button>");
        contentList.push(i);
    }
    lastBtn = document.getElementById(contentList[contentList.length-1]);
    halfcount = Math.floor(contentList.length/2);

    for (var i = halfcount; i < contentList.length; i++) {
        document.getElementById(contentList[i]).style.visibility = "hidden";
    }
    // write closed div tag
    document.write("</div>");
}

// function that shuffles the buttons to a random position
function shuffleButtons() {
    // get the div that buttons are in it
    var div = document.querySelector('.buttongridA');
    // Loop that start from our number of buttons 20 and goes to 0
    for (var i = contentList.length; i >= 0; i--) {
        // append a button to the new random position 
        div.appendChild(div.children[Math.random() * i | 0]);
    }
}

function timeCheck() {
    for (var i=0; i<timeArray.length; i++) {
        if(Number(i)!=null){
            timeTotal += Number(timeArray[i]);
        }
    }
    console.log(timeTotal)
    if (Number(timeTotal) > 20000){
        document.getElementById('dialogtext').textContent = "You completed TMT-A! Your completion time is higher than average.Consider going for a medical check up!"
    }
}


// Dialog menu below
function completion(){
    lastBtn.onclick = function(){
        checkButtonA(this);
        document.querySelector('.buttongridA').style.display='none';
        timeCheck()
        finishbox.style.visibility = "visible";
        dialog.style.visibility = "visible";

        
        localStorage.setItem("timeArray", JSON.stringify(timeArray));
        localStorage.setItem("timeResults", JSON.stringify(timeResults));
        localStorage.setItem("errors", JSON.stringify(errors));
    }
    proceed.onclick = function() {
        finishbox.style.display = "none";
        dialog.style.display = "none";
        location.href="/results";
    }
}


