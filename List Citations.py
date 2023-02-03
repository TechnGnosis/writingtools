def list_citations(n):
    numbers = [i + 1 for i in range(n)]
    print("\n".join("[{}]".format(num) for num in numbers))

list_citations(30)
