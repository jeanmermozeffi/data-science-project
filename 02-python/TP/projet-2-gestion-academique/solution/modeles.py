"""
Classes du domaine "académique".
Chapitre mobilisé : 05-POO (héritage, polymorphisme, encapsulation).
"""


class Etudiant:
    """Étudiant standard. notes = {matiere: (note, coefficient)}"""

    def __init__(self, nom: str, notes: dict):
        self.nom = nom
        self.notes = notes

    def moyenne_ponderee(self) -> float:
        total_points = sum(note * coef for note, coef in self.notes.values())
        total_coefs = sum(coef for _, coef in self.notes.values())
        if total_coefs == 0:
            return 0.0
        return total_points / total_coefs

    def mention(self) -> str:
        """Méthode polymorphe : seuils standards, redéfinie dans EtudiantRedoublant."""
        moyenne = self.moyenne_ponderee()
        if moyenne >= 16:
            return "Très bien"
        if moyenne >= 14:
            return "Bien"
        if moyenne >= 12:
            return "Assez bien"
        if moyenne >= 10:
            return "Passable"
        return "Insuffisant"

    def bulletin(self) -> str:
        lignes = [f"Bulletin de {self.nom} ({self.__class__.__name__})"]
        for matiere, (note, coef) in self.notes.items():
            lignes.append(f"  - {matiere:<15} : {note}/20 (coef {coef})")
        lignes.append(f"  Moyenne pondérée : {self.moyenne_ponderee():.2f}/20 — Mention : {self.mention()}")
        return "\n".join(lignes)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.nom}, moyenne={self.moyenne_ponderee():.2f})"


class EtudiantBoursier(Etudiant):
    """Hérite d'Etudiant, ajoute le calcul de bourse selon un barème de moyennes."""

    def __init__(self, nom: str, notes: dict, bareme: list, montant_plein: float):
        super().__init__(nom, notes)
        self.bareme = bareme
        self.montant_plein = montant_plein

    def calcul_bourse(self) -> float:
        moyenne = self.moyenne_ponderee()
        for seuil, taux in self.bareme:
            if moyenne >= seuil:
                return self.montant_plein * taux
        return 0.0

    def bulletin(self) -> str:
        base = super().bulletin()
        return base + f"\n  Bourse attribuée : {self.calcul_bourse():,.0f} FCFA/mois".replace(",", " ")


class EtudiantRedoublant(Etudiant):
    """Hérite d'Etudiant, redéfinit mention() avec des seuils plus stricts (polymorphisme)."""

    def mention(self) -> str:
        moyenne = self.moyenne_ponderee()
        if moyenne >= 14:
            return "Bien (progression notable)"
        if moyenne >= 10:
            return "Passable — passage conditionnel"
        return "Insuffisant — maintien en formation"


class Promotion:
    """Regroupe une liste d'Etudiant et fournit les analyses de la promotion."""

    def __init__(self, etudiants: list):
        self.etudiants = etudiants

    def classement(self) -> list:
        # lambda + sorted() : Chapitre 04
        return sorted(self.etudiants, key=lambda e: e.moyenne_ponderee(), reverse=True)

    def moyenne_promotion(self) -> float:
        moyennes = [e.moyenne_ponderee() for e in self.etudiants]
        return sum(moyennes) / len(moyennes) if moyennes else 0.0

    def etudiants_en_difficulte(self) -> list:
        # filter() : Chapitre 04
        return list(filter(lambda e: e.moyenne_ponderee() < 10, self.etudiants))

    def rapport(self) -> str:
        lignes = ["=" * 55, "RAPPORT DE PROMOTION — Data Science Batch 7", "=" * 55]
        lignes.append(f"Effectif                : {len(self.etudiants)}")
        lignes.append(f"Moyenne de promotion    : {self.moyenne_promotion():.2f}/20")

        lignes.append("\n-- Classement --")
        for rang, etudiant in enumerate(self.classement(), start=1):
            lignes.append(f"  {rang}. {etudiant.nom:<20} {etudiant.moyenne_ponderee():.2f}/20  ({etudiant.mention()})")

        en_difficulte = self.etudiants_en_difficulte()
        lignes.append(f"\n-- Étudiants en difficulté (< 10/20) : {len(en_difficulte)} --")
        for etudiant in en_difficulte:
            lignes.append(f"  ⚠️  {etudiant.nom} — {etudiant.moyenne_ponderee():.2f}/20")

        lignes.append("=" * 55)
        return "\n".join(lignes)
