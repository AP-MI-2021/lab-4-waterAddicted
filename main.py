import math

def citire_lista():
    result_list = []
    lst = input('Introduceti lista:')
    str_lst = lst.split()
    for string_element in str_lst:
        element = int(string_element)
        result_list.append(element)
    return result_list

def liste_cu_numpar_par_de_elemente(lst1,lst2):
    '''
    Functia verifica daca cele doua liste au acelasi numar de elemente pare
    :param lst1: prima lista de elemente
    :param lst2: a doua lista de elemente
    :return: returneaza True daca listele au acelasi numar de pemente pare sau False in caz contrar.
    '''
    numar_pare1=0
    numar_pare2=0
    for i in range(0,len(lst1)):
        if lst1[i] % 2 == 0:
            numar_pare1 +=1

    for i in range(0,len(lst2)):
        if lst2[i] % 2 == 0:
            numar_pare2 +=1
    if numar_pare1 == numar_pare2:
        return  True
    return False

def intesectia_listelor(list1,list2):
    '''
    Functia va returna intesectia dintre prima si a doua lista.
    :param list1: prima lista
    :param list2: a doua lista
    :return: o lista alcatutita din termenii comuni ai listelor sau none in cazul in care listele nu au termeni in comun.
    '''
    result_list = []
    for i in range(0,len(list1)):
        for j in range(0,len(list2)):
            if list1[i] == list2[j]:
                result_list.append(list1[i])

    if len(result_list) == 0:
        return None
    return result_list

def creare_element_nou(a,b):
    '''
    Concateneaza elementul a cu elementul b.
    :param a: primul element
    :param b: al odilea element
    :return: un element de forma ab
    '''
    adaos = int(math.log(b,10)) + 1
    zeros_add=10**adaos
    return a*zeros_add+b

def get_oglindit(nr):
    '''
    Creeza oglinditul unui numar.
    :param nr: numarul
    :return: numarul oglindit
    '''
    oglindit = 0

    while nr > 0:
        oglindit = oglindit * 10 + nr % 10
        nr = nr // 10

    return oglindit


def palindrom(nr):
    '''
    Verifica daca un numar este palindrom
    :param nr: numarul verificat
    :return: true daca este paldinrom
    '''
    oglindit = get_oglindit(nr)
    return oglindit == nr


def concatenare_elem_palindrom(list1,list2):
    '''
    Funcita va concatena elementele de pe aceasi pozitii din cele doua liste si va verifica daca numarul nou format este un palindrom..In caz afirmativ acesta va fi introdus intr-o lista noua(pnetru rezultate)

    :param list1: prima lista
    :param list2: a doua lista
    :return: o lista fomrata din palindroame dupa concatenarea elementelor de pe aceleasi pozitii sau none in cazul nexistentei acestora
    '''
    result_list=[]
    m = min(len(list1),len(list2))
    pass
    for i in range(0,m):
        nou = creare_element_nou(list1[i],list2[i])
        if palindrom(nou):
            result_list.append(nou)

    if len(result_list)  == 0:
        return None
    return result_list

def inlcuire_palindoame_a_elem_div_cu_list3(list1,list2,list3):
    '''
    Verifica daca elementele din primele doua liste unst divizibile cu toate elementele din a treia lista,iar in caz afirmativ le inverseaza.
    :param list1: prima lista
    :param list2: a doua lista
    :param list3: lista cu divizori
    :return: un touple format din doua liste
    '''
    result_list1 = []
    result_list2 = []
    for i in range(0,len(list1)):
        dev = True
        for j in range(0,len(list3)):
            if list1[i]%list3[j] != 0:
                dev = False
        if dev == True:
            result_list1.append(get_oglindit(list1[i]))
        else:
            result_list1.append(list1[i])

    for i in range(0,len(list2)):
        dev = True
        for j in range(0,len(list3)):
            if list2[i]%list3[j] != 0:
                dev = False
        if dev == True:
            result_list2.append(get_oglindit(list2[i]))

        else:
            result_list2.append(list2[i])

    return (result_list1,result_list2)

def main():
    list1 = []
    list2 = []
    lista_goala1 = True
    lista_goala2 = True
    while True:
        print('1.   Citire liste.')
        print('2.   Listele au acelasi numar de elemente pare.')
        print('3.   Intersecția listelor citite de la tastatură.')
        print('4.   Afișați toate palindroamele obținute prin concatenarea elementelor de pe aceleași poziții în cele doua liste')
        print('5.   înlocuirea în cele două liste citite la punctul 1 a tuturor elementelor cu oglinditul lor dacă îndeplinesc următoarea regulă: elementele sunt divizibile cu toate elementele din a treia lista. Dacă nu îndeplinesc regula, se păstreaza elementul așa cum e.')
        print('x    Exit.')
        comanda = input('Introduceti comanda:')
        if comanda == '1':
            list1=citire_lista()
            list2=citire_lista()
            lista_goala1 = False
            lista_goala2 = False
        elif comanda == '2':
            if lista_goala1 == True:
                list1 = citire_lista()
                lista_goala1= False
            if lista_goala2 == True:
                list2=citire_lista()
                lista_goala2 = False
            if(liste_cu_numpar_par_de_elemente(list1,list2)):
                print('Au acelasi numar de elemnte pare.')
            print('Nu au aceasi numar de elemnte pare cele doua liste.')

        elif comanda == '3':
            if lista_goala1 == True:
                list1 = citire_lista()
                lista_goala1 = False
            if lista_goala2 == True:
                list2 = citire_lista()
                lista_goala2 = False
            result_list= intesectia_listelor(list1,list2)
            if result_list is None:
                print('Listele nu au elemente in comun.')
            else:
                print(f'Lista elementlor in comun dintre cele doua liste introduse este: {result_list}')


        elif comanda == '4':
            if lista_goala1 == True:
                list1 = citire_lista()
                lista_goala1 = False
            if lista_goala2 == True:
                list2 = citire_lista()
                lista_goala2 = False
            result_list = concatenare_elem_palindrom(list1,list2)
            if result_list == None:
                print('Concatenarea elementelor de pe aceleasi pozitii din cele doua liste nu fromeaza palindroame.')
            else:
                print(f'Lista palindromelor dupa concatenarea elemntelor de pe aceleasi pozitii din liste este {result_list}')


        elif comanda == '5':
            if lista_goala1 == True:
                list1 = citire_lista()
                lista_goala1 = False
            if lista_goala2 == True:
                list2 = citire_lista()
                lista_goala2 = False
            list3 = citire_lista()
            result_list = inlcuire_palindoame_a_elem_div_cu_list3(list1,list2,list3)
            print(result_list)

        elif comanda == 'x':
            break
        else:
            print('Comanda invalida.')


main()
