def main(s, n):
    """
    s string o'zgaruvchi berilgan.  Natija n ta belgidan iborat bo'ladi. 
    Siz s stringga chap qismiga "*" joylashtiradigan dastur qilishingiz kerak. (ljust())
    Args:
        s(str): String ya'ni matn
        n(int): parametr
    Returns:
        str: answer
    """
    return s.ljust(n,'*')