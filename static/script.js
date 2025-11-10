document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('passwordForm');
    const loadingSpinner = document.getElementById('loadingSpinner');
    const result = document.getElementById('result');
    const submitBtn = document.getElementById('submitBtn');
    const checkAgainBtn = document.getElementById('checkAgainBtn');
    const togglePasswordBtn = document.getElementById('togglePassword');
    const passwordInput = document.getElementById('password');
    
    // Toggle password visibility
    togglePasswordBtn.addEventListener('click', function() {
        const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordInput.setAttribute('type', type);
        togglePasswordBtn.classList.toggle('active');
    });
    
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const name = document.getElementById('name').value;
        const password = document.getElementById('password').value;
        
        // Hide form and result, show loading
        form.style.display = 'none';
        result.classList.add('hidden');
        loadingSpinner.classList.remove('hidden');
        submitBtn.disabled = true;
        
        try {
            const response = await fetch('/check', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    name: name,
                    password: password
                })
            });
            
            const data = await response.json();
            
            // Hide loading, show result
            loadingSpinner.classList.add('hidden');
            result.classList.remove('hidden');
            
            // Display results
            const strengthLabel = document.getElementById('strengthLabel');
            const feedbackText = document.getElementById('feedbackText');
            
            strengthLabel.textContent = `🔐 Password Strength: ${data.strength}`;
            strengthLabel.className = `strength-${data.strength.toLowerCase().replace(' ', '-')}`;
            feedbackText.textContent = `💬 ${data.feedback}`;
            
        } catch (error) {
            console.error('Error:', error);
            loadingSpinner.classList.add('hidden');
            result.classList.remove('hidden');
            document.getElementById('strengthLabel').textContent = '❌ Error';
            document.getElementById('feedbackText').textContent = 'Something went wrong. Please try again.';
        } finally {
            submitBtn.disabled = false;
        }
    });
    
    checkAgainBtn.addEventListener('click', function() {
        form.style.display = 'block';
        form.reset();
        result.classList.add('hidden');
        loadingSpinner.classList.add('hidden');
    });
});

