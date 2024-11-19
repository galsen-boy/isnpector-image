# Explication
Ce code est un script Python qui effectue deux tâches principales liées aux images : l'extraction d'informations de localisation à partir des métadonnées EXIF (GPS) d'une image et l'extraction d'une clé PGP (Pretty Good Privacy) cachée dans un fichier. Voici une explication détaillée du code :
1. **Importation des bibliothèques**

- ``argparse`` : Gère les arguments passés en ligne de commande.
- ``PIL.Image (Pillow)`` : Librairie pour manipuler des images (ouvre et extrait des informations EXIF).

2. **Fonction ``rational_to_float(rational)``**

- Cette fonction convertit un nombre "rationnel" (composé de deux entiers représentant un ratio, comme une fraction) en un nombre flottant.
- Cette fonction n'est cependant pas utilisée dans le code fourni.

3. **Fonction ``extract_location(path)``**

- Cette fonction extrait les informations de localisation (latitude et longitude) d'une image si elles sont disponibles dans les métadonnées EXIF.

**Étapes** :

- Ouvre l'image à partir du chemin fourni (path).
- Tente de récupérer les métadonnées EXIF associées à l'image.
- Cherche spécifiquement les données GPS (code EXIF 34853).
- Si les informations GPS (latitude, longitude) sont présentes, la fonction calcule les coordonnées géographiques (latitude et longitude) en degrés, minutes et secondes puis les affiche.

Si aucune donnée GPS n'est trouvée, la fonction affiche un message indiquant que les données de localisation ne sont pas présentes.
4. **Fonction ``extract_pgp(path)``**

- Cette fonction cherche et extrait une clé PGP publique cachée dans un fichier binaire (par exemple, une image).

**Étapes** :

- Ouvre le fichier fourni et lit son contenu binaire.
- Cherche les délimitations des blocs PGP (balises BEGIN PGP PUBLIC KEY BLOCK et END PGP PUBLIC KEY BLOCK).
- Si une clé PGP est trouvée, elle est extraite et affichée. Si non, un message indique que la clé PGP n'a pas pu être récupérée.

5. **Fonction ``main()``**

- Utilise argparse pour définir les options en ligne de commande :
    - ``-steg`` : Option pour spécifier un fichier dont on souhaite extraire une clé PGP.
    - ``-map`` : Option pour spécifier un fichier dont on souhaite extraire les coordonnées GPS.
- Selon l'argument fourni par l'utilisateur, soit la fonction ``extract_pgp`` (pour extraire la clé PGP), soit extract_location (pour extraire la localisation) est appelée. Si aucun argument n'est fourni, une aide est affichée avec les options disponibles.

6. Bloc **if __name__ == "__main__"**:

- Ce bloc exécute la fonction main() uniquement lorsque le script est exécuté directement, et non importé comme un module dans un autre programme.

**Résumé**

Ce script permet d'extraire des informations spécifiques d'un fichier image ou d'un fichier binaire :

- Option ``-map`` : Extrait et affiche la localisation GPS si disponible dans l'image.
- Option ``-steg`` : Extrait et affiche une clé PGP publique cachée dans un fichier, si elle est présente.

**Exemple d'exécution**
```
python script.py -map image.jpg  # Pour extraire la localisation GPS
python script.py -steg fichier.jpg  # Pour extraire une clé PGP cachée
```
