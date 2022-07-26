from django.db import models
from PIL import Image
from django.utils.html import mark_safe





# departments=[('Cardiologist','Cardiologist'),
# ('Dermatologists','Dermatologists'),
# ('Emergency Medicine Specialists','Emergency Medicine Specialists'),
# ('Allergists/Immunologists','Allergists/Immunologists'),
# ('Anesthesiologists','Anesthesiologists'),
# ('Colon and Rectal Surgeons','Colon and Rectal Surgeons'),
# ('Pediatricians','Pediatricians'),
# ('Ophthalmologists','Ophthalmologists'),
# ('Endocrinologists','Endocrinologists'),
# ('Gastroenterologists','Gastroenterologists'),
# ('Nephrologists','Nephrologists'),
# ('Urologists','Urologists'),
# ('Pulmonologists','Pulmonologists'),
# ('Otolaryngologists','Otolaryngologists'),
# ('Neurologists','Neurologists'),
# ('Psychiatrists','Psychiatrists'),
# ('Oncologists','Oncologists'),
# ('Radiologists','Radiologists'),
# ('Rheumatologists','Rheumatologists'),
# ('Physiotherapists','Physiotherapists')


# ]

# gender=[
#     ('Male','Male'),
#     ('Female','Female'),
#     ('Transgender','Transgender'),
#     ('N/A','N/A')
# ]


# marital_status=[('Single','Single'),
# ('Married','Married')
# ]




class Doctor(models.Model):
    
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    profile_pic=models.ImageField( upload_to='profile_pics')
    email=models.EmailField(null=True)
    address=models.CharField(max_length=70)
    mobile = models.CharField(max_length=20,null=True)
    marital_status=models.CharField(max_length=20)
    sex=models.CharField(max_length=20)
    department=models.CharField(max_length=50)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.first_name + " " + self.last_name
    
    

    # @property
    

    # def profile_pic_preview(self):
    #     if self.profile_pic:
    #         return mark_safe('<img src="{}" width="300" height="300" />'.format(self.profile_pic.url))
    #     return ""    

    # def __str__(self):
    #     return f"{self.first_name} | {self.department}"    

    # def save(self, *args, **kawrgs):
    #     super().save(*args, **kawrgs)

    #     img = Image.open(self.profile_pic)
       
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.profile_pic.path)

