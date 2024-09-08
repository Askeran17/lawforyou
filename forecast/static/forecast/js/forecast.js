/*jshint esversion: 6 */
/*jshint sub:true*/

// I set this option so JSHint doesn't raise unnecessary warnings.”

//questions count
let forecastquestionTotal = document.querySelector("#questions-total");

//start screen
let startPage = document.querySelector('#start-display');
let startButton = document.getElementById('start-button');
let forecastContainer = document.getElementById('forecast');

//when user click on start button
startButton.addEventListener('click', () => {
	startPage.classList.add('hide');
	forecastContainer.classList.remove('hide');
  });

  forecastContainer.classList.add('forecast');

  // Questions and Options array
const questions = [
	{
		question: "Did you send the documents electronically?",
		answers: ["Yes", "No"],
		correct: 1,
	},
	{
		question: "Have you been involved with the police in the last 18 months?",
		answers: [
			"Yes",
			"No"
		],
		correct: 2,
	},
	{
		question: "Do you have a permanent job?",
		answers: [
			"Yes",
			"No"
		],
		correct: 1,
	},
	{
		question: "Has your case been pending for more than 6 months?",
		answers: ["Yes", "No"],
		correct: 1,
	},

    {
		question: "Have you received any letters about your case?",
		answers: ["Yes", "No"],
		correct: 2,
	},

];

// search elements
const headerBlock = document.querySelector('#header');
const listBlock = document.querySelector('#list');
const submitButton = document.querySelector('#submit');


// scores variables
let goodAnswer = 0; // number of good answers
let badAnswer = 0; // number of bad answers
let score = 0; // games scores
let questionIndex = 0; // current question
let questionTotal = 1; // count question

// start commands
clearPage();
showQuestion();
submitButton.onclick = checkAnswer;

// clear page HTML
function clearPage() {
    headerBlock.innerHTML = '';
    listBlock.innerHTML = '';

}

// start current question
function showQuestion(){
console.log('showQuestion');

// question
const headerTemplate = `<h2 class="title">%title%</h2>`;
const title = headerTemplate.replace('%title%', questions[questionIndex]['question']);


headerBlock.innerHTML = title;

// answer options
let answerNumber = 1;
for (let answerText of questions[questionIndex]['answers']) {  
const questionTemplate = 
     `<li>
         <label>
    <input value="%number%" type="radio" class="answer" name="answer" />
    <span>%answer%</span>
</label>
</li>`;

const answerHTML = questionTemplate
.replace('%answer%', answerText)
.replace('%number%', answerNumber); 

listBlock.innerHTML += answerHTML;
answerNumber++;

}

}

// the function will be triggered when the button is pressed
function checkAnswer(){
    console.log('checkAnswer started!');
    
    // find the selected radio button
    const checkedRadio = listBlock.querySelector('input[type="radio"]:checked');
    
    // if the answer is not selected - do nothing, exit the function
    if (checkedRadio) {
        console.log('ok');
    } else {
        submitButton.blur();
        return;
    }
    
    // find out the user's answer number
    let userAnswer = parseInt(checkedRadio.value); 
    
    // if the answer is correct - increase the score. If not, continue count questions
    if (userAnswer === questions[questionIndex]['correct'] ) {
        goodAnswer++;
        document.innerHTML=+goodAnswer;
        document.innerHTML=+score;
    } else {
        badAnswer++;
        document.innerHTML=+badAnswer;
        
           
    }

    // question lenght
{ forecastquestionTotal.innerHTML = `<p>${questionTotal + 1} of ${questions.length} questions</p>`;
questionTotal++;
	}
    
    
    // checking questions
    if (questionIndex !== questions.length - 1){
        console.log('This is NOT last question');
        questionIndex++;
        clearPage();
        showQuestion();
        return;
    
    } else {
        console.log('This is last question');
        clearPage();
        showResult();
    }
    
    }

    // function for result
function showResult () {
    console.log(forecastquestionTotal);
    forecastquestionTotal.classList.add("questions-hidden");
    console.log('showResult started!');
    console.log(goodAnswer);

    const resultsTemplate = `
    <h2 class="title">%title%</h2>
    <h3 class="summary">%message%</h3>
    <p class="result">%result%</p>
    `;

    let title, message;

    // outcome options at the end of the forecast
    if (goodAnswer === questions.length) {
        title = 'Good work😀';
        message = 'The probability of a positive decision is high!';

    } else if ((goodAnswer * 100) / questions.length >= 50) {
        title = 'Not bad🤔';
        message = 'The probability of a positive decision is average';

    } else {
        title = 'Please complete your case😕';
        message = 'The probability of a positive decision is low';
    }

// result
let result = `${goodAnswer} of ${questions.length}`;

// final answer
const finalMessage = resultsTemplate
            .replace('%title%', title)
            .replace('%message%', message)
            .replace('%result%', result);

headerBlock.innerHTML = finalMessage;

// play again
submitButton.blur();
submitButton.innerText = 'Try again';
submitButton.onclick = function(){
    history.go();
	
};

}