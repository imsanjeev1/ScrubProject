from django import template

register = template.Library()

@register.filter(name="cut")
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, "")

@register.filter
def data_split(data_list):
    return data_list[:4]

@register.filter
def index(indexable, i):
    return indexable[i]


@register.filter
def split(splitable, split_at):
    # split with max limit
    if len(split_at.split("||||")) == 2:
        return splitable.split(split_at.split("||||")[0], int(split_at.split("||||")[1]))

    # normal split without max limitation
    return splitable.split(split_at)