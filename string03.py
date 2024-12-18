def main(s, n):
    """
    s string o'zgaruvchi berilgan.  Natija n ta belgidan iborat bo'ladi 
    Siz s string ni markazga joylashtiradigan dastur qilishingiz kerak. Yetmagan belgiga '*' joylashtiring.(center())
    Args:
        s(str): String ya'ni matn
        n(int): parametr
    Returns:
        str: answer
    """
    return s.center(n,'*')