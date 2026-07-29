"""
Classes du domaine "analyse de sentiment".
Chapitre mobilisé : 05-POO.
"""
from nettoyage import nettoyer_texte
from analyse import calculer_score, mots_les_plus_frequents


class Avis:
    def __init__(self, texte: str, client: str, note_etoiles: int):
        self.texte = texte
        self.client = client
        self.note_etoiles = note_etoiles
        self.tokens = nettoyer_texte(texte)  # nettoyage fait une seule fois, à la construction

    def __repr__(self):
        return f"Avis({self.client}, {self.note_etoiles}★, '{self.texte[:30]}...')"


class AnalyseurSentiment:
    def __init__(self, lexique: dict, negations: set, seuil_positif: int, seuil_negatif: int):
        self.lexique = lexique
        self.negations = negations
        self.seuil_positif = seuil_positif
        self.seuil_negatif = seuil_negatif

    def score(self, avis: Avis) -> int:
        return calculer_score(avis.tokens, self.lexique, self.negations)

    def classifier(self, avis: Avis) -> str:
        s = self.score(avis)
        if s >= self.seuil_positif:
            return "positif"
        if s <= self.seuil_negatif:
            return "négatif"
        return "neutre"

    def repartition_sentiments(self, avis_liste: list) -> dict:
        repartition = {"positif": 0, "neutre": 0, "négatif": 0}
        for avis in avis_liste:
            repartition[self.classifier(avis)] += 1

        total = len(avis_liste)
        return {sentiment: round(100 * n / total, 1) for sentiment, n in repartition.items()} if total else repartition

    def mots_frequents_avis_negatifs(self, avis_liste: list, top_n: int = 10) -> list:
        tokens_negatifs = [avis.tokens for avis in avis_liste if self.classifier(avis) == "négatif"]
        return mots_les_plus_frequents(tokens_negatifs, top_n)

    def tableau_croise_etoiles_sentiment(self, avis_liste: list) -> dict:
        """Pour chaque nombre d'étoiles, compte combien d'avis sont positif/neutre/négatif."""
        tableau = {}
        for avis in avis_liste:
            etoiles = avis.note_etoiles
            sentiment = self.classifier(avis)
            tableau.setdefault(etoiles, {"positif": 0, "neutre": 0, "négatif": 0})
            tableau[etoiles][sentiment] += 1
        return dict(sorted(tableau.items()))

    def rapport(self, avis_liste: list) -> str:
        lignes = ["=" * 55, "RAPPORT D'ANALYSE DE SENTIMENT — Avis clients CI-Shop", "=" * 55]

        lignes.append(f"Nombre d'avis analysés : {len(avis_liste)}\n")

        lignes.append("-- Répartition des sentiments --")
        for sentiment, pourcentage in self.repartition_sentiments(avis_liste).items():
            lignes.append(f"  {sentiment:<10} : {pourcentage}%")

        lignes.append("\n-- Mots les plus fréquents dans les avis négatifs --")
        for mot, frequence in self.mots_frequents_avis_negatifs(avis_liste):
            lignes.append(f"  {mot:<15} ({frequence} fois)")

        lignes.append("\n-- Tableau croisé étoiles / sentiment détecté --")
        for etoiles, repartition in self.tableau_croise_etoiles_sentiment(avis_liste).items():
            lignes.append(f"  {etoiles}★ : {repartition}")

        lignes.append("=" * 55)
        return "\n".join(lignes)
