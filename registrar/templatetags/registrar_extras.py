from django import template

register = template.Library()

@register.filter(name='get_first')
def get_first(value):
    '''Returns the first name from the given name
    '''
    return value.split(' ')[0]
