from django.db import models
from wagtail.search import index
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
# Create your models here.



class BlogIndexPage(Page):
    pass




class BlogPage(Page):
    date = models.DateField("Post date") #
    short_description = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_field = Page.search_fields + [
        index.SearchField('short_description'),
    index.SearchField('body')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('short_description'),
        FieldPanel('body',classname="full")
    ]