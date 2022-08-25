from .models import *

links = Category.objects.filter(pk__in = [1,2,3])

class DataMixin:
    paginate_by = 16
    
    def get_user_context(self, **kwargs):
        context = kwargs
        context.update({
            'links': links,
            'cat_selected': context['cat_selected'] if 'cat_selected' in context else 0,
            'user': self.request.user
        })
        return context