from pprint import pprint


def beolvas():
    cipok = []
    with open('sneakers.csv') as f:
        next(f)
        for sor in f:
            ertek = sor.strip().split(',')
            sneaker = {
                'title': ertek[0],
                'color': ertek[1],
                'full_price': ertek[2],
                'current_price': ertek[3],
                'publish_date': ertek[4]

            }
            cipok.append(sneaker)
    return cipok


def rendezesi_szempont(sneakers):
    szempontok = ['title', 'color', 'full_price', 'current_price', 'publish_date']
    for sorszam, szempont in enumerate(szempontok, start=1):
        print(f"{sorszam} - {szempont}")
    valasztas = int(input('Válassz, melyik szempont alapján rendezzem a cipőket? ')) - 1
    valasztott_szempont = szempontok[valasztas]
    print(valasztott_szempont)
    pprint(sorted(sneakers, key=lambda cipo: cipo[valasztott_szempont]))


def main():
    sneakers = beolvas()
    rendezesi_szempont(sneakers)


main()
