## 01-DML
# Tables 
1- Agences
2- employes
3- clients
4- comptes
5- Types_compte
6- cartes
7- transactions
8- prets
9- remboursements
10- beneficiaires

colonne, types, contraintes
### Agences
id_agences (SERIAL, PK)
code_agence (VARCHAR(5), NOT NULL, UNIQUE)
nom, ville, region (VARCHAR, NOT NULL)
telephone VARCHAR(20),
date_ouvertures DATE DEFAULT today,
actif BOOLEAN DEFAULT TRUE,


## Relation
Agences **ratache** Client => Un client est rattaché à une agence
Agences **emploie** Employes => Une agence emploie un ou plusieurs employes
Client => Compte
Client => types_compte
