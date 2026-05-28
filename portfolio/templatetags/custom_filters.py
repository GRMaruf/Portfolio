from django import template
import math

register = template.Library()

@register.filter
def split(value, key):
    return value.split(key)

@register.filter
def split_lines(value):
    return value.splitlines()

@register.filter
def first_half(value):
    need = math.ceil(len(value)/2)
    return value[:need]

@register.filter
def second_half(value):
    need = math.ceil(len(value)/2)
    return value[need:]

@register.filter
def first_third(value):
    need = math.ceil(len(value)/3)
    return value[:need]

@register.filter
def first_third(value):
    need = math.ceil(len(value)/3)
    return value[:need]

@register.filter
def second_third(value):
    need = math.ceil(len(value)/3)
    return value[need:need*2]

@register.filter
def third_third(value):
    need = math.ceil(len(value)/3)
    return value[need*2:]

@register.filter
def before_colon(value):
    return value.split(":", 1)[0]

@register.filter
def after_colon(value):
    return value.split(":", 1)[1]