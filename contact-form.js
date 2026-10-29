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
        // Formspree signale le succes par le statut HTTP et un champ "next" dans la
        // reponse, pas par un champ "ok". Tester json.ok affichait une erreur au
        // visiteur alors que son message etait bien parti.
        var json = {};
        try { json = await res.json(); } catch (e) {}

        if (res.ok) {
            feedback.className = 'form-feedback mt-4 p-4 rounded-sm text-sm text-center bg-[#AED18E]/20 text-[#2C6E68] border border-[#AED18E]';
            feedback.textContent = 'Message envoyé avec succès. Le cabinet vous répondra sous 48h ouvrées.';
            form.reset();
        } else {
            var champEmail = json.errors && json.errors.some(function(e){ return e.field === 'email'; });
            var msg = champEmail
                ? 'L\'adresse email semble incorrecte. Merci de la vérifier.'
                : 'Le message n\'a pas pu être envoyé. Veuillez réessayer ou appeler le cabinet au 07 70 28 25 46.';
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
