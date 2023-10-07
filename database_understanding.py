from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()


		#Terminal Commands
		$python3 manage.py shell
		>>> from book_outlet.models import Book

		#Inserting Data in database
		>>> harry_potter = Book(title="Harry Potter 1-The Philosopher's Stone", rating=5)
		>>> harry_potter.save() 
		>>> lord_of_the_rings = Book(title="Lord of the Rings", rating=4)
		>>> lord_of_the_rings.save()

		#Getting Data From DataBase
		>>> Book.objects.all()
		<QuerySet [<Book: Book object (1)>, <Book: Book object (2)>]> # this is not showing useful data . So lets Modify modal

#-------------------Adding __str__ function for return type---------------------------->

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    
    def __str__(self):
    	return f"{self.title} ({self.rating})"
    	
    	
    	#Terminal Commands
    	>>> Book.objects.all()
	<QuerySet [<Book: Harry Potter 1-The Philosopher's Stone (5)>, <Book: Lord of the Rings (4)>]>
	

#--------------------------------------Updating Models and Migrations-------------------->

#Updating Modals 
from django.core.validators import  MinValueValidator , MaxValueValidator


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False )
    
    def __str__(self):
    	return f"{self.title} ({self.rating})"
    	

		#Terminal Commands
		>>> from book_outlet.models import Book
		>>> Book.object.all()[1]
		>>> Book.objects.all()[1]
		<Book: Lord of the Rings (4)>
		
		>>> Book.objects.all()[0]
		<Book: Harry Potter 1-The Philosopher's Stone (5)>
		
		>>> Book.objects.all()[0].is_bestselling
		False
		
		>>> Book.objects.all()[0].rating
		5
		
		>>> Book.objects.all()[0].title
		"Harry Potter 1-The Philosopher's Stone"
		

#---------------Updating Data in database ----------------------------------------------------->

		#terminal Commands
		>>> a = Book.objects.all()[0]
		>>> a.title
		"Harry Potter 1-The Philosopher's Stone"
		
		>>> lotr = Book.objects.all()[1]
		>>> lotr.title
		'Lord of the Rings'
		
		
		>>> a.author = "J.K Rowling"  #after modification of table we are keeping author name ----Updation
		>>> a.is_bestselling = True 
		>>> a.save()

		>>> Book.objects.all().author
		Traceback (most recent call last):
		  File "<console>", line 1, in <module>
		AttributeError: 'QuerySet' object has no attribute 'author'
		>>> Book.objects.all()[0].author
		'J.K Rowling'
		
		
		>>> lotr.author = "Champak Lal"
		>>> lotr.is_bestselling = True
		>>> lotr.save()


		>>> Book.objects.all()[1].author
		'Champak Lal'
		>>> Book.objects.all()[1].title
		'Lord of the Rings'
		
	
#-----------------Deleting Data In database-------------------------------------------------------------->

		#Lets say we want to delete harry potter
		>>> a = Book.objects.all()[0]  #instantiation
		>>> a.delete()
		(1, {'book_outlet.Book': 1}) #Deleted Receipt Haha
		
		>>> Book.objects.all()
		<QuerySet [<Book: Lord of the Rings (4)>]> #Only this object left
		
	
	
#---------------------Use of create() Function instead of instantiation with key, value pair 
#and  calling save() method to hit the data base------------------
#---Unlike .save() method create() method instantly hits the data base and gets executed------------------>



		#Terminal Commands
		>>> Book.objects.create(title="Harry Potter 1", rating=5, author="J.K Rowling", is_bestselling=True)
		<Book: Harry Potter 1 (5)>
		
		>>> Book.objects.all()
		<QuerySet [<Book: Lord of the Rings (4)>, <Book: Harry Potter 1 (5)>]>
		
		>>> Book.objects.create(title="My Story", rating=2, author="Chandra Mohan", is_bestselling=True)
		<Book: My Story (2)>
		
		>>> Book.objects.create(title="Some Random Book", rating=1, author="Random Dude", is_bestselling=False)
		<Book: Some Random Book (1)>
		
		>>> Book.objects.all()
		<QuerySet [<Book: Lord of the Rings (4)>, <Book: Harry Potter 1 (5)>, <Book: My Story (2)>, <Book: Some Random Book (1)>]>


#----------------------------Quering and Filtering Data ------------------------------------------------>

#get() method to fetch single data item uniquely
#filter() method to fetch multiple data with comman feature
# understanding __lt , __lte , __icontains .......



		#--------------------get()-------------------------->
		>>> Book.objects.get(title="My Story")
		<Book: My Story (2)>
		
		>>> Book.objects.get(rating=5)
		<Book: Harry Potter 1 (5)>
		
		>>> Book.objects.all()
		<QuerySet [<Book: Lord of the Rings (4)>, <Book: Harry Potter 1 (5)>, <Book: My Story (2)>, <Book: Some Random Book (1)>]>
		
		>>> Book.objects.get(is_bestselling=True) #Multiple Objects Returned .So showing error
		Traceback (most recent call last):
		  File "<console>", line 1, in <module>
		  File "/home/cms/Videos/Research Analysis/Python Django The Practical Guide/understandingBackend/venv/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method
		    return getattr(self.get_queryset(), name)(*args, **kwargs)
		  File "/home/cms/Videos/Research Analysis/Python Django The Practical Guide/understandingBackend/venv/lib/python3.10/site-packages/django/db/models/query.py", line 640, in get
		    raise self.model.MultipleObjectsReturned(
		book_outlet.models.Book.MultipleObjectsReturned: get() returned more than one Book -- it returned 3!
		
		
		#-----------filter()-------------------------------------->
		>>> Book.objects.filter(is_bestselling=True)
		<QuerySet [<Book: Lord of the Rings (4)>, <Book: Harry Potter 1 (5)>, <Book: My Story (2)>]>
		
		>>> Book.objects.filter(is_bestselling=False)
		<QuerySet [<Book: Some Random Book (1)>]>
		
		>>> Book.objects.filter(rating=2, is_bestselling=False)
		<QuerySet []>
		
		>>> Book.objects.filter(rating<2)  #We cannot use like this 
		Traceback (most recent call last):
		  File "<console>", line 1, in <module>
		NameError: name 'rating' is not defined
		
		>>> Book.objects.filter(rating__lte=3)
		<QuerySet [<Book: My Story (2)>, <Book: Some Random Book (1)>]>
		
		>>> Book.objects.filter(rating__lt=3)
		<QuerySet [<Book: My Story (2)>, <Book: Some Random Book (1)>]>
		
		>>> Book.objects.filter(rating__lt=3, title__icontains="story")
		<QuerySet [<Book: My Story (2)>]>
		>>> 



#OR condition .... Query Performance (understanding caching) ---------------->





