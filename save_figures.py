from box import box_plot, bad_plot
box_plot().savefig('box_pairing.svg', transparent=True)
bad_plot().savefig('bad_pairing.svg', transparent=True)

from cantor import cantor_plot
cantor_plot().savefig('cantor_pairing.svg', transparent=True)

from szudzik import szudzik_plot
szudzik_plot().savefig('szudzik_pairing.svg', transparent=True)

from peter import peter_plot
peter_plot().savefig('peter_pairing.svg', transparent=True)

from alternative import alternative_plot
alternative_plot().savefig('alternative_pairing.svg', transparent=True)
