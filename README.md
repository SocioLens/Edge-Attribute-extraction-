![](https://nsa40.casimages.com/img/2021/03/20/210320031955219639.png)

# Socio-Lens : Network 

Vous retrouverez dans ce répertoire les différents outils développés par le cabinet Socio-Lens pour réaliser une analyse de réseaux sociaux. 
Le répertoire comprend :

- Un formulaire codé en HTML Webform ainsi qu'un lien permettant de retrouver le formulaire hébergé sur le site FramaForm
- Un programme d'extraction des données de réseaux codé en Python
- Un exemple d'analyse réalisé via Jupyter et mobilisant le module Networkx 

## Formulaire : 

Le questionnaire réalisé pour la collecte des données nécessaires à la constitution du réseau est fourni au format WebForm de manière à être aisément inséré dans une page internet. Le formulaire est également disponible sur le site internet "[FramaForm](https://framaforms.org/node/401440/clone/confirm)" et peut être modifié/partagé via cette plateforme. 
Nous tenons malgré tout à prévenir les futur.e.s utilisateur.trice.s du questionnaire que toute modification induite au questionnaire suppose des modification au programme d'extraction des données. Le programme fonctionnant par indexation des colonnes, certaines valeurs devront être modifiées si la position relative des questions se trouve modifiée. 

Exemple : Si l'utilisateur décide d'ajouter deux nouvelles questions à la première partie du questionnaire.

Original :

```python
dfn=df[[9,12,13,14,15,16,17,18,19,20,21]].applymap(lambda x: np.nan if x =="Prénom Nom" else x)
```

 Si 2 questions sont ajoutées dans la première partie : 

```python
dfn=df[[11,14,15,16,17,18,19,20,21,22,23]].applymap(lambda x: np.nan if x =="Prénom Nom" else x)
```

La majorité des modifications faites au questionnaire n'induisent que des modifications mineures au programme (comme celle que nous venons de montrer) et peuvent simplement être réalisées par l'utilisateur. Il est néanmoins essentiel d'être conscient de la nécessité des changements avant de réaliser toute modification sur le questionnaire. 

## Extraction : 

Le programme d'extraction permet de réaliser les étapes décrites dans le rapport final d'enquête.
Nous fournissons une version exécutable du programme ainsi que le code source :

- L'exécutable permet d'extraire directement les données de réseaux si le formulaire n'a pas été altéré. 
- Le code source permet de réaliser des modifications en accord avec les changements réalisés sur le questionnaire ou de modifier/ajouter des fonctionnalités à celles que nous avons intégrées. 

Pour utiliser la version exécutable de notre programme il convient de : 

- Télécharger les données de résultats au format : .xlsx (possibilité offerte sur le site FramaForm)
- Télécharger les données sans étiquettes 
- Positionner le fichier de données dans le même répertoire que l'exécutable 

Lorsque ces étapes ont été réalisées, le programme peut être lancé et il convient uniquement d'indiquer le nom du fichier contenant les données : 

![](https://nsa40.casimages.com/img/2021/03/20/210320033044489635.png)

 

Le programme fournit alors deux fichiers Excel : Le premier présente l'ensemble des paires de nœuds du réseau et le second indique pour chacun des nœuds le sexe de l'individu correspondant. 
Ces deux fichiers peuvent être, après des nettoyages mineurs (réalisables directement sous excel), importés et exploités pour l'analyse. 



## Exemple :

Le dernier fichier présent dans le répertoire est un exemple d'analyse. Nous avons simplement tenu à montrer certaines possibilités d'analyses et de visualisation pouvant être réalisées avec un jeu de données simple (4 répondants au questionnaire). 
Nous renvoyons les utilisateurs vers la documentation présente sur le site internet du module [Networkx](https://networkx.org/documentation/stable/tutorial.html) ainsi qu'à l'ouvrage : "A First Course in Network Science" pour approfondir et compléter notre exemple.   

Il est également possible de réaliser directement l'analyse via le logiciel [Gephi](https://gephi.org/). Pour ce faire, nous recommandons d'importer les données via Networkx et de les exporter au format "gexf" : 

```python
import networkx as nx 

G= nx.read_edgelist('Dictionnaire_liens.csv',create_using=nx.Graph(),comments="node", delimiter=',') #Importation des données

nx.write_gexf(G, "graph.gexf") #Exportation vers Gephi 
```









