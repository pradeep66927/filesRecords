var readlineSync = require('readline-sync');
var score = 0;


console.log("           WELCOME TO THE QUIZ ABOUT INDIA AND WORLD ")
console.log("")
console.log("")
var userName = readlineSync.question("what's your name ? :");
console.log("                          welcome "+ userName + " \n\nin this quiz you can judge yourself that you know somthing about india or world or not \n\nQuiz rule:-every correct answer will gift you 1 mark\n");
 

// play function

function play(question,answer) {
  var userAnswer = readlineSync.question(question);

  if (userAnswer === answer) {
    console.log("right");
    score = score + 1
  } else {
    console.log("wrong!");
  }

  console.log("current score : "+ score);
  console.log("---------------");
}

// array of objects
var questions = [{
  question:"Qn-1.how many country are there in the world approxmately?\nA.190  B.192  C.195  D.197 \n\nchoose your answer:",
  answer: "C"
},{
  question: "Qn-2.how many state and union terriotries currently in india?\nA.29 and 7  B.28 and 8  C.30 and 7  D.27 and 9 \n\nchoose your answer:",
  answer:"C"
},{
  question: "Qn-3.which is the longest river of  india?\nA.Brahmputra  B.Godawari  C.Mahanadi  D.Ganga \n\nchoose your answer:",
  answer:"D"
},{
  question: "Qn-4.what is the maximum height of statue in the world\nA.200 m  B.195 m  C.182 m  D.190 m \n\nchoose your answer:",
  answer:"C"
},{
  question: "Qn-5.the most happiest countory in the world\nA .U.S.A  B.britain  C.russia  D.finland \n\nchoose your answer:",
  answer:"D"
}];

//loop

for (var i=0; i<questions.length; i++) {
  var currentQuestion = questions[i];
  play(currentQuestion.question,currentQuestion.answer)
}

function showScores() {
  console.log("Hey! You SCORED: ", score);
}

showScores();

console.log("THANKS FOR PLAYING")