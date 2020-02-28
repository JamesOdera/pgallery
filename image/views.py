from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt
from .models import Article

# Create your views here.
def gallery(request):
    return render(request, 'gallery.html')

def image_today(request):
    date = dt.date.today()
    image = Article.todays_image()
    return render(request, 'images/today-image.html', {"date": date, "image": image})

    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>Image for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_image(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)

    image = Article.days_image(date)
    return render(request, 'images/past-image.html', {"date": date, "image": image})
