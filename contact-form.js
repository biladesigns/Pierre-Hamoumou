var FORMSPREE_ENDPOINT = 'https://formspree.io/f/mwvjbgep';

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

    var data = new FormData(form);

    try {
        var res = await fetch(FORMSPREE_ENDPOINT, {
            method: 'POST',
            headers: { 'Accept': 'application/json' },
            body: data
        });
        var json = await res.json();

        if (json.ok) {
            feedback.className = 'form-feedback mt-4 p-4 rounded-sm text-sm text-center bg-[#AED18E]/20 text-[#2C6E68] border border-[#AED18E]';
            feedback.textContent = 'Message envoyé avec succès. Le cabinet vous répondra sous 48h ouvrées.';
            form.reset();
        } else {
            var msg = json.errors ? json.errors.map(function(e){ return e.message; }).join(', ') : 'Une erreur est survenue.';
            feedback.className = 'form-feedback mt-4 p-4 rounded-sm text-sm text-center bg-red-50 text-red-700 border border-red-200';
            feedback.textContent = msg;
        }
    } catch (err) {
        feedback.className = 'form-feedback mt-4 p-4 rounded-sm text-sm text-center bg-red-50 text-red-700 border border-red-200';
        feedback.textContent = 'Impossible de contacter le serveur. Veuillez réessayer ou contacter le cabinet au 07 70 28 25 46.';
    }

    btn.disabled = false;
    btn.textContent = originalText;
}
