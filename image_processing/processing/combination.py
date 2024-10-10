import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def find_difference(imagem1, imagem2):
    assert imagem1.shape == imagem2.shape, "Coloque duas imagens com a mesma forma."
    gray_imagem1 = rgb2gray(imagem1)
    gray_imagem2 = rgb2gray(imagem2)
    (score, diferenca_imagem) = structural_similarity(gray_imagem1, gray_imagem2, full=True)
    print("A semelhança das imagens:", score)
    normalizada_diferenca_imagem = (difference_image-np.min(diferenca_image))/(np.max(diferenca_imagem)-np.min(diferenca_imagem))
    return normalizada_diferenca_imagem

def transfer_histogram(imagem1, imagem2):
    coresponde_imagem = match_histograms(imagem1, imagem2, multichannel=True)
    return corresponde_imagem
