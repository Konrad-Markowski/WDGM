import numpy as np
from PIL import Image


def rysuj_ramke_w_obrazie(obraz, grub):
    # Wczytanie tablicy obrazu w typie uint8
    tab_obraz = np.asarray(obraz).astype(np.uint8)
    h, w = tab_obraz.shape

    # Rysowanie czarnej ramki o grubości 'grub'
    for i in range(grub):  # górna i dolna ramka
        tab_obraz[i, :] = 0  # górna ramka
        tab_obraz[h - i - 1, :] = 0  # dolna ramka

    for j in range(grub):  # lewa i prawa ramka
        tab_obraz[:, j] = 0  # lewa ramka
        tab_obraz[:, w - j - 1] = 0  # prawa ramka

    # Zamiana tablicy na typ bool (obrazy czarno-białe)
    tab_obraz_bool = tab_obraz.astype(bool)

    # Tworzenie nowego obrazu z tablicy
    return Image.fromarray(tab_obraz_bool)


def rysuj_ramki(w, h, grub):
    # Tworzenie pustego białego obrazu
    tab = np.ones((h, w), dtype=np.uint8)

    # Dodawanie naprzemiennych czarnych i białych ramek
    for i in range(0, min(w, h) // 2, grub * 2):
        tab[i:h - i, i:i + grub] = 0  # lewa ramka
        tab[i:h - i, w - i - grub:w - i] = 0  # prawa ramka
        tab[i:i + grub, i:w - i] = 0  # górna ramka
        tab[h - i - grub:h - i, i:w - i] = 0  # dolna ramka

    return Image.fromarray(tab.astype(bool))


def rysuj_pasy_pionowe(w, h, grub):
    # Tworzenie pustego obrazu
    tab = np.ones((h, w), dtype=np.uint8)

    # Tworzenie pionowych pasów
    for j in range(0, w, 2 * grub):
        tab[:, j:j + grub] = 0  # Pionowe pasy

    return Image.fromarray(tab.astype(bool))


