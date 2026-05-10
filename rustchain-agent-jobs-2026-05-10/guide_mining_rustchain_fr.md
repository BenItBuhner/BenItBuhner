# Guide de configuration du minage RustChain

Ce guide explique, en francais, le parcours general pour installer, configurer et verifier un mineur RustChain. RustChain utilise Proof-of-Antiquity, ou Preuve d'Anciennete: le reseau valorise non seulement la participation, mais aussi le materiel reel et verifiable, y compris les machines anciennes.

## 1. Comprendre le role du mineur

Un mineur RustChain n'est pas seulement un programme qui tourne en arriere-plan. Il represente une combinaison de trois elements:

- un identifiant de mineur ou portefeuille, souvent appele `miner_id`;
- une machine physique avec des caracteristiques materielles;
- des attestations regulieres qui prouvent que la machine est active.

Une attestation est une preuve envoyee au reseau. Elle indique que le mineur est present pendant une periode donnee, appelee epoch. Le mot "attestation" peut rester en anglais dans la documentation technique, car il designe une preuve de presence et de profil materiel.

## 2. Preparer Linux

Sur une distribution Linux recente, commencez par installer les outils de base:

```bash
sudo apt update
sudo apt install -y git curl ca-certificates
```

Selon la version du mineur, vous pourriez aussi avoir besoin de Python, de Rust, de bibliotheques systeme ou d'outils de compilation. Verifiez toujours le README officiel du depot RustChain avant de lancer une installation definitive.

## 3. Recuperer le projet

Clonez le depot officiel:

```bash
git clone https://github.com/Scottcjn/Rustchain.git
cd Rustchain
```

Ensuite, lisez les fichiers de documentation disponibles dans le depot, en particulier le README, les guides d'API et les notes liees a Proof-of-Antiquity. Les commandes exactes peuvent changer rapidement dans un projet experimental.

## 4. Configurer l'identite du mineur

Choisissez un `miner_id` stable. Evitez de changer cet identifiant a chaque execution, car le reseau doit pouvoir associer vos attestations a la meme identite.

Une configuration typique contient:

- l'URL du noeud RustChain;
- le `miner_id` ou portefeuille;
- les options d'attestation materielle;
- eventuellement des parametres de journalisation.

Exemple conceptuel:

```text
NODE_URL=https://explorer.rustchain.org
MINER_ID=votre_identifiant_rtc
```

Ne considerez pas cet exemple comme un fichier de configuration universel. Il montre seulement les valeurs que vous devrez probablement fournir.

## 5. Lancer la premiere attestation

Une fois les dependances installees et l'identite configuree, lancez le client de minage ou d'attestation selon les instructions du depot.

Le but de la premiere execution est de verifier quatre points:

- le programme demarre sans erreur;
- le noeud public est joignable;
- votre materiel est detecte de maniere coherente;
- votre mineur apparait dans les donnees de l'epoch ou de la liste des mineurs.

## 6. Verifier l'etat du reseau

Ces endpoints publics sont utiles pour un premier diagnostic:

```bash
curl -s https://explorer.rustchain.org/health
curl -s https://explorer.rustchain.org/epoch
curl -s https://explorer.rustchain.org/api/miners
```

`/health` indique si le noeud repond. `/epoch` donne le contexte de la periode courante. `/api/miners` permet d'observer les mineurs connus ou actifs, selon l'implementation du noeud.

## 7. Attendre le settlement

Les recompenses ne sont pas toujours visibles immediatement. Dans un systeme par epoch, la participation est souvent calculee a la fin d'une periode, puis distribuee pendant une etape de settlement, ou reglement. Attendez la fin d'une epoch complete avant de conclure que la configuration ne fonctionne pas.

## 8. Conseils pratiques

Gardez des notes sur votre machine: modele, processeur, architecture, systeme d'exploitation et date des tests. Pour RustChain, ces informations sont importantes car la valeur culturelle du projet vient de la diversite materielle.

Evitez les fausses declarations. Proof-of-Antiquity n'a de sens que si les attestations refletent du materiel reel.

Surveillez les journaux. Les erreurs de connexion, les problemes SSL, les timeouts et les mauvais identifiants sont plus courants que les vrais bugs de consensus lors d'une premiere installation.

## 9. Resume

Pour miner RustChain sous Linux:

1. Installez les dependances de base.
2. Clonez le depot officiel.
3. Configurez un `miner_id` stable.
4. Lancez le mineur ou le client d'attestation.
5. Verifiez `/health`, `/epoch` et `/api/miners`.
6. Attendez le settlement de l'epoch.

RustChain recompense la presence materielle verifiable. Une bonne installation est donc a la fois technique et documentaire: faites tourner la machine, prouvez qu'elle existe, et gardez des traces claires.
