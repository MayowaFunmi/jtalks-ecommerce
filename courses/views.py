from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.views import generic, View
from .forms import ReviewAdd
from .models import Category, Courses, CourseReview


# # Create your views here.
# class CourseListView(generic.ListView):
#     template_name = "jtalks/categories.html",
#     template_name = "jtalks/course.html"
#     queryset = Courses.objects.all()

# class CourseDetailView(generic.ListView):
#     template_name = "jtalks/course-inner.html",
#     queryset = Courses.objects.all()


def course_list(request, slug=None):
    category = None
    categories = Category.objects.all()
    courses = Courses.objects.filter(available=True)
    if slug:
        category = get_object_or_404(Category, slug=slug)
        courses = courses.filter(category=category)
    return render(request, 'courses/content/list.html', {'category': category, 'categories': categories, 'courses': courses})


def course_detail(request, id, slug):
    course = get_object_or_404(Courses, id=id, slug=slug, available=True)
    all_reviews = CourseReview.objects.filter(course=course).order_by('-id')[:2]
    total_data = CourseReview.objects.filter(course=course).count()
    reviews = CourseReview.objects.all()
    review_form = ReviewAdd()

    can_add = None
    if request.user.is_authenticated:
        can_add = True
        review_check = CourseReview.objects.filter(user=request.user, course=course).count()
        if review_check > 0:
            can_add = False
    else:
        can_add = False
    context = {
        'course': course,
        'form': review_form,
        'can_add': can_add,
        'all_reviews': all_reviews,
        'total_data': total_data,
        'reviews': reviews
    }
    return render(request, 'courses/content/detail.html', context)


# display list of all courses in each category
def blog_category(request, category):
    courses = Courses.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-date'
    )
    context = {
        "category": category,
        "courses": courses
    }
    return render(request, "forum/category_post_list.html", context)


class SaveReview(View):
    def get(self, request):
        course_id = request.GET.get('id', None)
        review = request.GET.get('review', None)
        rating = request.GET.get('rating', None)

        current_course = Courses.objects.get(id=course_id)
        obj = CourseReview.objects.create(
            user=request.user, course=current_course, review_text=review, review_rating=int(rating)
        )
        user_name = obj.user.first_name + ' ' + obj.user.last_name
        course_name = obj.course.name
        course = {
            'id': obj.id, 'user': user_name, 'course': course_name, 'review_text': obj.review_text,
            'review_rating': obj.review_rating
        }
        data = {
            'course': course
        }
        print(data)

        return JsonResponse(data)


def load_more_review(request):
    offset = int(request.GET['offset'])
    limit = int(request.GET['limit'])
    course_id = int(request.GET['id'])
    course = get_object_or_404(Courses, id=course_id, available=True)
    data = CourseReview.objects.filter(course=course).order_by('-id')[offset:offset+limit]
    t = render_to_string('courses/more_review.html', {'data': data})
    return JsonResponse({'data': t})