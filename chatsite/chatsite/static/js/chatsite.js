//Remove the enter functionality if the textbox is null
const userMessageInput = document.getElementById('user-message');
userMessageInput.addEventListener('keydown', function(e) {
    if (e.key === 'Enter' && userMessageInput.value.trim() === '') {
        e.preventDefault();
    }
});

//Shift + Enter it will do new line
const userMessageInputNewLine = document.getElementById('user-message');
userMessageInputNewLine.addEventListener('keydown', function(e) {
    if (e.key === 'Enter' && e.shiftKey) {
        const currentValue = userMessageInputNewLine.value;
        userMessageInputNewLine.value = currentValue + '\n';
        e.preventDefault();
    }
});
