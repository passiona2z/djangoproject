from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm) :
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)     # 지금까지 차이가 없다.


        self.fields['username'].disabled = True