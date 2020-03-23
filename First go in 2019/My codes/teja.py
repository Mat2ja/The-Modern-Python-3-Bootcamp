import colorama
from termcolor import cprint
from random import choice
import time

colorama.init()

colors = ('red', 'green', 'yellow', 'cyan', 'magenta')

voli = [
        'kurac', 'jebačinu', 'sexxxx', 'butt plug', 'mamu', 'krafne', 'ljubav je na selu', 'filipa krovinovića', 'cici mici', 
        'tangice', 'dlakice', 'penis', 'pimpač', 'noge', 'poljubčiće u obrašćiće', 'banane', 'hardkor sex', 'kebab', 'sprijeda', 'straga', 
        'u guzu', 'u picu', 'pizzu', 'jebavanje', 'sesanje', 'pušit kurac', 'pašticadu', 'kad joj cuclaju cice', 'mice', 'kurac u svojoj mici', 
        'pintarest', 'transvestite', 'choking', 'čokoladu', 'trljati picu', 'imati picu trljanu', 'margaretu', 'paradajz', 'dekice', 
        'grah', 'purdit', 'smurdit', 'kade', 'pese', 'da ga prima', 'kaufland', 'muji olovkice', 'voditi ljubav', 'matijuuuuuuuuu']

for n in voli:
    random_color = choice(colors)
    text = f"\t\t\t\t\t\t\t\t\t\t\tTeja voli {n.upper()}!!!!!!!!!!!!\n"
    time.sleep(0.75)
    cprint(text, color=random_color, attrs=['bold'])

# python teja.py

