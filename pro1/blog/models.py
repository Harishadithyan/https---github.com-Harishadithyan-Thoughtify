from django.db import models

class Category(models.Model):
    category=models.CharField(max_length=50)

    def __str__(self):
        return self.category
    


class card(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    image=models.URLField()
    des=models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class read(models.Model):
    name = models.ForeignKey(card, on_delete=models.CASCADE)
    para1 = models.TextField()
    img1 = models.URLField()
    para2 = models.TextField()
    img2 = models.URLField()
    para3 = models.TextField()
    img3 = models.URLField()
    para4 = models.TextField()

    def __str__(self):
        return f"Read content for: {self.name.title}"  # Return the title of the related card
