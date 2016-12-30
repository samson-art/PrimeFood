from django.template.defaulttags import register


@register.filter(name='get_item')
def get_item(dict, key):
    # output of this is a list of tuples [('A', 'value1'), ('B', 'value2')]
    return dict.get(key)
