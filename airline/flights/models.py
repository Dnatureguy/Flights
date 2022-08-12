from django.db import models

# Create your models here.


# Models are way of creating a python class that represents data that django store inside of a database.
# So when a model is created, django is going to figure out the SQL syntax to use to a) create that table
#     b) manipulate that table.
#     Each model represents the main table that you want your data stored in.




class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def ___str__(self):
        return f"{self.city} ({self.code})"
    


class Flight(models.Model):   #Creating a python that is a model.
        origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures") #Foreignkey is the way of referencing data from different table.
        destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals") #Cascade is to corresppondling delete values from each table. 
        duration = models.IntegerField()
        
        def __str__(self):   #This is a string function. It provides the objects in a string represention when called.
            return f"{self.id}: {self.origin} to {self.destination}"