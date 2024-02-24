document.addEventListener("DOMContentLoaded", function() {
    var scrollButton = document.getElementById('scroll');
    if (scrollButton){
        scrollButton.addEventListener('click', function() {
            var scrol = document.getElementById('form');
            if (scrol){
                scrol.scrollIntoView({ behavior: 'smooth' });
            }
        });
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