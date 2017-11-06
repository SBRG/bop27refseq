from co.converters import GenbankConverter
from co.mutation import DEL, INS

component = GenbankConverter.from_file('NC_000913_3.gb')

updated_component = component.mutate([
    DEL(2173363 - 1, 2),
    INS(3560456 - 1, 'G'),
    INS(4296381 - 1, 'CG')
])

GenbankConverter.to_file(updated_component, 'bop27.gb')
