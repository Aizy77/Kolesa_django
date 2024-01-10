# from django.db import models
# from django.utils import timezone
# from colorfield.fields import ColorField

# class cars(models.Model):
#     name = models.CharField(max_length = 250)
#     generation = models.CharField(max_length = 250)
#     body = models.CharField(max_length = 250)
#     EngCap = models.CharField(max_length = 250)
#     transmission = models.CharField(max_length = 250)
#     drive = models.CharField(max_length = 250)

#     price = models.IntegerField()

#     customs_cleared = models.CharField(max_length = 50)
#     rudder = models.CharField(max_length = 50)
#     # run = models.IntegerField(default = 1, blank = True, null = True)

#     image = models.ImageField(null = True, blank = True, upload_to = "images/")

#     colour = models.CharField(max_length = 250)

#     description = models.TextField(max_length = 2100)

#     city = models.CharField(max_length = 250)
#     number = models.CharField(max_length = 11, null = True)

#     admited = models.DateTimeField(default = timezone.now)

#     class Meta:
#         ordering = ('-admited', )
#     def __str__(self):
#         return self.name
#     def __str__(self):
#         return self.generation
#     def __str__(self):
#         return self.body
#     def __str__(self):
#         return self.EngCap
#     def __str__(self):
#         return self.transmission
#     def __str__(self):
#         return self.drive
#     def __str__(self):
#         return self.price
#     def __str__(self):
#         return self.customs_cleared
#     def __str__(self):
#         return self.rudder
#     # def __str__(self):
#     #     return self.run
#     def __str__(self):
#         return self.image
#     def __str__(self):
#         return self.colour
#     def __str__(self):
#         return self.description
#     def __str__(self):
#         return self.city
#     def __str__(self):
#         return self.number

# # Create your models here.
