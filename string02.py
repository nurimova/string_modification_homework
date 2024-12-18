def main(s, k, l, n):
    """
    s, k , l, n string o'zgaruvchilari berilgan. S string matn hisoblanadi. k va l belgi. n bu 
    butun son. k belgini l belgiga almashtiring faqat n tasini:
    Args:
        s(str): String ya'ni matn
        k(str): parametr
        l(str): parametr
        n(int): parametr
    Returns:
        str: answer
    """
    return s.replace('k','l',n)