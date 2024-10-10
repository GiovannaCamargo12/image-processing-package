from skimage.transform import resize

def resize_imagem(imagem, proportion):
    assert 0 <= proportion <= 10, "Coloque uma espesificação de 0 a 10"
    height = round(imagem.shape[0] * proportion)
    width = round(imagem.shape[1] * proportion)
    imagem_resized = resize(imagem, (height, width), anti_aliasing=True)
    return imagem_resized
