document.addEventListener('DOMContentLoaded', function() {
    var header = document.querySelector('#header');
    if (header) {
        header.style.backgroundColor = '#ffcc00';  // Bright yellow background for testing
        header.style.color = '#000000';  // Black text color
        console.log('Admin inline test JS applied.');
    }
});
