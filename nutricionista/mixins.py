from django.contrib.auth.mixins import UserPassesTestMixin

class NutricionistaMixin(UserPassesTestMixin):
    def test_func(self) -> bool | None:
        return self.request.user.groups.filter(name='NUTRICIONISTA').exists()