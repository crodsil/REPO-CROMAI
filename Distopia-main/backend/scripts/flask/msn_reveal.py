from PIL import Image
import numpy as np


def revelar_mensagem(imagem):
    imagem_array = np.array(imagem)
    linhas, colunas, canais = imagem_array.shape
    
    mensagem_bin = ''
    for linha in range(linhas):
        for coluna in range(colunas):
            for canal in range(canais):
                pixel_bin = format(imagem_array[linha, coluna, canal], '08b')
                mensagem_bin += pixel_bin[-1]
    
    mensagem_ascii = ''
    for i in range(0, len(mensagem_bin), 8):
        caractere_bin = mensagem_bin[i:i+8]
        caractere_ascii = chr(int(caractere_bin, 2))
        if caractere_ascii == '\0':
            break
        mensagem_ascii += caractere_ascii
    
    return mensagem_ascii