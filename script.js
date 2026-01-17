const speech = document.getElementById("speech");
const buttons = document.getElementById("buttons");

let step = 0;

function setDialogue(text, options) {
  speech.textContent = text;
  buttons.innerHTML = "";

  options.forEach(option => {
    const btn = document.createElement("button");
    btn.textContent = option.text;
    btn.onclick = option.action;
    buttons.appendChild(btn);
  });
}

/* --- ШАГ 1 --- */
function start() {
  setDialogue(
    "Hi! I'm a cookie 🍪",
    [
      { text: "Continue", action: askHow },
      { text: "Who are you?", action: askWho },
      { text: "Hello!", action: sayHello },
      { text: "Bye", action: sayBye }
    ]
  );
}

/* --- ВАРИАНТЫ --- */
function askWho() {
  setDialogue(
    "I'm a talking cookie 😄",
    [{ text: "Continue", action: askHow }]
  );
}

function sayHello() {
  setDialogue(
    "Hello! Nice to see you!",
    [{ text: "Continue", action: askHow }]
  );
}

function sayBye() {
  setDialogue(
    "Hey! Don't leave yet 😢",
    [{ text: "Continue", action: askHow }]
  );
}

/* --- ШАГ 2 --- */
function askHow() {
  setDialogue(
    "How are you today?",
    [
      { text: "Good 😊", action: good },
      { text: "Normal 😐", action: normal },
      { text: "Bad 😢", action: bad },
      { text: "Very bad 😞", action: veryBad }
    ]
  );
}

/* --- ОТВЕТЫ --- */
function good() {
  setDialogue(
    "Yay! I'm happy for you! 🍪✨",
    [{ text: "Start again", action: start }]
  );
}

function normal() {
  setDialogue(
    "That's okay. Some days are like that 🙂",
    [{ text: "Start again", action: start }]
  );
}

function bad() {
  setDialogue(
    "Oh no… I hope things get better 💛",
    [{ text: "Start again", action: start }]
  );
}

function veryBad() {
  setDialogue(
    "I'm sorry 😞 Take a virtual cookie 🍪",
    [{ text: "Start again", action: start }]
  );
}

/* --- СТАРТ --- */
start();
