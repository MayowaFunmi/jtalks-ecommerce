import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Avg
from products.models import random_code

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Courses(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    categories = models.ManyToManyField(Category, related_name='courses')
    name = models.CharField(max_length=100)
    overview = models.TextField()
    cover = models.ImageField(blank=True, null=True, upload_to="courses_cover/")
    slug = models.SlugField(unique_for_date='created', max_length=250, null=True, blank=True)

    # Courses content
    content_url = models.URLField(blank=True, null=True)
    content_file = models.FileField(blank=True, null=True)
    tutor = models.CharField(max_length=100, blank=True, null=True)
    tutor_image = models.ImageField(blank=True, null=True, upload_to="course_tutor")
    tutor_title = models.CharField(max_length=100, blank=True, null=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # What you will learn

    class Meta:
        ordering = ('id',)
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name

    def get_avg_rating(self):
        reviews = CourseReview.objects.filter(course=self).aggregate(rating_avg=Avg('review_rating'))
        return reviews['rating_avg']

    def get_avg_rating1(self):
        reviews = CourseReview.objects.filter(course=self)
        print(reviews)
        count = len(reviews)
        sum = 0
        for review in reviews:
            sum += review.review_rating
        return sum/count


class CourseReview(models.Model):
    RATING = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    review_text = models.CharField(max_length=160)
    review_rating = models.CharField(choices=RATING, max_length=150)
    rated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.review_rating} Rated by {self.user.username}'

    def get_review_rating(self):
        return self.review_rating


class UserLibrary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='library')
    courses = models.ManyToManyField(Courses)
    paid = models.BooleanField(default=False)
    reference_id = models.CharField(max_length=200, null=True, blank=True)
    order_id = models.CharField(default=random_code, max_length=10, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    payment_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = "UserLibraries"

    def __str__(self):
        return self.user.username

"""
    def price_display(self):
        return self.price/100

        def get_absolute_url(self):
        return reverse('courses:course_detail', args=[self.id, self.slug])
"""
