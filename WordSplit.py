class WordSplit:
    @classmethod
    def __init__(ctx, first, *args):
        ctx.length = None
        ctx.counter = 0
        ctx.words = list()
        ctx.create(first, *args)
    @classmethod
    def create(ctx, first, *args):
        ctx.origin = first
        for i in args:
            ctx.length = len(i)
            for z in first:
                for u in i:
                    if ctx.counter == ctx.length:
                        ctx.counter = 0
                        ctx.words.append(i)
                    elif z == u:
                        ctx.counter += 1
                        continue
        return ctx.checkduplicate()
    @classmethod
    def checkduplicate(ctx):
        ctx.counter = 0
        for r in ctx.words:
            for z in ctx.words:
                if r == z:
                    ctx.counter += 1
                else:
                    continue
            ctx.counter -= 1
            if not ctx.counter == 0:
                for i in range(ctx.counter):
                    ctx.words.remove(r)
                ctx.counter = 0
        return ctx.display()
    @classmethod
    def display(ctx):
        ctx.counter = 1        
        print("The word", ctx.origin, "contains the following words: ")
        for a in ctx.words:
            print("{}. word is {}." .format(ctx.counter, a))
            ctx.counter += 1

wordsplit = WordSplit("Pseudopseudohypoparathyroidism", "rath", "popa", "pseuodo", "popara", "m", "m", "m", "pop", "popa")


'''
def wordsplit(first, *args):
    uzunluk = None
    sayac = 0
    kelimeler = list()

    for i in args:
        uzunluk = len(i)
        for z in first:
            for u in i:
                if sayac == uzunluk:
                    sayac = 0
                    kelimeler.append(i)
                elif z == u:
                    sayac += 1
                    continue
    sayac = 0
    for r in kelimeler:
        for z in kelimeler:
            if r == z:
                sayac += 1
            else:
                continue
        sayac -= 1
        if not sayac == 0:
            for i in range(sayac):
                kelimeler.remove(r)
            sayac = 0    

    sayac = 1        
    print(first, "kelimesinde ayriyeten şu kelimeler bulunmaktadır: ")
    for a in kelimeler:
        print("{}. kelimemiz {}." .format(sayac, a))
        sayac += 1'''