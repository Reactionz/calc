
/* 

How to Write A Calculator in Javascript

Step 1: Obtain value when a button is pressed and display a number on the screen based on what you typed in.
Step 2: If you press one of the math symbol buttons, it is going to have sort of a darker frame over it to know that
you have pressed the button and you are going to do a math equation. This is going to be done in only integers as working with 
floating points would be a pain in the ass so I don't want to go down that road.

Another thing to know is that when you put a number and press one of the math symbol buttons, it is going to change back to zero
but store that value to add with the other number that is about to be used.
*/
let runningTotal = 0;
let buffer = "0";
let previousOperator = null;
const screen = document.querySelector('.screen');

function init() {
    document.querySelector(".calc-keypad").addEventListener("click", function (event) {
        buttonClick(event.target.innerText);
        // console.log('hi');
    });
}

function buttonClick(value) {
    if (isNaN(parseFloat(value))) {
        console.log(value);
        handleSymbol(value);
    } else {
        console.log(value);
        handleNumber(value);
    }
    rerender();
}

function handleNumber(value) {
    if (buffer === "0") {
        buffer = value;
    } else {
        buffer += value;
    }

}

function handleSymbol(value) {
    switch (value) {
        case 'C':
            buffer = '0';
            runningTotal = 0;
            previousOperator = null;
            break;
        case 'CE':
            buffer = '0';
            break;
        case '=':
            if (previousOperator === null) {
                return;
            }
            flushOperation(parseFloat(buffer));
            previousOperator = null;
            buffer = "" + runningTotal;
            runningTotal = 0;
            break;
        case '←':
            if (buffer.length === 1) {
                buffer = "0";
            } 
            else if(buffer[0] == '-') {
                if (buffer.length == 2) {
                    buffer = "0";
                } else {
                    buffer = buffer.substring(0, buffer.length - 1);
                }
            }
            //TODO: Make it possible to back out characters when more than one value with negatives
            // else if (buffer.includes('-')) {
            //     if (buffer.length <= 2) {
            //         buffer = "0";
            //     }
            //} 
            else {
                buffer = buffer.substring(0, buffer.length - 1);
            }
            break;
        case '.':
            if (buffer.includes('.')) {
                break;
            } else {
                buffer += ".";
            }
            break;
        case '+/-':
            if (buffer[0]== '-') {
                console.log('starts with');
                buffer = buffer.substr(1);
            }
            else if (buffer == 0) {
                    break;
            }
            // else if (buffer.includes('-')) {
            //     break;
            // }
              else {
                buffer = '-' + buffer;
            }
            break;
        case 'sin':
            // console.log(buffer)
            buffer = Math.sin(buffer * Math.PI / 180);
            break;
        case 'cos':
            buffer = Math.cos(buffer * Math.PI / 180);
            break;
        case 'tan':
            buffer = Math.tan(buffer * Math.PI / 180);
            break;
        case 'sq':
            buffer = Math.pow(buffer, 2);
            break;
        case 'sqrt':
            buffer = Math.sqrt(buffer);
            break;
        case 'log':
            if (buffer == '-Infinity') {
                buffer = '0';
            }
            buffer = Math.log10(buffer);
            break;
        case 'ln':
            if (buffer == '-Infinity') {
                buffer = '0';
                break;
            }
            buffer = Math.log(buffer);
            break;
        default:
            handleMath(value);
            break;
    }
}

function handleMath(value) {
    const intBuffer = parseFloat(buffer);

    if (runningTotal === 0) {
        runningTotal = intBuffer;
    } else {
        flushOperation(intBuffer);
    }

    previousOperator = value;
    //ready for the next number to come in
    buffer = '0';
}

/*Addition, Subtraction, Multiplication, Divisiion
Sine (degrees), Cosine, Tangent
Exponential, Natural Logarithm, Square Root (sqrt)
Power of 2 (sq), Decimal Point, Positive To Negative Change (+/-)
Clear current input (clear), cancel or reset the calculator option */
function flushOperation(intBuffer) {
    if (previousOperator === "+") {
        runningTotal += intBuffer;
    } else if (previousOperator === "-") {
        runningTotal -= intBuffer;
    } else if (previousOperator === "x") {
        runningTotal *= intBuffer;
    } else if (previousOperator === "÷") {
        runningTotal /= intBuffer;
    } else if (previousOperator === "exp") {
        runningTotal = runningTotal ** intBuffer;
    }
}

function rerender(value) {
    screen.innerText = buffer;
}

init();