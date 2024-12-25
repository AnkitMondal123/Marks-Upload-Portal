from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class CustomMenuPageView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('account_login')  

    def get_template_names(self):
        if not self.request.user.is_approved:
            return ["pages/menu1.html"]
        else:
            return ["pages/menu2.html"]

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)