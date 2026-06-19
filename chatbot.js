function sendMessage(){

let input =
document.getElementById("message");

let message =
input.value.trim();

if(message===""){
return;
}

let chatBox =
document.getElementById("chat-box");

chatBox.innerHTML +=
`
<div class="user-message">
${message}
</div>
`;

fetch("/chat",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
message:message
})

})

.then(response=>response.json())

.then(data=>{

chatBox.innerHTML +=
`
<div class="bot-message">
${data.response}
</div>
`;

chatBox.scrollTop =
chatBox.scrollHeight;

});

input.value="";
}

/* Enter Key Support */

document.addEventListener(
"DOMContentLoaded",
function(){

let input =
document.getElementById("message");

if(input){

input.addEventListener(
"keypress",
function(e){

if(e.key==="Enter"){

e.preventDefault();

sendMessage();

}

});

}

});

/* Voice Recognition */

function startVoice(){

if(
'webkitSpeechRecognition'
in window
){

const recognition =
new webkitSpeechRecognition();

recognition.lang="en-US";

recognition.start();

recognition.onresult =
function(event){

document.getElementById(
"message"
).value =
event.results[0][0].transcript;

};

}
else{

alert(
"Voice recognition not supported in this browser."
);

}

}

/* Dark Mode */

function toggleTheme(){

document.body.classList.toggle(
"light"
);

}

/* Animated Counter */

function animateCounter(
id,
start,
end,
duration
){

let obj =
document.getElementById(id);

let current =
start;

let range =
end-start;

let increment =
range/(duration/20);

let timer =
setInterval(()=>{

current += increment;

obj.innerText =
Math.floor(current);

if(current>=end){

obj.innerText=end;

clearInterval(timer);

}

},20);

}

/* Run Counters */

window.onload=function(){

if(document.getElementById("patients")){

animateCounter(
"patients",
0,
10000,
2000
);

animateCounter(
"accuracy",
0,
95,
2000
);

animateCounter(
"doctors",
0,
250,
2000
);

}

};
