# Pyramide d'audience

Les mesures théoriques sont expliquées dans le fichier `theory.ipynb`.

## Workflow

Ordre d'exécution recommandé :

1. `get_data.ipynb` récupère les statistiques d'audience pour une année donnée à partir de https://stats.data.gouv.fr
2. `add_ids` ajoute les données de https://data.gouv.fr aux statistiques d'audience
3. `knee.ipynb` calcule le point d'inflexion et génère un listing pour le haut de la pyramide `out/top-{année}.csv` et le bas `out/bottom-{année}.csv`
4. `dgfr.update.ipynb` met à jour les fiches des jeux de données produit sur https://data.gouv.fr
