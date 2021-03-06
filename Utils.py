import matplotlib.pyplot as plt
import numpy as np
import torchvision.utils as vutils
import torchvision.transforms as transforms
from skimage.exposure import match_histograms
import torch

# contains utility functions that we need in the main program

# matches the color histogram of original and the super resolution output
def color_histogram_mapping(images, references):
    matched_list = []
    for i in range(len(images)):
        matched = match_histograms(images[i].permute(1, 2, 0).numpy(), references[i].permute(1, 2, 0).numpy(),
                                   channel_axis=-1)
        matched_list.append(matched)
    return torch.tensor(np.array(matched_list)).permute(0, 3, 1, 2)


def visualize_generations(seed, images):
    plt.figure(figsize=(16, 16))
    plt.title(f"Seed: {seed}")
    plt.axis("off")
    plt.imshow(np.transpose(vutils.make_grid(images, padding=2, nrow=5, normalize=True), (2, 1, 0)))
    plt.show()


# denormalize the images for proper display
def denormalize_images(images):
    mean= [0.5, 0.5, 0.5]
    std= [0.5, 0.5, 0.5]
    inv_normalize = transforms.Normalize(
        mean=[-m / s for m, s in zip(mean, std)],
        std=[1 / s for s in std]
    )
    return inv_normalize(images)




