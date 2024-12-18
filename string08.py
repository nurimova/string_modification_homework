def main(s):
    """
    s  string o'zgaruvchi berilgan. Siz s matnda neshta so'z borligini aniqlang.
    Args:
        s(str): String ya'ni matn
    Returns:
        str: answer
    """
    return s.count(' ')+1
s='python code'
print(main(s))
s='it markaz 103'
print(main(s))