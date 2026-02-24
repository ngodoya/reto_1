def palindromo(word: str) -> bool:
    word = word.lower().replace(' ', '')
    begin = 0
    end = len(word) - 1

    while begin < end:
        if word[begin] != word[end]:
            return False
        begin += 1
        end -= 1
    return True
print(palindromo("Dabale arroz a la zorra el abad"))