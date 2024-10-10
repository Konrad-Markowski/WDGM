import numpy as np
from PIL import Image


def rysuj_ramke_w_obrazie(obraz, grub):
    tab_obraz = np.asarray(obraz).astype(np.uint8)
    h, w = tab_obraz.shape

    for i in range(grub):
        tab_obraz[i, :] = 0
        tab_obraz[h - i - 1, :] = 0

    for j in range(grub):
        tab_obraz[:, j] = 0
        tab_obraz[:, w - j - 1] = 0

    tab_obraz_bool = tab_obraz.astype(bool)
    return Image.fromarray(tab_obraz_bool)

obraz = Image.new('1', (100, 150), 1)
print(rysuj_ramke_w_obrazie(obraz,20))
obraz.show()
