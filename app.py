@app.route("/process", methods=["POST"])
def process():
    # Récupération des données utilisateur
    nom = request.form.get("nom")
    prenom = request.form.get("prenom")
    carte_vitale = request.form.get("carte_vitale")
    jour = request.form.get("jour")
    mois = request.form.get("mois")
    annee = request.form.get("annee")
    qcm_answers = [
        request.form.get("q1"),
        request.form.get("q2"),
        request.form.get("q3"),
        request.form.get("q4"),
        request.form.get("q5"),
    ]

    # Calcul de l'âge
    try:
        naissance = date(int(annee), int(mois), int(jour))
        age = date.today().year - naissance.year
        if date.today() < naissance.replace(year=date.today().year):
            age -= 1
    except:
        age = "Inconnue"

    # Calcul des réponses au QCM
    yes_count = sum(1 for answer in qcm_answers if answer == "Oui")

    # Calcul des mensualités
    base_cost = 50
    additional_cost = yes_count * 10
    total_cost = base_cost + additional_cost

    # Ajustement en fonction de l'âge (simplifié)
    if age != "Inconnue" and age > 65:
        age_surcharge = (age - 65) * 0.01  # 1 % par année au-delà de 65 ans
        total_cost *= (1 + age_surcharge)
    total_cost = round(total_cost, 2)

    return render_template(
        "result.html",
        nom=nom,
        prenom=prenom,
        carte_vitale=carte_vitale,
        age=age,
        yes_count=yes_count,
        total_cost=total_cost,
    )
