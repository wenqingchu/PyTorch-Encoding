from .base import *
from .ade20k import ADE20KSegmentation
from .pascal_voc import VOCSegmentation
from .pascal_aug import VOCAugSegmentation
from .pcontext import ContextSegmentation
from .cityscapes import CityscapesSegmentation
from .coco_stuff import CocostuffSegmentation

datasets = {
    'ade20k': ADE20KSegmentation,
    'pascal_voc': VOCSegmentation,
    'pascal_aug': VOCAugSegmentation,
    'pcontext': ContextSegmentation,
    'cityscapes': CityscapesSegmentation,
    'coco_stuff': CocostuffSegmentation,
}
def get_segmentation_dataset(name, **kwargs):
    return datasets[name.lower()](**kwargs)
