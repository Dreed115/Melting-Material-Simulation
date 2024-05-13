import random

# Función para cambiar los tipos de elementos en el archivo .lmp
def cambiar_tipos_elementos(input_file, output_file, proporcion_tipo_1):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.strip():  # Verifica si la línea no está en blanco
                # Dividir la línea en columnas
                atom_id, atom_type, x, y, z = line.split()
                        
                # Cambiar aleatoriamente el tipo de elemento según las proporciones dadas
                if random.random() < proporcion_tipo_1:
                    # Cambiar el tipo de elemento a 1
                    atom_type = '1'
                else:
                    # Cambiar el tipo de elemento a 2
                    atom_type = '2'
                        
                # Escribir la línea con el tipo de elemento cambiado en el archivo de salida
                outfile.write(f"{atom_id} \t {atom_type} \t {x} \t {y} \t {z}\n")
            else:
                break  # Salir del bucle si se alcanza el final de la sección 'Atoms'

# Nombre del archivo de entrada y salida
input_file = 'supercell.lmp'
output_file = 'atoms14.lmp'

# Proporción de átomos que tendrán el tipo de elemento 1 (por ejemplo, 0.5 para el 50%)
proporcion_tipo_1 = 0.5

# Llama a la función para cambiar los tipos de elementos
cambiar_tipos_elementos(input_file, output_file, proporcion_tipo_1)