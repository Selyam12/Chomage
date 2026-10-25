# Suivi du chômage

Ce dépôt sert à organiser et suivre le dossier d'indemnisation chômage de son
propriétaire : démarches France Travail, échéances, pièces justificatives,
estimations et historique des échanges.

## Principes de travail

- Répondre et rédiger en français, sauf demande contraire.
- Utiliser les dates au format `JJ/MM/AAAA` et le fuseau `Europe/Paris`.
- Distinguer explicitement les faits sourcés, les calculs, les hypothèses et
  les actions restant à faire.
- Ne jamais présenter une estimation comme une décision de France Travail ;
  indiquer les éléments à confirmer auprès de l'organisme.
- Pour tout calcul, conserver les données d'entrée, la formule, la date de
  référence et les règles utilisées afin qu'il soit reproductible.
- Vérifier les règles, montants et échéances actuels sur une source officielle
  lorsque la demande dépend d'informations susceptibles d'avoir changé.

## Données sensibles

Les documents du dossier peuvent contenir des données personnelles,
financières ou de santé. Les traiter comme confidentiels.

- Ne pas recopier dans les réponses les numéros de sécurité sociale, adresses,
  coordonnées bancaires, identifiants ou autres données inutiles.
- Minimiser les données ajoutées à de nouveaux fichiers et préférer les
  références aux pièces source.
- Ne pas envoyer, publier, partager ou supprimer de documents sans une
  instruction explicite de l'utilisateur.
- Préserver les originaux ; travailler sur des copies pour toute annotation ou
  transformation.

## Organisation recommandée

- `documents/` : pièces reçues, en conservant les originaux.
- `suivi/` : journal des démarches, échéances et prochaines actions.
- `calculs/` : estimations et leurs hypothèses.
- `courriers/` : brouillons de messages et courriers, jamais envoyés sans
  validation explicite.

Créer ces dossiers uniquement lorsqu'ils deviennent nécessaires. Employer des
noms de fichiers descriptifs, sans données personnelles superflues, et datés
en `AAAA-MM-JJ` quand cela aide au tri.

## Contrôles avant livraison

- Citer la pièce ou la source officielle à l'origine de chaque information
  importante.
- Recalculer les totaux et signaler toute incohérence détectée.
- Relire les courriers pour vérifier les dates, références et pièces jointes.
- Ne prendre aucune action externe (envoi, dépôt sur un portail, partage) sans
  accord explicite de l'utilisateur.
