document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();
    const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

    if (name === '' || email === '' || message === '') {
        document.getElementById('errorMessage').style.display = 'block';
        document.getElementById('successMessage').style.display = 'none';
    } else if (!email.match(emailPattern)) {
        document.getElementById('errorMessage').innerText = 'Please enter a valid email address.';
        document.getElementById('errorMessage').style.display = 'block';
        document.getElementById('successMessage').style.display = 'none';
    } else {
        document.getElementById('errorMessage').style.display = 'none';
        document.getElementById('successMessage').style.display = 'block';

        console.log({
            name: name,
            email: email,
            message: message
        });
        document.getElementById('contactForm').reset();
    }
});
