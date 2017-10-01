var animateText = document.getElementById("animated-text1");
var animateTexts = document.getElementById("animated-text2");
var textArray = animateText
    .innerText
    .split("");
var textArrays = animateTexts
    .innerText
    .split("");

animateText
    .firstChild
    .remove();
animateTexts
    .firstChild
    .remove();

//Probably a better way to do this.
var elArray = textArray.map((letter, index) => {
    if (letter == " ") 
        letter = '&nbsp;';
    var el = document.createElement("span");
    el.className = "letter";
    el.innerHTML = letter;
    el.style.animationDelay = index / (textArray.length) + "s";
    animateText.appendChild(el);
    return el;
});

var elArrays = textArrays.map((letter, index) => {
    if (letter == " ") 
        letter = '&nbsp;';
    var el = document.createElement("span");
    el.className = "letter2";
    el.innerHTML = letter;
    el.style.animationDelay = index / (textArrays.length) + "s";
    animateTexts.appendChild(el);
    return el;
});

animateText.innerHtml = elArray;
animateTexts.innerHtml = elArrays;