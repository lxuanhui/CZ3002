var prevButton = 0; //The button that was clicked before: 0 if no button has been clicked yet
var alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"];
var timer = 0;
var contentList = [];
var timeArray = [];
var timeResults = [];
var prevButton = 0;
var halfcount = 0;
var errors = 0;

// Get the modal
var dialog = document.getElementById("dialog");
// Get the <span> element that closes the modal
var proceed = document.getElementById("proceed");
var finishbox = document.getElementById("finish");
var lastBtn;

function contentListGen() {
    for (var i = 0; i < alpha.length; i++) {
        contentList.push(i + 1);
        contentList.push(alpha[i]);
    }
}
// A function that is called when a button is clicked with a (this) sent to it
// you can read more about (this) on internet

function checkButtonB(clickedButton) {
    // check if id of current button is equal to corresponding in contentList
    if (clickedButton.id == contentList[prevButton]) {
        // If it is then change the background color of it
        clickedButton.style.background = "#0FFF50";
        clickedButton.style.color = "black"


        document.getElementById(clickedButton.id).style.opacity = "0";
        timer = (new Date()).getTime();
        timeArray.push(timer);

        if (prevButton + halfcount < contentList.length) {
            document.getElementById(contentList[prevButton + halfcount]).style.visibility = "visible";
        }
        prevButton++;
    }
    else {
        clickedButton.style.animation = "incorrect 1s";
        errors++;
    }
    if (clickedButton.id === contentList[contentList.length - 1]) {
        for (var i = 0; i < timeArray.length; i++) {
            timeResults.push(timeArray[i + 1] - timeArray[i]);
        }
    }
}

// function to generate buttons
function createButtons() {
    // Write a div tag to document with class name (game)
    document.write("<div class='buttongridB'>");
    // Loop to generate buttons
    for (var i = 0; i < contentList.length; i++) {
        // write button tags to document with id=i when i = 1, 2, 3, 4, .. and call checkButtonB function when clicked and pass (this) to it
        document.write("<button class='tmtbutton' id=" + contentList[i] + " onclick='checkButtonB(this)'>" + contentList[i] + "</button>");
    }
    lastBtn = document.getElementById(contentList[contentList.length - 1]);
    halfcount = Math.floor(contentList.length / 2);

    for (var i = Math.floor(contentList.length / 2); i < contentList.length; i++) {
        document.getElementById(contentList[i]).style.visibility = "hidden";
    }
    // write closed div tag
    document.write("</div>");

}

// function that shuffles the buttons to a random position
function shuffleButtons() {
    // get the div that buttons are in it
    var div = document.querySelector('.buttongridB');
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
    if (Number(timeTotal) > 40000){
        document.getElementById('dialogtext').textContent = "You completed TMT-B! Your completion time is higher than average.Consider going for a medical check up!"
    }
}

function completion() {
    lastBtn.onclick = function () {
        checkButtonB(this);
        document.querySelector('.buttongridB').style.display = 'none';
        timeCheck()
        finishbox.style.visibility = "visible";
        dialog.style.visibility = "visible";

        localStorage.setItem("timeArray", JSON.stringify(timeArray));
        localStorage.setItem("timeResults", JSON.stringify(timeResults));
        localStorage.setItem("errors", JSON.stringify(errors));

    }
    proceed.onclick = function () {
        finishbox.style.display = "none";
        dialog.style.display = "none";
        location.href = "/results";
    }
}