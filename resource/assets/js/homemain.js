const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');
const JoinBtn1 = document.getElementById('join-button1');
const JoinBtn2 = document.getElementById('join-button2');
const CloseBtn = document.getElementById('close-btn');

signUpButton.addEventListener('click', () => {
    container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
    container.classList.remove("right-panel-active");

});

JoinBtn1.addEventListener('click', () => {
    document.querySelector('.join-modal').style.display = 'flex';
});

JoinBtn2.addEventListener('click', () => {
    document.querySelector('.join-modal').style.display = 'flex';
});

CloseBtn.addEventListener('click', () => {
    document.querySelector('.join-modal').style.display = 'none';
});