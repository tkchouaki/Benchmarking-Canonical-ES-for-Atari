# Benchmarking-Canonical-ES-for-Atari

Ce projet a pour but d'étudier l'algorithme proposé par PatrykChrabaszcz, Ilya Loshchilov et FrankHutter permettant à une Intelligence Artificielle d'apprendre à jouer sur d'anciens jeux Atari.

Le projet s'inscrit dans le cadre du master ANDROIDE dispensé à Sorbonne Université, Paris.

L'organisation est la suivante :

  * le dossier src contient diverses expérimentations pour déployer le code des auteurs sur des clusters ainsi qu'un algorithme de Deep Reinforcement Learning pour comparaison (le code provient d'[ici](https://github.com/omerbsezer/PolicyGradient_PongGame))
  * le dossier references contient un ensemble d'articles cités par le papier original
  * le dossier result contient quant à lui (pour le moment) les résultat obtenus sur un cluster de 24 coeurs - 90Go de RAM sur une durée de 24h.

Pour déployer le code original (`src/Canonical_ES_Atari`) vous pouvez utiliser le dockerfile situé dans `src`. Ce dernier configure un conteneur permettant d'exécuter le code. Sachez que ce conteneur possède un volume permettant de récupérer les résultats.

Pour notre part, nous avons utiliser une instance de [Google Cloud](https://cloud.google.com/) pour exécuter nos experiences. Pour ceux qui souhaiteraient utiliser cette méthode, référez vous simplement à la [documentation](https://cloud.google.com/docs/overview/cloud-platform-services#computing-hosting) traitant du déploiement de conteneurs.
Pour l'algorithme de Deep Reinforcement Learning, vous trouverez également un dockerfile dans `src/PolicyGradient_PongGame`.

Vous pourrez également noter que ce dépôt contient également du code pour déployer les expériences sur le [Cloud Azure](https://azure.microsoft.com/fr-fr/). Néanmoins, cette métode n'a pas vraiment abouti et il vous faudra créer votre propre VM correctement configurée ainsi que remplacer les clés d'accès au stockage.

A terme, le dépôt contiendra également une présentation du travail et les derniers résultats.
