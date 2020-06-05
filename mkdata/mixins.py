from django.contrib.auth.mixins import UserPassesTestMixin
from .models import AddedWork


class OnlyRegistererMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        work = AddedWork.objects.get(id=self.kwargs['pk'])
        #print(f'work.userid is {work.userid}')
        #print(f'user.id is {user.id}')
        return work.userid == user.id or work.userid == 0
