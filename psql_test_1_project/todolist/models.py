from django.db import models


class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=200, null=False, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    last_updated = models.DateTimeField(auto_now=True, null=False, blank=False)

    class Meta:
        db_table = 'Todos'

    def __str__(self):
        return "<Todo: {}>".format(self.text)
