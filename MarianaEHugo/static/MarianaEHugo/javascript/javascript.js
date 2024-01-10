document.addEventListener("DOMContentLoaded", function () {
    // Dropdown functionality
    var dropdown = document.querySelector('.dropdown');
    if (dropdown) {
        dropdown.addEventListener('click', function(event) {
            event.stopPropagation();
            this.querySelector('.dropdown-content').classList.toggle('show');
        });
    }

    window.onclick = function(event) {
        if (!event.target.matches('.dropdown, .dropdown *')) {
            var dropdowns = document.getElementsByClassName("dropdown-content");
            for (var i = 0; i < dropdowns.length; i++) {
                if (dropdowns[i].classList.contains('show')) {
                    dropdowns[i].classList.remove('show');
                }
            }
        }
    };

    // Slideshow functionality
    var slides = document.getElementsByClassName("slide");
    var currentSlideIndex = 0;
    var interval;

    function showSlide(index) {
        var newTransformValue = "translateX(-" + index * 100 + "%)";
        document.getElementById("heroImage").style.transform = newTransformValue;
    }

    function nextSlide() {
        currentSlideIndex = (currentSlideIndex + 1) % slides.length;
        showSlide(currentSlideIndex);
    }

    function prevSlide() {
        currentSlideIndex = (currentSlideIndex - 1 + slides.length) % slides.length;
        showSlide(currentSlideIndex);
    }

    var nextBtn = document.getElementById("nextBtn");
    var prevBtn = document.getElementById("prevBtn");

    if (nextBtn) {
        nextBtn.addEventListener("click", function () {
            nextSlide();
            resetInterval();
        });
    }

    if (prevBtn) {
        prevBtn.addEventListener("click", function () {
            prevSlide();
            resetInterval();
        });
    }

    function startInterval() {
        interval = setInterval(nextSlide, 5000);
    }

    function resetInterval() {
        clearInterval(interval);
        startInterval();
    }

    startInterval();
});


function updateCountdown() {
    const targetDate = new Date('2024-07-13T00:00:00'); // Set your wedding date here
    const now = new Date();
    const difference = targetDate - now;

    if (difference <= 0) {
        // Handle the event that the countdown is over
        document.getElementById('countdown').innerHTML = "It's Wedding Time!";
        clearInterval(intervalId); // Stop the countdown
        return;
    }

    // Time calculations
    const months = Math.floor(difference / (1000 * 60 * 60 * 24 * 30));
    const days = Math.floor((difference % (1000 * 60 * 60 * 24 * 30)) / (1000 * 60 * 60 * 24));
    const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((difference % (1000 * 60)) / 1000);

    // Function to format the number with leading zero if necessary
    function formatNumber(number) {
        return number < 10 ? '0' + number : number;
    }

    // Display the result with leading zeros
    document.getElementById('months-number').innerText = formatNumber(months);
    document.getElementById('days-number').innerText = formatNumber(days);
    document.getElementById('hours-number').innerText = formatNumber(hours);
    document.getElementById('minutes-number').innerText = formatNumber(minutes);
    document.getElementById('seconds-number').innerText = formatNumber(seconds);
}
  
// Update the countdown every second
const intervalId = setInterval(updateCountdown, 1000);

