# Algorithme d'optimisation d'un portefeuille d'actions
## Mission:
  **"Sujet : Algorithme pour maximiser nos bénéfices**

  Bonjour,

  J'espère que vous êtes prêt pour votre premier vrai projet ! Nous avons besoin d'aide pour optimiser les solutions de nos clients afin de rendre nos       programmes d'investissement à court terme plus compétitifs. Nous avons besoin que vous conceviez un algorithme qui maximisera le profit réalisé par nos clients après deux ans d'investissement. Votre algorithme doit suggérer une liste des actions les plus rentables que nous devrions acheter pour maximiser le profit d'un client au bout de deux ans.

  Nous avons les contraintes suivantes :

  Chaque action ne peut être achetée qu'une seule fois.

  Nous ne pouvons pas acheter une fraction d'action.

  Nous pouvons dépenser au maximum 500 euros par client.

  Vous trouverez ci-dessous une liste des actions sur lesquelles nous travaillons : 

  **Actions #	Coût par action (en euros)	Bénéfice (après 2 ans)**
  
      Action-1	20	5%
      Action-2	30	10%
      Action-3	50	15%
      Action-4	70	20%
      Action-5	60	17%
      Action-6	80	25%
      Action-7	22	7%
      Action-8	26	11%
      Action-9	48	13%
      Action-10	34	27%
      Action-11	42	17%
      Action-12	110	 9%
      Action-13	38	23%
      Action-14	14	1%
      Action-15	18	3%
      Action-16	08	8%
      Action-17	04	12%
      Action-18 	10	14%
      Action-19	24 	21%
      Action-20	114	18%
  Je sais que vous êtes nouveau dans le monde de la finance, alors voici un aperçu de la signification de chaque colonne : 

 -  Actions – Chaque "Action-#" représente une action dans une entreprise différente. Si vous imaginez la valeur d'une entreprise comme étant une tarte  entière, chaque action est comme une part de cette tarte. 
 -  Coût par action (en euros) – Le coût d'une action de l'entreprise en euros.
 -  Bénéfice (après 2 ans) – Il s'agit du bénéfice réalisé par le titulaire de l'action après 2 ans d'investissement dans l'entreprise. Le bénéfice est un pourcentage du coût de l'action.  
  - Parce que nous voulons être aussi transparents que possible pour nos clients, nous voulons que le programme essaie toutes les différentes combinaisons d'actions qui correspondent à nos contraintes, et choisisse le meilleur résultat.  Le programme doit donc lire un fichier contenant des informations sur les actions, explorer toutes les combinaisons possibles et afficher le meilleur investissement.

 
  Merci ! 
  Robin Greene
  Tech Lead, AlgoInvest&Trade"

## Requirements:
 Pour fonctionner le code a besoin de: **[Python3](https://www.python.org/downloads/)**

## Fonctionnement:
<ol>
<li> Tapez dans votre terminal:

`git clone https://github.com/PascalineBo/Portfolio_algorithm.git`
</li>
<li>  puis positionnez-vous dans le dossier Porfolio_algorithm 
 
 `cd Porfolio_algorithm`
   </li> 
<li>
 
> `python bruteforce.py` ou 
 
> `python optimized.py` ou 
 
> `python optimized2.py`
 </li>
 
 <li> Pour tester **bruteforce.py** et **optimized.py**, vous pouvez importer automatiquement le fichier **input.txt** grâce à votre IDE (sinon le programme vous demande de tout saisir à la main pour 20 actions)
</li>
 
<li> Remarque: le fichier **optimized2.py** importe ses données en lisant le fichier **dataset1_Python+P7.csv**
 
  (si vous voulez traiter un autre fichier csv avec la même organisation de données, il suffit changer le nom du fichier dans le code de la fonction get_shares_data)</li>
