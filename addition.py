def additionner_nombre(nombre1, nombre2):
    """
    Cette fonction prend deux nombres en entrée et renvoie leur somme.
    
    Args:
    nombre1 (float): Premier nombre.
    nombre2 (float): Deuxième nombre.
    
    Returns:
    float: La somme de nombre1 et nombre2.

    Exception:
    TypeError: Si nombre1 ou nombre2 n'est pas un nombre.
    """
    try:
        return nombre1 + nombre2
    except TypeError:
        raise TypeError("Les entrées doivent être des nombres.")
