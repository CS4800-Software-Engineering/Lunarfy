// const countdown = 1
// let time = countdown * 60
// const countdown = document.getElementById("timer")
let points = 0
// var correct = true
const wordbank = ["take", "life", "back", "never","die", "away", "give", "time", "night", "day", "man", "woman", "dream", "world", "little","baby", "good", "again", "eyes", "mind", "heart", "world", "you", "breathe", "love", "fire", "dance", "moon", "sun", "star", "flower", "kiss", "lips", "sugar", "honey", "sweet", "girl", "boy", "everything", "lovely", "beautiful", "car", "music", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "december", "september", "august", "red", "blue", "yellow", "green", "orange", "purple", "black", "white", "sad", "happy", "mad", "slow", "fast", "talk", "call", "run", "sorry", "money", "myself", "young", "old", "school", "work"];
var word = ''
let time = 2 * 60;
var attemptArtist = false;
var songGuess = "song";
var artistGuess = "%20";

function updateTimer() {
    const minutes = Math.floor(time / 60); // rounds a number DOWN to the nearest integer
    let seconds = time % 60;

    seconds = seconds < 10 ? '0' + seconds : seconds;
    document.getElementById("timer").innerHTML = `${minutes}:${seconds}`;

    time--;

    if (time < 0) { //stop the setInterval whe time = 0 for avoid negative time
        clearInterval(refreshIntervalId);
        document.getElementById("finalLabel").style.display = "inline-block"
        document.getElementById("finalLabel").style.fontSize = "40pt";
        document.getElementById("highScore").style.display = "inline-block"
        document.getElementById("final1").style.display = "inline-block"
        document.getElementById("final2").style.display = "inline-block"

        document.getElementById("timer").style.display = "none";
        document.getElementById("prompt").style.display = "none";
        document.getElementById("field").style.display = "none";
        document.getElementById("artistField").style.display = "none";
        document.getElementById("artistOn").style.display = "none";
        document.getElementById("check").style.display = "none";
        document.getElementById("bf1").style.display = "none";
        document.getElementById("bf2").style.display = "none";
        document.getElementById("bf3").style.display = "none";
        document.getElementById("bf4").style.display = "none";


        // document.getElementById("timeup").style.display = "inline-block";
        // document.getElementById("songs").style.display = "inline-block";
        document.getElementById("space1").style.display = "inline-block";
        document.getElementById("space2").style.display = "none";
        document.getElementById("space3").style.display = "none";
        document.getElementById("space4").style.display = "none";
        document.getElementById("space5").style.display = "none";


        document.getElementById("keyword").style.display = "none";
        document.getElementById("again").style.display = "inline-block";
        document.getElementById("generate").style.display = "none";
        // document.getElementById("end").style.display = "inline-block";
        document.getElementById("b1").style.display = "inline-block";
        document.getElementById("b2").style.display = "inline-block";
        document.getElementById("b3").style.display = "inline-block";
        document.getElementById("b4").style.display = "inline-block";
        document.getElementById("b5").style.display = "inline-block";

    }
}



function startTime(){
  refreshIntervalId = setInterval(updateTimer, 1000);
  document.getElementById("begin").style.display = "none"
  generateWord()
}

function reload(){
  window.location.reload();
}

function generateWord(points=0){
  var pointStr = "Score: "+ points
  attemptArtist = false;


  document.getElementById("field").value = "";
  document.getElementById("generate").style.display = "inline-block"
  document.getElementById("timer").style.display = "inline-block"
  document.getElementById("prompt").style.display = "inline-block"
  document.getElementById("points").style.display = "inline-block"
  document.getElementById("finalLabel").style.display = "none"
  document.getElementById("highScore").style.display = "none"

  document.getElementById("field").style.display = "inline-block"
  document.getElementById("artistOn").style.display = "inline-block";
  document.getElementById("artistField").style.display = "none";

  document.getElementById("check").style.display = "inline-block"
  document.getElementById("bf1").style.display = "inline-block"
  document.getElementById("bf2").style.display = "inline-block"
  document.getElementById("bf3").style.display = "inline-block"
  document.getElementById("keyword").style.display = "inline-block"
  // document.getElementById("timeup").style.display = "none"
  // document.getElementById("songs").style.display = "none"
  document.getElementById("space1").style.display = "none"
  // document.getElementById("space2").style.display = "none"
  // document.getElementById("space3").style.display = "none"
  // document.getElementById("space4").style.display = "none"
  // document.getElementById("space5").style.display = "none"

  document.getElementById("again").style.display = "none"
  // document.getElementById("end").style.display = "inline-block"

  document.getElementById("intro").style.display = "none"
  document.getElementById("intro2").style.display = "none"

  document.getElementById("i1").style.display = "none"
  document.getElementById("i2").style.display = "none"
  document.getElementById("i3").style.display = "none"
  document.getElementById("i4").style.display = "none"
  document.getElementById("i5").style.display = "none"

  word = wordbank[Math.floor(Math.random() * wordbank.length)];
  // alert(text)
  document.getElementById("keyword").innerHTML = word
  document.getElementById("points").innerHTML = pointStr


}

function artist(){
  document.getElementById("artistField").style.display = "inline-block";
  document.getElementById("artistOn").style.display = "none";
  document.getElementById("bf2").style.display = "none";

  document.getElementById("bf3").style.display = "inline-block";
  document.getElementById("bf4").style.display = "inline-block";

  attemptArtist = true;

}


async function game3(){
  var correct = "True"
  var resultStr = "CORRECT";
  document.getElementById("artistOn").style.display = "none";

  songGuess = document.getElementById("field").value;
  if (attemptArtist){
    artistGuess = document.getElementById("artistField").value;
    points = points + 1;
  }

  if (songGuess == "pineapple" || songGuess == ""){
      correct = "False"
  }
  // alert(word)
  // alert(songGuess)
  // alert(artistGuess)


  // if (correct == "True"){
  //   points = points + 1;
  //   resultStr = "CORRECT";
  // }else{
  //   resultStr = "INCORRECT";
  // }
  let answer = await checkAnswer(songGuess, word, artistGuess, points)
  // if(answer == true){
  //   points = points + 1;
  //   resultStr = "CORRECT";
  // }else if(answer == false) {
  //   resultStr = "INCORRECT";
  // }else{
  //   resultStr = "UNKNOWN";
  // }

  // alert(resultStr);
  // generateWord(points);
}


// checkAnswer()

async function checkAnswer(song_title="love", term="love", artist_name="love", points) {

  myURL = `http://lunarverse.pythonanywhere.com/checkanswer/${song_title}/${term}/${artist_name}/`

  // alert(myURL)
  let url_response = await grabUrl(myURL, points)

  // alert(String(url_response))
  // alert("done")
  return url_response
}

async function grabUrl(myURL, points){
    const response = await fetch(myURL)
    const data = await response.text()
    // alert("here")
    if (data == "True"){
        alert("Correct")
        points = points + 1;
        generateWord(points);
        return True
    }else if(data == "False"){
        alert("Incorrect")
        // points = points + -1;
        generateWord(points);
        return False
    }else{
      // points = points + -10;
      generateWord(points);
      alert("no idea what this is")
    }
    return False
}

// function game2(){
//   clearInterval(refreshIntervalId);
//   // document.getElementById("continue").style.display = "inline-block";
//   // document.getElementById("check").style.display = "none";
//   // document.getElementById("field").style.display = "none";
//   // document.getElementById("prompt").style.display = "none"


//   // alert("Correct");
//   var correct = "True";

//   if (correct == "True"){
//     points = points + 1;

//     var pointStr = "Points: " + points;
//     var resultStr = "Correct";
//     document.getElementById("points").innerHTML = pointStr;
//     alert("result");
//     generateWord();

//   }else{
//     alert("Incorrect");
//     generateWord();
//   }
//   generateWord();
//   alert("generate");

// }



// function game(){
//   var correct = true
//   // document.getElementById("timer").style.display = "none"
//   // document.getElementById("prompt").style.display = "none"
//   // document.getElementById("field").style.display = "none"
//   document.getElementById("check").style.display = "none"
//   // document.getElementById("keyword").style.display = "none"
//   var resultStr = "Correct"
//   // document.getElementById("continue").style.display = "inline-block"
//   // document.getElementById("generate").style.display = "none"
//   // document.getElementById("end").style.display = "inline-block"

//   alert("HIIII")
//   // window.location.href = "https://pages.emilyrvillalba.repl.co/result.html";
//   if (correct){
//     points = points + 1;

//     pointStr = "Points: " + points
//     document.getElementById("points").innerHTML = pointStr
//     // document.getElementById("prompt").innerHTML = resultStr
//     alert("result")
//     // document.getElementById("correctOrNot").style.display = "inline-block"
//     document.getElementById("continue").style.display = "inline-block"
//     document.getElementById("end").style.display = "inline-block"

//   }else{
//     alert("Incorrect")
//     generateWord()
//   }
//   alert("GREAT JOB!!!!!")
// }

// function updateTimer() {
//   const minutes = Math.floor(time/60);
//   let seconds = time % 60;

//   seconds = seconds < 10 ? '0' + seconds:seconds;
//   document.getElementById("timer").innerHTML = `${minutes}: ${seconds}`;
//   time--;

//   // console.log(seconds)

//   if seconds == 10:
//     document.getElementById("timer").style.color = "red";

// }


// function generateWord(){
//   document.getElementById("timer").style.display = "inline-block"
//   document.getElementById("prompt").style.display = "inline-block"
//   document.getElementById("field").style.display = "inline-block"
//   document.getElementById("check").style.display = "inline-block"
//   document.getElementById("keyword").style.display = "inline-block"

//   word = wordbank[Math.floor(Math.random() * wordbank.length)];
//   // alert(word)
//   document.getElementById("keyword").innerHTML = word

// }
// function game(){
//   var correct = true
//   // document.getElementById("timer").style.display = "none"
//   // document.getElementById("field").style.display = "none"
//   // document.getElementById("check").style.display = "none"
//   // document.getElementById("keyword").style.display = "none"
//   // document.getElementById("prompt").innerHTML = "CONGRATS!!!!!!!!"
//   // alert("HIIII")
//   // window.location.href = "https://pages.emilyrvillalba.repl.co/result.html";
//   if (correct){
//     points = points + 1;
//     alert(points)
//     document.getElementById("point").innerHTML = points

//     alert("Correct")
//     generateWord()
//     // window.location.href = "https://pages.emilyrvillalba.repl.co/correct.html";
//   }else{
//     alert("Incorrect")
//     generateWord()
//   }
//   // alert("GREAT JOB!!!!!")
// }

function displayResult(){
  // var correct = true
  // if (correct = true){
  //   alert("yayyyyyy")
  //   document.getElementById("result").innerHTML = "Congrats!!!"
  // document.getElementById("result").style.display = "inline-block"
  // }else{
  //   document.getElementById("result").innerHTML ="Incorrect""
  // }
  // alert("DISplay result")
  // window.location.href = "https://pages.emilyrvillalba.repl.co/correct.html";

  // alert("DISplay result ???????")

}
// window.location.replace("http://www.w3schools.com");

// replace()
// const { spawn } = require('child_process')
// // const countdown = 1
// // let time = countdown * 60
// // const countdown = document.getElementById("timer")
// var points = 0
// // var correct = true
// const wordbank = ["take", "life", "back", "never","die", "away", "give", "time", "night", "day", "man", "woman", "dream", "world", "little","baby", "good", "again", "eyes", "mind", "heart", "world", "you", "breathe", "love", "fire", "dance", "moon", "sun", "star", "flower", "kiss", "lips", "sugar", "honey", "sweet", "girl", "boy", "everything", "lovely", "beautiful", "car", "music", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "december", "september", "august", "red", "blue", "yellow", "green", "orange", "purple", "black", "white", "sad", "happy", "mad", "slow", "fast", "talk", "call", "run", "sorry", "money", "myself", "young", "old", "school", "work"];
// var word = ''
// let time = 0.25 * 60;
// var attemptArtist = false;
// var songGuess = "";
// var artistGuess = "";

// function updateTimer() {
//     const minutes = Math.floor(time / 60); // rounds a number DOWN to the nearest integer
//     let seconds = time % 60;

//     seconds = seconds < 10 ? '0' + seconds : seconds;
//     document.getElementById("timer").innerHTML = `${minutes}:${seconds}`;

//     time--;

//     if (time < 0) { //stop the setInterval whe time = 0 for avoid negative time
//         clearInterval(refreshIntervalId);
//         document.getElementById("timer").style.display = "none";
//         document.getElementById("prompt").style.display = "none";
//         document.getElementById("field").style.display = "none";
//         document.getElementById("artistField").style.display = "none";
//         document.getElementById("artistOn").style.display = "none";
//         document.getElementById("check").style.display = "none";
//         document.getElementById("bf1").style.display = "none";
//         document.getElementById("bf2").style.display = "none";
//         document.getElementById("bf3").style.display = "none";
//         document.getElementById("bf4").style.display = "none";


//         // document.getElementById("timeup").style.display = "inline-block";
//         // document.getElementById("songs").style.display = "inline-block";
//         document.getElementById("space").style.display = "inline-block";

//         document.getElementById("keyword").style.display = "none";
//         document.getElementById("again").style.display = "inline-block";
//         document.getElementById("generate").style.display = "none";
//         // document.getElementById("end").style.display = "inline-block";
//         document.getElementById("b1").style.display = "inline-block";
//         document.getElementById("b2").style.display = "inline-block";
//         document.getElementById("b3").style.display = "inline-block";
//         document.getElementById("b4").style.display = "inline-block";
//         document.getElementById("b5").style.display = "inline-block";

//     }
// }



// function startTime(){
//   refreshIntervalId = setInterval(updateTimer, 1000);
//   document.getElementById("begin").style.display = "none"
//   generateWord()
// }

// function reload(){
//   window.location.reload();
// }

// function generateWord(points=0){
//   var pointStr = "Points: "+ points

//   document.getElementById("field").value = "";
//   document.getElementById("generate").style.display = "inline-block"
//   document.getElementById("timer").style.display = "inline-block"
//   document.getElementById("prompt").style.display = "inline-block"
//   document.getElementById("points").style.display = "inline-block"
//   document.getElementById("field").style.display = "inline-block"
//   document.getElementById("artistOn").style.display = "inline-block";
//   document.getElementById("artistField").style.display = "none";

//   document.getElementById("check").style.display = "inline-block"
//   document.getElementById("bf1").style.display = "inline-block"
//   document.getElementById("bf2").style.display = "inline-block"
//   document.getElementById("bf3").style.display = "inline-block"
//   document.getElementById("keyword").style.display = "inline-block"
//   // document.getElementById("timeup").style.display = "none"
//   // document.getElementById("songs").style.display = "none"
//   document.getElementById("space").style.display = "none"
//   document.getElementById("again").style.display = "none"
//   // document.getElementById("end").style.display = "inline-block"

//   document.getElementById("intro").style.display = "none"
//   document.getElementById("intro2").style.display = "none"

//   document.getElementById("i1").style.display = "none"
//   document.getElementById("i2").style.display = "none"
//   document.getElementById("i3").style.display = "none"
//   document.getElementById("i4").style.display = "none"

//   word = wordbank[Math.floor(Math.random() * wordbank.length)];
//   // alert(text)
//   document.getElementById("keyword").innerHTML = word
//   document.getElementById("points").innerHTML = pointStr


// }

// function artist(){
//   document.getElementById("artistField").style.display = "inline-block";
//   document.getElementById("artistOn").style.display = "none";
//   document.getElementById("bf2").style.display = "none";

//   document.getElementById("bf3").style.display = "inline-block";
//   document.getElementById("bf4").style.display = "inline-block";

//   attemptArtist = true;

// }

// function game3(){
//   var correct = "True"
//   var resultStr = "CORRECT";
//   document.getElementById("artistOn").style.display = "none";

//   songGuess = document.getElementById("field").value;
//   if (attemptArtist){
//     artistGuess = document.getElementById("artistField").value;
//   }

//   alert(songGuess)
//   alert(artistGuess)

//   if (correct == "True"){
//     points = points + 1;
//     resultStr = "CORRECT";
//   }else{
//     resultStr = "INCORRECT";
//   }

//   alert(resultStr);
//   generateWord(points);
// }



// // function game2(){
// //   clearInterval(refreshIntervalId);
// //   // document.getElementById("continue").style.display = "inline-block";
// //   // document.getElementById("check").style.display = "none";
// //   // document.getElementById("field").style.display = "none";
// //   // document.getElementById("prompt").style.display = "none"


// //   // alert("Correct");
// //   var correct = "True";

// //   if (correct == "True"){
// //     points = points + 1;

// //     var pointStr = "Points: " + points;
// //     var resultStr = "Correct";
// //     document.getElementById("points").innerHTML = pointStr;
// //     alert("result");
// //     generateWord();

// //   }else{
// //     alert("Incorrect");
// //     generateWord();
// //   }
// //   generateWord();
// //   alert("generate");

// // }



// // function game(){
// //   var correct = true
// //   // document.getElementById("timer").style.display = "none"
// //   // document.getElementById("prompt").style.display = "none"
// //   // document.getElementById("field").style.display = "none"
// //   document.getElementById("check").style.display = "none"
// //   // document.getElementById("keyword").style.display = "none"
// //   var resultStr = "Correct"
// //   // document.getElementById("continue").style.display = "inline-block"
// //   // document.getElementById("generate").style.display = "none"
// //   // document.getElementById("end").style.display = "inline-block"

// //   alert("HIIII")
// //   // window.location.href = "https://pages.emilyrvillalba.repl.co/result.html";
// //   if (correct){
// //     points = points + 1;

// //     pointStr = "Points: " + points
// //     document.getElementById("points").innerHTML = pointStr
// //     // document.getElementById("prompt").innerHTML = resultStr
// //     alert("result")
// //     // document.getElementById("correctOrNot").style.display = "inline-block"
// //     document.getElementById("continue").style.display = "inline-block"
// //     document.getElementById("end").style.display = "inline-block"

// //   }else{
// //     alert("Incorrect")
// //     generateWord()
// //   }
// //   alert("GREAT JOB!!!!!")
// // }

// // function updateTimer() {
// //   const minutes = Math.floor(time/60);
// //   let seconds = time % 60;

// //   seconds = seconds < 10 ? '0' + seconds:seconds;
// //   document.getElementById("timer").innerHTML = `${minutes}: ${seconds}`;
// //   time--;

// //   // console.log(seconds)

// //   if seconds == 10:
// //     document.getElementById("timer").style.color = "red";

// // }


// // function generateWord(){
// //   document.getElementById("timer").style.display = "inline-block"
// //   document.getElementById("prompt").style.display = "inline-block"
// //   document.getElementById("field").style.display = "inline-block"
// //   document.getElementById("check").style.display = "inline-block"
// //   document.getElementById("keyword").style.display = "inline-block"

// //   word = wordbank[Math.floor(Math.random() * wordbank.length)];
// //   // alert(word)
// //   document.getElementById("keyword").innerHTML = word

// // }
// // function game(){
// //   var correct = true
// //   // document.getElementById("timer").style.display = "none"
// //   // document.getElementById("field").style.display = "none"
// //   // document.getElementById("check").style.display = "none"
// //   // document.getElementById("keyword").style.display = "none"
// //   // document.getElementById("prompt").innerHTML = "CONGRATS!!!!!!!!"
// //   // alert("HIIII")
// //   // window.location.href = "https://pages.emilyrvillalba.repl.co/result.html";
// //   if (correct){
// //     points = points + 1;
// //     alert(points)
// //     document.getElementById("point").innerHTML = points

// //     alert("Correct")
// //     generateWord()
// //     // window.location.href = "https://pages.emilyrvillalba.repl.co/correct.html";
// //   }else{
// //     alert("Incorrect")
// //     generateWord()
// //   }
// //   // alert("GREAT JOB!!!!!")
// // }

// function displayResult(){
//   // var correct = true
//   // if (correct = true){
//   //   alert("yayyyyyy")
//   //   document.getElementById("result").innerHTML = "Congrats!!!"
//   // document.getElementById("result").style.display = "inline-block"
//   // }else{
//   //   document.getElementById("result").innerHTML ="Incorrect""
//   // }
//   // alert("DISplay result")
//   // window.location.href = "https://pages.emilyrvillalba.repl.co/correct.html";

//   // alert("DISplay result ???????")

// }
// // window.location.replace("http://www.w3schools.com");

// // replace()
// const wordbank = ["take", "life", "back", "never","die", "night", "day", "man", "woman", "dream", "world", "little","baby", "good", "again", "mind", "heart", "you", "breathe", "love", "fire", "dance", "moon", "sun", "star", "flower", "kiss", "lips", "sugar", "honey", "sweet", "girl", "boy", "everything", "lovely", "beautiful", "car", "music", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "december", "september", "august", "red", "blue", "yellow", "green", "orange", "purple", "black", "white", "mad", "slow", "talk", "run", "sour", "money", "teamwork", "young", "old", "school", "California", "fall", "winter", "autumn", "summer"];
