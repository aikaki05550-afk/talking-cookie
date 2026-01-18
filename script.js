const speech = document.getElementById("speech");
const buttons = document.getElementById("buttons");
const cookieImg = document.querySelector(".cookie img");

let step = 0;
let canClickCookie = false;

function setDialogue(text, options) {
  speech.style.opacity = "0";
  
  setTimeout(() => {
    speech.textContent = text;
    buttons.innerHTML = "";
    speech.style.opacity = "1";

    options.forEach((option, index) => {
      const btn = document.createElement("button");
      btn.textContent = option.text;
      btn.onclick = option.action;
      btn.style.animationDelay = `${index * 0.1}s`;
      btn.className = "btn-fade";
      buttons.appendChild(btn);
    });
  }, 200);
}

// Cookie click interaction
if (cookieImg) {
  cookieImg.addEventListener("click", () => {
    if (canClickCookie) {
      cookieClicked();
    }
  });
}

/* --- ШАГ 1 --- */
function start() {
  canClickCookie = false;
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

function cookieClicked() {
  setDialogue(
    "Nom nom! 😋 That tickles!",
    [{ text: "Continue", action: askHow }]
  );
}

/* --- СТАРТ --- */
start();
