def merge_sort(arr, key=lambda x: x[1]):
    # Si la longitud del arreglo es 0 o 1, ya está ordenado
    if len(arr) <= 1:
        return arr
    
    # Divide el arreglo en dos mitades
    mid = len(arr) // 2
    left = arr[:mid]  # Obtiene la mitad izquierda del arreglo
    right = arr[mid:]  # Obtiene la mitad derecha del arreglo
    
    # Ordena recursivamente las dos mitades
    left = merge_sort(left, key)  # Llama recursivamente merge_sort para ordenar la mitad izquierda
    right = merge_sort(right, key)  # Llama recursivamente merge_sort para ordenar la mitad derecha
    
    # Combina las dos mitades ordenadas
    return merge(left, right, key)  # Combina las mitades ordenadas utilizando el merge

def merge(left, right, key):
    merged = []  # Inicializa la lista donde se almacenará la "fusión"
    left_index = right_index = 0  # Inicia los índices para recorrer las mitades izquierda y derecha
    
    # "Fusiona" las dos mitades ordenadas en una sola lista ordenada
    while left_index < len(left) and right_index < len(right):
        if key(left[left_index]) < key(right[right_index]):  # Comparar usando la clave proporcionada
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Agrega los elementos restantes de la mitad izquierda (si los hay)
    merged += left[left_index:]
    # Agrega los elementos restantes de la mitad derecha (si los hay)
    merged += right[right_index:]
    
    # Retorna la lista fusionada
    return merged

def schedule_trabajos(trabajos):
    # Ordena los trabajos por hora de inicio utilizando merge_sort
    trabajos_ordenados = merge_sort(trabajos, key=lambda x: x[1])
    trabajos_seleccionados = []  # Inicia la lista de trabajos seleccionados
    current_end_time = 0  # Inicia el tiempo de finalización actual
    trabajos_superpuestos = []  # Inicia la lista de trabajos superpuestos

    # Selecciona los trabajos que no se superponen
    for trabajo in trabajos_ordenados:
        nombre, tiempo_inicial, tiempo_final = trabajo
        if tiempo_inicial >= current_end_time:
            trabajos_seleccionados.append(trabajo)
            current_end_time = tiempo_final  # Actualiza el tiempo de finalización actual
        else:
            trabajos_superpuestos.append(trabajo)

    # Avisa si hay trabajos superpuestos
    if trabajos_superpuestos:
        print("¡Atención! Algunos trabajos se superponen:")
        for trabajo in trabajos_superpuestos:
            print(f"Trabajo: {trabajo[0]} que comienza en {trabajo[1]} y acaba en {trabajo[2]}")
    
    # Regresa la lista de trabajos seleccionados y todos los trabajos ordenados
    return trabajos_seleccionados, trabajos_ordenados

def imprimir_trabajos(trabajos):
    i = 1  # Inicializa el contador para numerar los trabajos
    for trabajo in trabajos:
        nombre, ini, fin = trabajo  # Saca el nombre, el tiempo de inicio y el tiempo de fin de cada trabajo
        print(f"{i}.- Trabajo: {nombre}")  # Imprime el número del trabajo y su nombre
        print(f"        Inicio: {ini}")  # Imprime el tiempo de inicio del trabajo
        print(f"        Fin: {fin}")  # Imprime el tiempo de finalización del trabajo
        i += 1  # Incrementa el contador para el siguiente trabajo

def combinaciones(lista):
    resultado = [[]]  # Inicia la lista de combinaciones con una lista vacía
    for elemento in lista:
        nuevas_combinaciones = [comb + [elemento] for comb in resultado]  # Genera nuevas combinaciones agregando el elemento a cada combinación existente
        resultado.extend(nuevas_combinaciones)  # Agrega las nuevas combinaciones al resultado
    return resultado  # Regresa la lista de todas las combinaciones

def combinaciones_de_dos(lista):
    resultado = []  # Inicia la lista de combinaciones de dos elementos
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            resultado.append((lista[i], lista[j]))  # Agrega cada par de elementos a la lista de combinaciones de dos
    return resultado  # Regresa la lista de combinaciones de dos

def se_sobreponen(t1, t2):
    inicio1, fin1 = t1[1], t1[2]  # Extrae el tiempo de inicio y finalización del primer trabajo
    inicio2, fin2 = t2[1], t2[2]  # Extrae el tiempo de inicio y finalización del segundo trabajo
    return not (fin1 <= inicio2 or fin2 <= inicio1)  # Regresa True si los trabajos se sobreponen, False si no

def combinaciones_no_sobrepuestas(trabajos_maximo_tiempo, trabajos):
    no_sobrepuestas = []  # Inicia la lista de combinaciones de trabajos que no se sobreponen
    todas_combinaciones = combinaciones(trabajos_maximo_tiempo)  # Obtiene todas las combinaciones de trabajos con el mayor tiempo de empleo
    for comb in todas_combinaciones:
        if len(comb) > 0 and all(not se_sobreponen(t1, t2) for t1, t2 in combinaciones_de_dos(comb)):  # Verifica si la combinación no tiene trabajos que se sobreponen
            no_sobrepuestas.append(comb)  # Agrega la combinación a la lista de combinaciones que no se sobreponen
    return no_sobrepuestas  # Retorna la lista de combinaciones que no se sobreponen

def main():
    # Solicita al usuario el número de trabajos
    num_trabajos = int(input("Ingresa el número de trabajos: "))
    trabajos = []  # Inicia la lista donde se almacenarán los trabajos
    
    # Solicita al usuario el nombre, la hora de inicio y finalización de cada trabajo
    for i in range(num_trabajos):
        nombre = input(f"Ingrese el nombre del trabajo {i + 1}: ")  # Solicita el nombre del trabajo
        while True:
            tiempo_inicial = int(input(f"Ingrese la hora de inicio del trabajo {i + 1} (0-24): "))  # Solicita la hora de inicio del trabajo
            tiempo_final = int(input(f"Ingrese la hora de finalización del trabajo {i + 1} (0-24): "))  # Solicita la hora de finalización del trabajo
            if 0 <= tiempo_inicial < tiempo_final <= 24:  # Verifica si los tiempos ingresados son válidos
                trabajos.append((nombre, tiempo_inicial, tiempo_final))  # Agrega el trabajo a la lista de trabajos
                break  # Sale del ciclo while si los tiempos son válidos
            else:
                print("Los tiempos introducidos no son válidos. Asegúrese de que la hora de inicio sea menor que la hora de finalización y que ambas estén en el rango de 0 a 24.")  # Muestra un mensaje de error si los tiempos no son válidos

    # Ordena y selecciona los trabajos que no se superponen
    trabajos_seleccionados, trabajos_ordenados = schedule_trabajos(trabajos)
    
    # Imprime todos los trabajos ordenados por hora de inicio
    print("Todos los trabajos organizados por hora de inicio:")
    imprimir_trabajos(trabajos_ordenados)

    # Imprime los trabajos seleccionados que no se superponen
    print("\nLos trabajos que no se superponen quedan organizados de la siguiente manera:")
    imprimir_trabajos(trabajos_seleccionados)

    # Calcula el tiempo de empleo para cada trabajo
    max_tiempo = {trabajo[0]: trabajo[2] - trabajo[1] for trabajo in trabajos}
    
    # Encuentra el mayor tiempo de empleo
    mayor_tiempo = max(max_tiempo.values())
    
    # Filtra los trabajos con el mayor tiempo de empleo
    trabajos_maximo_tiempo = [trabajo for trabajo in trabajos if trabajo[2] - trabajo[1] == mayor_tiempo]

    # Encuentra todas las combinaciones de trabajos con el mayor tiempo de empleo que no se sobreponen
    combinaciones_validas = combinaciones_no_sobrepuestas(trabajos_maximo_tiempo, trabajos)

    # Imprime todas las combinaciones de trabajos con el mayor tiempo de empleo que no se sobreponen
    print("\nTodas las combinaciones de trabajos con el mayor tiempo de empleo que no se sobreponen son:\n")
    print(f"Mayor tiempo de empleo: {mayor_tiempo}\n")
    for combinacion in combinaciones_validas:
        for trabajo in combinacion:
            print(f"Trabajo: {trabajo[0]}, Inicio: {trabajo[1]}, Fin: {trabajo[2]}")
        print("\n")
        
if __name__ == "__main__":
    main()  # Llama a la función main si el archivo se está ejecutando directamente como el programa principal