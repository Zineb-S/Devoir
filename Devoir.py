
########################################## Exercices 1 #################################################################
"""
ouvrante_list = ["[", "{", "("]
fermante_list = ["]", "}", ")"]

# Vérification

def check(myStr):
    stack = []
    for i in myStr:
        if i in ouvrante_list:
            stack.append(i)
        elif i in fermante_list:
            pos = fermante_list.index(i)  # on cherche l'index de i
            if ((len(stack) > 0) and (ouvrante_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "Non équilibré"
    if len(stack) == 0:
        return "équilibré"
    else:
        return "Non équilibré"

string = "{[{}{}]}[()]{{}{}}[]{}()"
print(string, "-", check(string))

string = "{()}[){(})"
print(string, "-", check(string))
"""
"""
                            Explication :   
                            
~~~On commence par initialiser une pile vide dans laquelle on va poser les éléments du string qu'on veut tester .
~~ Dans une boucle  for , " i " prend la valeur de chaque élément. 
~~ Si i est presente dans la liste ouvrante on procède à l'ajouter dans la pile.
~~ Si non on vérifie si i est dans la liste fermante et on associe une valeur " pos " a son index 
~~ Si le complèmentaire a i dans la liste fermente existe avec la même pos dans la liste ouvrante et ce complémentaire 
se situe juste avant dans la pile on procède à enlenver le dernier élément parcequ'on vient de trouver des parentheses équilibrées
~~ si on teste tous les éléments on vérifie si la pile est vide ou non d'où les résultats d'expressions équilibrées ou non 


                             Complexité:
                             
O(n) car on a une seule boucle qui parcours l'expression n fois 
"""
########################################## Exercices 2 #################################################################

from collections import deque

# Below lists detail all eight possible movements from a cell
# (top, right, bottom, left, and four diagonal moves)
row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]


# Function to check if it is safe to go to position `(x, y)`
# from the current position. The function returns false if `(x, y)`
# is not valid matrix coordinates or `(x, y)` represents water or
# position `(x, y)` is already processed.

def isSafe(mat, x, y, processed):
    return (x >= 0) and (x < len(processed)) and \
           (y >= 0) and (y < len(processed[0])) and \
           (mat[x][y] == 1 and not processed[x][y])


def BFS(mat, processed, i, j):
    # create an empty queue and enqueue source node
    q = deque()
    q.append((i, j))

    # mark source node as processed
    processed[i][j] = True

    # loop till queue is empty
    while q:

        # dequeue front node and process it
        x, y = q.popleft()

        # check for all eight possible movements from the current cell
        # and enqueue each valid movement
        for k in range(8):
            # skip if the location is invalid, or already processed, or has water
            if isSafe(mat, x + row[k], y + col[k], processed):
                # skip if the location is invalid, or it is already processed, or consists of water
                processed[x + row[k]][y + col[k]] = True
                q.append((x + row[k], y + col[k]))




mat = [
    [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
]

(M, N) = (len(mat), len(mat[0]))

# stores if a cell is processed or not
processed = [[False for x in range(N)] for y in range(M)]

island = 0
for i in range(M):
    for j in range(N):
        # start BFS from each unprocessed node and increment island count
        if mat[i][j] == 1 and not processed[i][j]:
            BFS(mat, processed, i, j)
            island = island + 1

print("The total number of islands is", island)

"""
                         Explication :
#### DFS:Depth-First Search #### ( méthode de profondeur )

On commence par le sommet v et on le marque comme visité
Quand un sommet u est atteint on le parcours jusqu'à ce que tous ses sommets adjacents ont été visités

#### BFS:Breadth-First Search #### (méthode de la distance plus courte )

On commence par explorer un nœud source, puis ses successeurs, puis les successeurs non explorés des successeurs... etc 

~~~~ La méthode qu'on a utilisé dans cette exercice est la BFS !!
Voici un breakdown des étapes que notre code suit pour touver le nombre final des îles 

1) On a une matrice de dimensions M,N composée des 0 et 1 et une liste processed qui nous montre si une position a déjà passé par la fct BFS ou non 
               
2) La boucle for parcours le premier élément si ce dernier n'est pas traité on commence la méthode BFS et une fois
 qu'elle soit terminée on incrémente le nombre d'île .

3) La fonction BFS prend comme arguments la matrice la liste processed et les index de la postion actuelle

4)on intialise une file et on y ajoute les index i et j puis on marque cette position comme traité (processed)

5) en entre dans une boucle while (tant qu'il y a des éléments dans la file) enlève les index i et j de la file et 
on procède a faire les traitement sur les 8 mouvements autour de notre position actuelle

6) on fait appelle a la fonction isSafe qui vérifie si cette position n'est pas déjà traité , ne dépasse pas les dimensions spécifiées
ne contient pas de l'eau 

7) si oui on marque cette position comme traité et on change sa valeur dans la liste processed par true 

8) Une fois le traitement terminé sur tout les mouvements possibles on sort de la BFS et on incrément le nb d'îles comme j'ai mentionné précedemment

                         Complexité:
 La complexité est de O ( M*N ) car le parcours de notre boucle dépend des dimensions de la matrice                              

"""

########################################## Exercices 3 #################################################################
"""
tableau =[-2, -5, 6, -2, -3, 1, 5, -6]
n=len(tableau)
ix = 0
g = 0
h = 0
vmax = tableau[ix]


def maxsomme(tableau,  n,  vmax,  g, h):
    ix = 0
    vmax = tableau[ix]
    somme = 0
    for  jx in range (0,n):
        if (somme < 0):
            somme = 0
            ix = jx
        somme += tableau[jx]
        if (somme > vmax):
            vmax = somme
            g = ix
            h = jx
    print(vmax)
maxsomme(tableau,  n, vmax,  g, h)
"""
"""
                         Explication :
                        
~~ On commence par donner vmax la valeur du premier élément de la liste car on le considère comme la valeur maximale pour l'instant 
~~ ix est l'index du premier élément et jx est la valeur des index qui va changer à chaque fois en parcourant la boucle for 
~~ somme est une variable qu'on incrémente avec la valeur d'élément d'index jx si seulement on finie de vérifier la condition if 
~~dans cette condition on affecte jx à ix si la somme est inférieur à 0 on la réintialise à 0 encore une fois 
~~ la deuxième condition consiste à comparer cette somme avec vmax si elle est supérieure alors la nouvelle valeur de vmax devient la somme elle même .
~~ g et h sont les valeurs qui vont délimitées les éléments contigus qui ont la somme maximale dans toute la liste 
~~ Ainsi on continue a parcourir la liste jusqu'a ce qu'on trouve une somme maximale comprise entre tableau[g] et tableau[h] 

                         Complexité:
                             
O(n) car on a une seule boucle qui parcours l'expression n fois 
"""
########################################## Exercices 4 #################################################################


"""
words = ["go","bat","me","eat","goal","boy", "run","boom"]
chars = ['e','o','b','a','m','g','l']
dictionnaire= dict()
def filling (words,chars,dictionnaire):
    for i in words:
        chars = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
        s = 0
        dictionnaire[i]=[]
        for j in range(len(i)):
            if i[j] in chars:
                dictionnaire[i].append(i[j])
                s += 1
                chars.remove(i[j])
        if s == len(i):
            print(i)
filling(words,chars,dictionnaire)
"""
"""
                                   Explication :
 ~~ La solution de cet exercice consiste simplement à créer un dictionnaire vide où ses clé seront les mots de la liste 
 words et les valeurs seront chaque lettre du mot         
 ~~ lorsqu'on ajoute les valeurs à la clé on verifie si ils sont présentent dans la liste des chars puis l'enlever 
 afin d'eviter la repetition de la lettre si elle occure plus d'une fois dans le meme mot                       
                                   Complexité:
                             
O(n**2) car on a deux boucle imbriquées où la première parcours les mots et la deuxième parcours chaque lettre de ces mots 
"""
########################################## Exercices 5 #################################################################
"""
def counts_sets(array,total):
    memo=dict()
    return rec (array,total, len(array)-1,memo)
def rec (array, total , i ,mem):
    key = str (total) + ":"+ str (i)
    if key in mem :
        return mem[key]
    if total == 0:
        solution=1
    elif total<0:
        solution=0
    elif i < 0:
        solution=0
    elif total< array[i]:
        solution = rec(array,total,i-1,mem)
    else:
        solution = rec(array,total-array[i],i-1,mem) + rec(array,total,i-1,mem)
    mem[key]=solution
    if solution ==0:
        return False
    else:
        return True
list= [3, 34, 4, 12, 5, 2]

print(counts_sets(list,9))
"""
"""
                         Explication :
                         
~~~La solution ici consiste a commencer par un ensemble vide qu'on a "ramifier" tout au long de notre procédure 
~~par exemple on aurait une branche qui va contenir un 10 et l'autre branche n'aurait pas un 10 , passant alors au 6 
il y aurait des branche avec {10,6} ,{10},{6} ou bien un ensemble vide.
~~ Finalement on va chercher dans chaque branche , soit contenant 10 soit non , le total qu'on veut trouver et à chaque fois 
on trouve des ensembles vérifiant nos condition on incrémente la variable solution afin de trouver le nombre final d'ensembles.

                         Complexité:

Notre solution fait des appels récursives dans la 1ère et 2ème fonction qui seront au maximum: appels = (total*n*2)+1
si on élimine les constantes on aurait une complexité de O(n)
"""
