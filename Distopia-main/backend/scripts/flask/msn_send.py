from PIL import Image
import numpy as np

def esconder_mensagem(imagem, mensagem):
    mensagem_bin = ''.join(format(ord(i), '08b') for i in mensagem)    
    imagem_array = np.array(imagem)
    tam_max_mensagem = imagem_array.size // 8
    if len(mensagem_bin) > tam_max_mensagem:
        raise ValueError("Au au! A mensagem é maior que a capacidade da imagem")
    
    mensagem_bin += '00000000'
    linhas, colunas, canais = imagem_array.shape
    
    posicao_mensagem = 0
    for linha in range(linhas):
        for coluna in range(colunas):
            for canal in range(canais):
                if posicao_mensagem < len(mensagem_bin):
                    pixel_bin = format(imagem_array[linha, coluna, canal], '08b')
                    novo_pixel_bin = pixel_bin[:-1] + mensagem_bin[posicao_mensagem]
                    imagem_array[linha, coluna, canal] = int(novo_pixel_bin, 2)
                    posicao_mensagem += 1
                else:
                    break
    
    return Image.fromarray(imagem_array)
