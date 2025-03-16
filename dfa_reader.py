import sys

def read_dfa_from_file():
    """Lee un DFA desde un archivo especificado por el usuario."""
    file = input("Ingrese el nombre del archivo (Escriba la extención '.txt'): ").strip()
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
            if not lines:
                raise ValueError("El archivo está vacío.")
            cases = int(lines[0].strip())
            if cases == 0:
                raise ValueError("No se especificaron casos de DFA.")
            dfas = []
            index = 1
            for _ in range(cases):
                if index >= len(lines):
                    raise ValueError("Formato incorrecto en la cantidad de estados.")
                num_states = int(lines[index].strip())
                index += 1
                
                if index >= len(lines):
                    raise ValueError("Formato incorrecto en el alfabeto.")
                alphabet = lines[index].strip().split()
                index += 1
                
                if index >= len(lines):
                    raise ValueError("Formato incorrecto en los estados finales.")
                final_states = set(map(int, lines[index].strip().split()))
                index += 1
                
                transitions = []
                for _ in range(num_states):
                    if index >= len(lines):
                        raise ValueError("Faltan transiciones en el DFA.")
                    transitions.append(list(map(int, lines[index].strip().split())))
                    index += 1
                
                dfas.append((num_states, alphabet, final_states, transitions))
            return dfas
    except FileNotFoundError:
        print("Error: No se encontró el archivo.")
        return None
    except ValueError as e:
        print(f"Error en el archivo: {e}")
        return None

def leer_entrada():
    """Permite ingresar manualmente un DFA con validaciones de error."""
    while True:
        try:
            c = int(input("Ingrese el número de casos: ").strip())
            if c <= 0:
                raise ValueError("El número de casos debe ser mayor a 0.")
            break
        except ValueError as e:
            print(f"Error: {e}, ingrese un número válido.")

    casos = []

    for i in range(c):
        print(f"\nDFA {i + 1}:")
        while True:
            try:
                n = int(input("Ingrese el número de estados: ").strip())
                if n <= 0:
                    raise ValueError("El número de estados debe ser mayor a 0.")
                break
            except ValueError as e:
                print(f"Error: {e}, ingrese un número válido.")

        while True:
            alfabeto = input("Ingrese el alfabeto (símbolos separados por espacio): ").strip().split()
            if alfabeto:
                break
            print("Error: El alfabeto no puede estar vacío.")

        while True:
            try:
                estados_finales = set(map(int, input("Ingrese los estados finales (separados por espacio): ").strip().split()))
                if any(e < 0 or e >= n for e in estados_finales):
                    raise ValueError("Los estados finales deben estar dentro del rango de estados.")
                break
            except ValueError as e:
                print(f"Error: {e}, ingrese números válidos.")

        transiciones = []
        print("Ingrese la tabla de transiciones (una línea por estado):")
        for j in range(n):
            while True:
                try:
                    transicion = list(map(int, input(f"Estado {j}: ").strip().split()))
                    if len(transicion) != len(alfabeto):
                        raise ValueError(f"Debe haber {len(alfabeto)} transiciones.")
                    if any(e < 0 or e >= n for e in transicion):
                        raise ValueError("Los estados de transición deben estar dentro del rango de estados.")
                    transiciones.append(transicion)
                    break
                except ValueError as e:
                    print(f"Error: {e}, ingrese valores correctos.")

        casos.append((n, alfabeto, estados_finales, transiciones))

    return casos

def encontrar_estados_equivalentes(num_states, final_states, transitions):
    """Aplica el algoritmo para encontrar estados equivalentes en un DFA."""
    table = [[False] * num_states for _ in range(num_states)]
    
    # Marcar pares de estados distinguibles inicialmente
    for i in range(num_states):
        for j in range(i + 1, num_states):
            if (i in final_states) != (j in final_states):
                table[i][j] = True

    # Refinamiento iterativo de la tabla de equivalencia
    changes = True
    while changes:
        changes = False
        for i in range(num_states):
            for j in range(i + 1, num_states):
                if not table[i][j]:
                    for k in range(len(transitions[0])):  # Recorre símbolos del alfabeto
                        t1, t2 = transitions[i][k], transitions[j][k]
                        if t1 != t2 and table[min(t1, t2)][max(t1, t2)]:
                            table[i][j] = True
                            changes = True

    # Extraer los estados equivalentes
    equivalentes = []
    for i in range(num_states):
        for j in range(i + 1, num_states):
            if not table[i][j]:
                equivalentes.append((i, j))

    return equivalentes

def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Ingresar DFA manualmente")
        print("2. Leer DFA desde un archivo")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            dfas = leer_entrada()
        elif opcion == "2":
            dfas = read_dfa_from_file()
            if dfas is None:
                continue  # Si hubo error en la lectura, volver al menú
        elif opcion == "3":
            print("Saliendo del programa.")
            sys.exit(0)
        else:
            print("Opción no válida. Intente de nuevo.")
            continue

        # Procesar DFAs obtenidos
        for dfa_index, (num_states, alphabet, final_states, transitions) in enumerate(dfas, start=1):
            equivalentes = encontrar_estados_equivalentes(num_states, final_states, transitions)
            print(f"\nDFA {dfa_index} - Estados equivalentes:")
            for pair in equivalentes:
                print(f"({pair[0]}, {pair[1]})", end=" ")
            print("\n")

if __name__ == "__main__":
    main()   
