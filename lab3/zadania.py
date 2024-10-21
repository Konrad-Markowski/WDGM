from PIL import Image, ImageDraw
import numpy as np


def rysuj_ramki_szare(w, h, grub):
    # Tworzenie obrazu w trybie L
    obraz = Image.new('L', (w, h), 255)
    rysunek = ImageDraw.Draw(obraz)

    # Rysowanie ramek o różnych odcieniach szarości
    odcien = 50
    for i in range(0, min(w, h) // 2, grub):
        rysunek.rectangle([i, i, w - i - 1, h - i - 1], outline=odcien)
        odcien = (odcien + 40) % 256  # Zmieniamy odcień szarości

    return obraz


def rysuj_pasy_pionowe_szare(w, h, grub):
    # Tworzenie obrazu w trybie L
    obraz = Image.new('L', (w, h), 255)
    rysunek = ImageDraw.Draw(obraz)

    # Rysowanie pionowych pasów o różnych odcieniach szarości
    odcien = 50
    for i in range(0, w, grub):
        rysunek.rectangle([i, 0, i + grub - 1, h], fill=odcien)
        odcien = (odcien + 40) % 256  # Zmieniamy odcień szarości

    return obraz


def negatyw(obraz):
    if obraz.mode == '1':
        obraz = obraz.convert('L')
        negatyw = Image.eval(obraz, lambda x: 255 - x).convert('1')
    elif obraz.mode == 'L':
        negatyw = Image.eval(obraz, lambda x: 255 - x)
    elif obraz.mode == 'RGB':
        r, g, b = obraz.split()
        r = Image.eval(r, lambda x: 255 - x)
        g = Image.eval(g, lambda x: 255 - x)
        b = Image.eval(b, lambda x: 255 - x)
        negatyw = Image.merge('RGB', (r, g, b))
    else:
        raise ValueError('Nieobsługiwany tryb obrazu')
    return negatyw

# Testowanie rysuj_ramki_szare
gwiazdka = Image.open('gwiazdka.bmp')
gwiazdka_negatyw = negatyw(gwiazdka)
gwiazdka_negatyw.save('gwiazdka_negatyw.png')

w, h, grub = 300, 200, 5

ramki_szare = rysuj_ramki_szare(w, h, grub)
pasy_szare = rysuj_pasy_pionowe_szare(w, h, grub)

ramki_szare.save('ramki_szare.png')
pasy_szare.save('pasy_szare.png')
