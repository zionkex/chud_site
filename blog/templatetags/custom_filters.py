
from django import template

register = template.Library()

@register.filter
def truncate_at_last_dot(value, words_limit):
    words = value.split()[:words_limit]
    truncated_text = ' '.join(words)
    last_dot_index = truncated_text.rfind('.')
    
    if last_dot_index != -1:
        truncated_text = truncated_text[:last_dot_index + 1]
    
    return truncated_text
