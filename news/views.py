from django.http import HttpResponse,Http404
import datetime as dt 

#views
def welcome(request):
    return HttpResponse("welcome to moringa tribune")

def news_of_day(request):
    date = dt.date.today()
    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)
    html=f'''
       <html>
         <body>
            <h1>{date.day}/{date.month}/{date.year}</h1>
         </body>
       </html>    
    '''
    return HttpResponse(html)

def convert_dates(dates):
    day_number = dt.date.weekday()
    #Functin to convert actual day of the week
    days= ["Monday","Tusday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    day = days[day_number]
    return day

def past_days_news(request,past_date):
    try:
        #Converts date from string to url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
        
    except ValueError:
        #Raise 404 error when valueerror is thrown
        raise Http404()
    day = convert_dates(date)
    html = f'''
        <html>
           <body>
             <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
           </body>
        </html>
    '''
    return HttpResponse(html)



     

