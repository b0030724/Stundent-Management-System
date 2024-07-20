from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, class_name):
    """
    Add a CSS class to form fields.
    Usage: {{ form.field|add_class:"css-class" }}
    """
    return value.as_widget(attrs={'class': class_name})
