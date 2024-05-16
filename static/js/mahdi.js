document.addEventListener("DOMContentLoaded", function() {
    // Example JavaScript to toggle visibility
    document.getElementById("backgroundImage").classList.add("show-background-image");

    var scrollButton = document.getElementById('scroll');
    if (scrollButton){
        scrollButton.addEventListener('click', function() {
            var scrol = document.getElementById('form');
            if (scrol){
                scrol.scrollIntoView({ behavior: 'smooth' });
            }
        });
    }

    var typeselect = document.getElementById('qtype');
    if (typeselect){
        type();
        typeselect.addEventListener("change", type)
    }
        function type(){
            var selectedvalue = typeselect.value;
        var op1 = document.getElementById('quesoc');
        var op2 = document.getElementById('quesmc');
        var op3 = document.getElementById('questext');
        if (selectedvalue === "oc"){
            op1.style.display = "block";
            op2.style.display = "none";
            op3.style.display = "none";
        } else if (selectedvalue === "mc"){
            op1.style.display = "none";
            op2.style.display = "block";
            op3.style.display = "none";
        } else if (selectedvalue === "text"){
            op1.style.display = "none";
            op2.style.display = "none";
            op3.style.display = "block";
        }
    }

    var totalSeconds = 600;
    var timerElement = document.getElementById('timer');
    if (timerElement) {
        function updateTimer() {

            var minutes = Math.floor(totalSeconds / 60);
            var seconds = totalSeconds % 60;
    
            var displayMinutes = minutes < 10 ? '0' + minutes : minutes;
            var displaySeconds = seconds < 10 ? '0' + seconds : seconds;
    
            timerElement.textContent = displayMinutes + ':' + displaySeconds;
            if (totalSeconds === 0) {
                clearInterval(timerInterval);
                window.location.href = '/test'
            } else {
                totalSeconds--;
            }
        }
        var timerInterval = setInterval(updateTimer, 1000);
        updateTimer();
    }
});