def is_palindrome(num):
    # convertir el num a un texto/string
    texto = str(num)

    # Compararar primer caracter con ultimo caracter, segundo caracter con penultimo caracter, etc.
    # Comparar C0 con Cn-1, C1 con Cn-2, etc.
    for i in range(int(len(texto) / 2)):
      # Al estar comparadno, si se detecta una comparacion que no sean iguales, entonces no es palindrome
      if not texto[i] == texto[len(texto) - 1 - i]:
        return False
    return True
