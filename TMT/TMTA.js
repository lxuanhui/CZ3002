var prevButton = 0; //The button that was cilcked before: 0 if no button has been clicked yet
var buttonCount = 15; // How many buttons do you want
var contentList = [];
var timeArray = [];
var timeResults = [];
var halfcount = 0;

// Get the modal
var dialog = document.getElementById("dialog");
// Get the <span> element that closes the modal
var proceed = document.getElementsByClassName("proceed");
var finishbox = document.getElementById("finish");
var lastBtn;

// A function that is called when a button is clicked with a (this) sent to it
// you can read more about (this) on internet
function checkButtonA(clickedButton) {
    console.log(clickedButton.id)
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
    }
    if (Number(clickedButton.id) === buttonCount) {
        for (var i = 0; i < timeArray.length; i++) {
            timeResults.push(timeArray[i + 1] - timeArray[i]);
        }
        console.log(timeResults);
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

// Dialog menu below
function completion(){
    lastBtn.onclick = function(){
        checkButtonA(this);
        finishbox.style.visibility = "visible";
        dialog.style.visibility = "visible";
    }
    proceed.onclick = function() {
        dialog.style.display = "none";
        console.log("Proceeding")
    }
}


// When the user clicks on <span> (x), close the modal

