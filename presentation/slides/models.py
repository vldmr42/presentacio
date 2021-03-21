from django.db import models

colors = [
    ('Black', 'Black'),
    ('Red', 'Red'),
    ('Blue', 'Blue')
]

aligns = [
    ('Left', 'Left'),
    ('Center', 'Center'),
    ('Right', 'Right')
]


class Presentations(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Slides(models.Model):
    presentation_id = models.ForeignKey('Presentations', on_delete=models.CASCADE, related_name='slides')
    order_number = models.PositiveSmallIntegerField()
    text = models.CharField(max_length=300)
    align = models.CharField(max_length=10, choices=aligns, default=aligns[0][0])
    color = models.CharField(max_length=10, choices=colors, default=colors[0][0])
    size = models.IntegerField()

    def __str__(self):
        return f'{self.order_number} slide in {self.presentation_id} presentation'
