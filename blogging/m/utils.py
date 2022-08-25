menu = []

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context.update({
            'menu': menu,
        })
        return context