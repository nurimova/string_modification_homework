def main(s, n):
    """
    s string o'zgaruvchi berilgan.  Natija n ta belgidan iborat bo'ladi. 
    Siz s stringga o'ng qismiga "*" joylashtiradigan dastur qilishingiz kerak. (rjust())
    Args:
        s(str): String ya'ni matn
        n(int): parametr
    Returns:
        str: answer
    """
    return s.rjust(n,"*")