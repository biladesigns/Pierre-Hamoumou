// Clé Web3Forms — obtenir gratuitement sur https://web3forms.com/ en entrant pierre.hamoumou.avocat@gmail.com
var WEB3FORMS_KEY = 'VOTRE_CLE_WEB3FORMS';

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
            body: data
        });
        var json = await res.json();

        if (json.success) {
            feedback.className = 'form-feedback mt-4 p-4 rounded-sm text-sm text-center bg-[#AED18E]/20 text-[#2C6E68] border border-[#AED18E]';
            feedback.textContent = 'Message envoyé avec succès. Le cabinet vous répondra sous 48h ouvrées.';
            form.reset();
        } else {
            throw new Error(json.message || 'Erreur serveur');
        }
    } catch (err) {
        feedback.className = 'form-feedback mt-4 p-4 rounded-sm text-sm text-center bg-red-50 text-red-700 border border-red-200';
        feedback.textContent = 'Une erreur est survenue. Veuillez réessayer ou contacter le cabinet directement au 07 70 28 25 46.';
    }

    btn.disabled = false;
    btn.textContent = originalText;
}
