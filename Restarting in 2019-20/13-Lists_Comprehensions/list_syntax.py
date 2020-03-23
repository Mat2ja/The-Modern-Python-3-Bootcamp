'LISTS'

#  variable = list(range(1,10))
#  - type()
#  - len(list) - lenght of the list

#  - .append(value) - dodaj na kraj
#  - .extend([value,value...]) - prodzuje listu za listu u zagradi
#  - .insert(index,value) - dodaj bilogdje
#  - .insert(len(list),"stoogod dodajemo") - stavlja na kraj, -1 bi stavilo na predzadnje

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
#  - "".join(lista).upper() - spaja sve iz liste bez razmaka i u uppercase, turn the list into string
#  - "nesto".split(",") - stvara posebni string za sve do zareza
#  - string.split() - napravi novu listu di je svaka rijec jedan elemnt (tj split je na razmacima)

#  - range(od,do) - exculsive
#  - nesto = list()      npr brojevi = list(range(1,10))

'SLICING'
#  - some_list[start:end:step] - end is exclusive
#  - some_list[1:] - npr pocinje od 1, stavit :
#  - some_list[:4] - npr zavrsava od 4, stavit :
#  - some_list[1::2] - npr pocinje od 1 do kraja, svaki drugi
#  - some_list[::2] - svaki drugi

# with negative step it reverses the order - krece od kraja do pocetka korakom unazad
#  - some_list[1::-1] - od prvog do nultog indeksa
#  - some_list[:4:-1] - od iza do indeksa 4
#  - some_list[4::-1] - od indeksa 4 do pocetka(najmanjeg indeksa)

#  - some_list[::-1]  - reverses the whole string (olso works for lists)
