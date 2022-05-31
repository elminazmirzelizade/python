animals = input('Heyvanlari girin: ').split(', ')
prices = { 'inek': 500, 'toyuq': 50, 'qoyun': 120, 'at': 900, 'keci': 210 }


try:
    if not 3<len(animals)<10:
        raise ValueError('3-den cox ve 10-dan az sayda heyvan yazmalisiniz')
    print('Umumi qiymet:', sum(map(lambda animal: prices[animal], animals)))
except KeyError:
    print('Heyvanin adini sehv girmisiniz. Sehviniz:')
except ValueError:
    print('3-den cox ve 10-dan az sayda heyvan yazmalisiniz')
except Exception:
    print('Bir xeta bas verdi')
