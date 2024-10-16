import matplotlib.pyplot as plt

def plot_imagem(imagem):
    plt.figure(figsize=(12, 4))
    plt.imshow(imagem, cmap='gray')
    plt.axis('off')
    plt.show()

def plot_result(*args):
    number_imagems = len(args)
    fig, axis = plt.subplots(nrows=1, ncols = number_imagems, figsize=(12, 4))
    names_lst = ['Imagem {}'.format(i) for i in range(1, number_imagems)]
    names_lst.append('Result')
    for ax, name, imagem in zip(axis, names_lst, args):
        ax.set_title(name)
        ax.imshow(imagem, cmap='gray')
        ax.axis('off')
    fig.tight_layout()
    plt.show()

def plot_histogram(imagem):
    fig, axis = plt.subplots(nrows=1, ncols = 3, figsize=(12, 4), sharex=True, sharey=True)
    color_lst = ['red', 'green', 'blue']
    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        ax.set_title('{} histogram'.format(color.title()))
        ax.hist(imagem[:, :, index].ravel(), bins = 256, color = color, alpha = 0.8)
    fig.tight_layout()
    plt.show()
