'LISTS'
#  - type()
#  - len(list) - lenght of the list

#  - .append(value) - dodaj na kraj
#  - .extend([value,value...]) - prodzuje listu za listu u zagradi
#  - .insert(index,value) - dodaj bilogdje
#  - .insert(len(list),"END") - stavlja na kraj, -1 bi stavilo na predzadnje

#  - del list[index] - izbrisi
#  - .clear() - remove all items, prazne zagrade
#  - .pop(index) - izbrisi ali sacuvaj vrijednost
#  - .pop() - ako je prazno, uklanja zadnji index
#  - .remove(value) - makni preko imena umj indexa, mice samo prvu pojavu!
#  - .index(value) - kaze na kojem indexu se nalazi value
#  - .index(value,starting index)
#  - .index(value,starting index,ending index)
#  - .count(value) - kolko se puta nalazi
#  - .replace(value1,value2)

#  - .sort() - alphabetically, permanently, PRVO SVA VELIKA, pa sva mala. ASCII
#  - .sort(reverse=True) - reverse, permanently
#  - sorted(list) - temporarily, inside print function, ne mijenja original
#  - .reverse() - reverses the list
#  - reversed(...) - ne mijenja original




'STRING method za liste'
#  - "nesto izmedu vrijednosti liste koje spaja".join(list) - osim nakon zadnjeg
#  - "".join(lista).upper() - spaja sve iz liste bez razmaka i u uppercase
#  - "nesto".split(",") - stvara posebni string za sve do zareza
#  - string.split() - napravi novu listu di je svaka rijec jedan elemnt (tj split je na razmacima)

#  - range(od,do) - exculsive
#  - nesto = list()      npr brojevi = list(range(1,10))

'SLICING'
#  - some_list[start:end:step] - end is exclusive



'DICTIONARIES'
#  - for key, value in people.items() - svi key pairs
#  - for key in people.keys() === for key in people - svi keys
#  - for key, value in sorted(people.keys()) - svi keys abecedno

#  - for value in people.values() - sve values
#  - for value in set(people.values()) - bez ponavljanja

#  - .clear() - ocisti cijeli dict
#  - .copy()

#  - create initial dictionaries
#  - {}.fromkeys(["keys"],"value") - creates a pair, each can be string in []!!!
#  -                                key ako rijec mora u []
#  - dict.fromkeys(["keys"/range()], "value")

#  - .get("key") - daje value iz para, ako nema daje None
#  - .get("key", ako nema daje vrijednost koju tu navedemo) - daje value iz para
#  - .pop("key") - removes that key-value pair i vraca value, 
#  -             - ako .pop() - bit ce error jer nema poredak(pa ne uklanja zadnjeg ko kog listi)
#  - .popitem() - removes a radnom pair, vraca cijeli par u obliku tuple
#  - .update(new_dictionary) - updates the whole dict by adding new pairs, 
#  -                           but overrides exisiting pairs(if keys are the same)




'TUPLE'
#  - nesto = (...) ili nesto = tuple(...)
#  - .count(value) - koliko puta se nalazi
#  - .inddx(value) - index prve vrijednosti




'SETS' # can't have duplicates!!, nema indexanja
#  - s = set({1,4,5}) ili = {1,4,5}
#  - set(postojeca_lista) - konverzija u set

#  - .add(value)
#  - .remove(value)
#  - .discard(value) - kao remove, ali ne daje error ako nema trazene value u setu
#  - .copy()
#  - .clear()

'SET_MATH:'
#  - union - | - set1 | set2
#  - intersectionn - & - set1 & set2
# comprehension - kao dictionary ali ima samo 1 value, a ne key_value
#  - {x ** 2 for x in range(10)}



'FOR LAMBDAS'
# map - stvara listu
#  - varijabla = list(map(lambda nesto: nesto, iz_cega))

# filter - filtrira listu
#  - varijabla = list(filter(lambda nesto: vraca samo ako True, nesto_radi_stim))
