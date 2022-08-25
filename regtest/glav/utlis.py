from .models import CustomUser


menu = [
    {'link': 'home', 'title': 'Home'},
    {'link': 'home', 'title': 'Home'},
    {'link': 'home', 'title': 'Home'},
    {'link': 'addpost', 'title': 'Add Post'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context.update({
            'menu': menu,
            'logged': self.request.user.is_authenticated,
            'user': self.request.user
        })
        return context