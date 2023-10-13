from django.db import models



class Carousel(models.Model):
	image = models.ImageField(upload_to='pics/%y/%m/%d/')
	title = models.CharField(max_length=150)
	sub_title = models.CharField(max_length=100)

	def __str__(self):
		return self.title


# Create your models here.

class AboutUs(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    image = models.ImageField(upload_to='about_us/', verbose_name='Backgroup Image')
    client = models.CharField(max_length = 50)
    client_logo = models.ImageField(upload_to='about_us/', verbose_name='First Image')
    #image2 = models.ImageField(upload_to='about_us/', verbose_name='second Image')

    class Meta:
        verbose_name = 'about us '
        verbose_name_plural = 'about us '

    def __str__(self):
        return self.title



class Team(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    facebook = models.URLField(verbose_name='facebook Link')
    linkedin = models.URLField(verbose_name='linkedin Link')
    skype = models.URLField(verbose_name='skype Link')
    instagram = models.URLField(verbose_name='instagram Link')

    image = models.ImageField(upload_to='chef/')    

    class Meta:
        verbose_name = 'Squad'
        verbose_name_plural = 'Squad'

    def __str__(self):
        return self.name


class Contact(models.Model):
    subject = models.CharField(max_length=50)
    from_email = models.EmailField()
    phone = models.CharField(max_length=9)
    message = models.TextField(verbose_name='Conteúdo')
    image           = models.ImageField(upload_to='contact/', null=True, blank=True)
  
    timestamp = models.DateTimeField(auto_now_add=True)

  


    def __str__(self):
        return self.subject
