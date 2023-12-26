from django.contrib.auth.mixins import UserPassesTestMixin

class PacienteMixin(UserPassesTestMixin):
    def test_func(self) -> bool | None:
        return self.request.user.groups.filter(name='PACIENTES').exists()