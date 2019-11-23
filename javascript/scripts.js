const questions = [
    //javascript object
    {
        question: "What is 10 + 10?",
        options: ["10", "20", "30"],
        answer: "20"
    },
    {
        question: "What is Athena's favorite animal?",
        options: ["jellyfish", "penguins", "otters"],
        answer: "otters"
    }
];

let question_number = 0;
let correct = 0;

document.addEventListener("DOMContentLoaded", () => {
    load_question();
    document.querySelectorAll('.option').forEach(function(button) {
        button.onclick = function() {
            console.log(button.textContent, button.innerHTML)
            if (questions[question_number].answer == button.textContent) {
                correct++;
            }
            question_number ++;
        }
    })
});

function load_question() {
    document.querySelector('#question').innerHTML = questions[question_number].question;
    const options = document.querySelector('#options');
    for (const option of questions[question_number].options) {

        // my solution
        // const button = document.createElement('button');
        // button.innerHTML = option;
        // document.querySelector('#options').append(button);

        options.innerHTML += `<button class="option">${option}</button>`
    }
}
