from django.urls import reverse_lazy
from django.views.generic import CreateView
from django import forms

from .forms import UserCreationFormWithEmail


class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self):
        form = super(SignUpView, self).get_form()
        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control mb-2',
                                                                'placeholder': 'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2',
                                                              'placeholder': 'Email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2',
                                                                     'placeholder': 'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2',
                                                                     'placeholder': 'Repite contraseña'})
        return form
