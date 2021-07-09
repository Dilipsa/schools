from django import template

register = template.Library()

#simle Tag
@register.simple_tag
def fun_name(user):
    try:
        application = Application.objects.get(user=request.user)
    except:
        pass
        
    if application:
        # return true
        return request.user