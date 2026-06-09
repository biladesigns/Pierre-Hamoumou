// Clé Web3Forms — obtenir gratuitement sur https://web3forms.com/ en entrant pierre.hamoumou.avocat@gmail.com
var WEB3FORMS_KEY = '675b06e3-b9bd-4b9f-9faf-1af062a00b39';

async function submitContactForm(e) {
    e.preventDefault();
    var form = e.target;
    var btn = form.querySelector('button[type="submit"]');
    var feedback = form.querySelector('.form-feedback');

    var originalText = btn.textContent.trim();
    btn.disabled = true;
    btn.textContent = 'Envoi en cours…';
    feedback.className = 'form-feedback hidden';
    feedback.textContent = '';

    // Injecter la clé dynamiquement
    var keyInput = form.querySelector('input[name="access_key"]');
    if (keyInput) keyInput.value = WEB3FORMS_KEY;

    var data = new FormData(form);

    try {
        var res = await fetch('https://api.web3forms.com/submit', {
            method: 'POST',
            headers: { 'Accept': 'application/json' },
            body: data
        });
        var text = await res.text();
        var json;
        try { json = JSON.parse(text); } catch(e) { json = { success: false, message: text }; }

        if (json.success) {
            feedback.className = 'form-feedback mt-4 p-4 rounded-sm text-sm text-center bg-[#AED18E]/20 text-[#2C6E68] border border-[#AED18E]';
            feedback.textContent = 'Message envoyé avec succès. Le cabinet vous répondra sous 48h ouvrées.';
            form.reset();
        } else {
            feedback.className = 'form-feedback mt-4 p-4 rounded-sm text-sm text-center bg-red-50 text-red-700 border border-red-200';
            feedback.textContent = json.message || 'Une erreur est survenue. Veuillez réessayer.';
        }
    } catch (err) {
        feedback.className = 'form-feedback mt-4 p-4 rounded-sm text-sm text-center bg-red-50 text-red-700 border border-red-200';
        feedback.textContent = 'Impossible de contacter le serveur. Vérifiez votre connexion ou contactez le cabinet au 07 70 28 25 46.';
    }

    btn.disabled = false;
    btn.textContent = originalText;
}
