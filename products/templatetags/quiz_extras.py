from django import template

register = template.Library()

@register.simple_tag
def calculate_question_range(group_num, per_page=20):
    start = (group_num - 1) * per_page + 1
    end = group_num * per_page
    return f"{start} - {end}"