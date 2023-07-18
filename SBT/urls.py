from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("service/", views.service, name="service"),
    path("contact/", views.contact, name="contact"),
    path("faq/", views.faq, name="faq"),
    path("feature/", views.feature, name="feature"),
    path("project/", views.project, name="project"),
    path("team/", views.team, name="team"),
    path("testimonial/", views.testimonial, name="testimonial"),
    path("policy/", views.policy, name="policy"),
    path("career/", views.career, name="career"),
    path("tnc/", views.tnc, name="tnc"),
    path("base/", views.base, name="base"),
    path("chart/", views.chart, name="chart"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("expense/", views.expense, name="expense"),
]