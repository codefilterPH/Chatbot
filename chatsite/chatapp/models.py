from django.db import models


class OpenAIKey(models.Model):
    name = models.CharField(max_length=50, null=True, blank=False, default='API KEY')
    key = models.CharField(max_length=255, null=True, blank=False)
    model = models.CharField(max_length=50, null=True, blank=False, default='text-davinci-003')
    max_tokens = models.SmallIntegerField(default=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "API KEY"
        verbose_name_plural = "API KEY"

