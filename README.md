# Image inspector

Cet outil vous aide à explorer et analyser des images avec des capacités avancées pour détecter des informations cachées à l'aide de méthodes stéganographiques. De plus, il vous permet d'extraire les métadonnées GPS pour identifier l'emplacement où l'image a été prise. Que vous ayez besoin de découvrir des données dissimulées ou d'enquêter sur l'origine des images, le programme Image Inspector offre des fonctionnalités essentielles pour un examen et une analyse d'images efficaces.
# Qu'est-ce que la stéganographie ?

La stéganographie est une technique utilisée pour cacher des informations, des messages ou des données à l'intérieur d'un autre fichier ou support apparemment anodin, de manière à dissimuler l'existence du contenu caché. L'objectif de la stéganographie est de s'assurer que les informations cachées restent indétectées par des observateurs occasionnels, en faisant une forme de sécurité par l'obscurité.

## Comment peut-on cacher des informations dans des fichiers normaux ?

Les informations peuvent être cachées dans des fichiers normaux par diverses techniques stéganographiques. Voici quelques méthodes courantes :

  1. **Stéganographie du bit de poids faible (LSB)** : Dans les fichiers image, le bit de poids faible de chaque canal de couleur d'un pixel est remplacé par un bit des données cachées. Comme le changement de couleur des pixels est minime, l'œil humain ne peut pas le détecter, mais les données cachées peuvent être extraites par ceux qui connaissent la technique.

  2. **Technique à spectre étalé**: Dans les fichiers audio, les données cachées sont réparties sur différentes bandes de fréquences, les rendant imperceptibles pour l'oreille humaine. Les données cachées peuvent être extraites par un récepteur qui sait comment les décoder.

  3. **Stéganographie dans les fichiers texte** : Dans les fichiers texte, des informations cachées peuvent être intégrées en utilisant différentes méthodes, comme l'altération des espacements, la modification des caractéristiques de la police ou l'utilisation de caractères invisibles.

  4. **Stéganographie dans les espaces blancs** : Dans les fichiers texte ou HTML, des données cachées peuvent être dissimulées dans les espaces blancs (espaces, tabulations ou sauts de ligne) sans affecter le contenu visible.

  5. **Concaténation de fichiers** : La concaténation de plusieurs fichiers peut cacher des données à la vue de tous, surtout lorsque les fichiers porteurs sont volumineux et complexes.

  6. **Stéganographie vidéo** : Dans les fichiers vidéo, des données cachées peuvent être stockées dans les trames ou les vecteurs de mouvement sans provoquer de changements visibles dans la qualité vidéo.

Il est important de noter que la stéganographie n'est qu'un élément d'un ensemble plus large de mesures de sécurité. Elle est souvent utilisée en complément du chiffrement pour fournir une couche supplémentaire de protection aux données sensibles.
## Comment fonctionne le programme ?

Le programme décrit agit comme un outil de stéganographie avec des fonctionnalités spécifiques.

  1. **Description de l'image et extraction de l'emplacement (avec l'option -map)** : Le programme prend un fichier image en entrée, comme indiqué dans la description du projet. Lorsqu'on utilise le drapeau **-map**, le programme extrait les données GPS des métadonnées de l'image. Ces données GPS peuvent révéler l'emplacement où l'image a été prise.

  2. **Extraction de la clé PGP (avec l'option -steg)** : Lorsqu'on utilise le drapeau **-steg**, le programme lit le contenu du fichier image sous forme de données brutes. Il identifie ensuite le bloc ou la section de l'image où la clé PGP (Pretty Good Privacy) est cachée. La clé PGP peut avoir été intégrée à l'aide d'une technique stéganographique, comme le LSB ou une autre méthode. Le programme localise les points de départ et de fin du bloc caché, puis extrait la clé PGP.



# Comment exécuter

Assurez-vous que Python est installé en exécutant les commandes suivantes :

    sudo apt update
    sudo apt install python3

## Packages pip utilisés :
 Pillow
 ```
  pip install pillow 
 ```
#Utilisation
```
$ python3 image.py -h
usage: image.py [-h] [-steg STEG | -map MAP]

inspector-image

options:
  -h, --help  show this help message and exit
  -steg STEG  Extract PGP key
  -map MAP    Extract location
```
```
$ python3 image.py -map images/image.jpeg
Lat: 32.0866296534937
Lon: 34.885130555555556
```
```
$ python3 image.py -steg images/image.jpeg
-----BEGIN PGP PUBLIC KEY BLOCK-----  
Version: 01  
  
mQENBGIwpy4BCACFayWXCgHH2QqXkicbqD1ZlMUALpyGxDFiWh1SErFUPJOO/CgU  
2688bAd26kxDSGShiL9YUOQJ6MS+zJ0KlBkeKPoQlPHRBVpH7vjcRbZNgDxd82uE  
7mhM6AH+W3fAim/PhU3lm661UGMCHM3YLupa/N0Dhhmfimtg+0AimCoXk6Q6WJxg  
ao8XY1Wqacd2L0ssASY5EkMahNgtX0Ri8snbTlImd5Jq/sC4buZq96IlxyhtX0ew  
zD/md0U++8SxG9+gi+uuImqV8Wq1YHvJH5BtIbfcNG9V00+03ikEX9tppKxCkhzx  
9rSqvyH6Uirs3FVhFtoXUSg8IeYgSH6p5tsVABEBAAG0CDAxQDAxLjAxiQEcBBAB  
AgAGBQJiMKcuAAoJEAJuInmYDhhbO3gIAITZhEtLBj524y1oeBKI5fZDwgCQum6B  
D9ZaUq1+dI98HsiRAiUqw1YbuJQgeUVGCmqXeC3E7VTPCPZsaCLfWWZVeosRIqB8  
PwGxcY6vXHYR4S6T8rHwsNASw+Vo2pmQIGn4tABmtyappqJbwSz+5yg73DjYXiX/  
e/f6i9nrFFsfMjjKd71cAyHjV8u0z7fGDXpR22vo7CdloXMxsZRyHjd/4ofUgvu0  
6hWYG2zBWTXpwaYRU9u1NCr1gfKnukm8gbILSSgjr8pQ3OLWHleJXc0sCEJFKSbg  
+I0KJP7Ccrxy0MaKYk0T0tYbBrvqQCzXqzAqcjn+1GoDDS1J8WBJopM=  
=N8hc  
-----END PGP PUBLIC KEY BLOCK-----
```

### Quelles sont les questions d'audit ??
[Cliquez ici pour voir les questions d'audit.](https://github.com/01-edu/public/tree/master/subjects/cybersecurity/inspector-image/audit)

#### Authored by: [DAIBOU BA](https://learn.zone01dakar.sn/git/daiba/)
###### Completed during [zone01-dakar](https://learn.zone01dakar.sn/) full-stack development course.
#### Project Description: [here](https://github.com/01-edu/public/tree/master/subjects/cybersecurity/inspector-image)


