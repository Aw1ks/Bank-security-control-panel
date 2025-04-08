import django
from django.utils import duration 

from datacenter.models import Visit
from django.shortcuts import render
from datacenter.passcard_info_view import calculate_visit_duration, is_visit_long


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at=None)

    number_hours_day = 24
    number_seconds_hour = 3600
    number_seconds_minute = 60

    non_closed_visits = []
    
    for visit in active_visits:
        duration = calculate_visit_duration(visit)

        hours = duration.days * number_hours_day + duration.seconds // number_seconds_hour
        minutes = (duration.seconds % number_seconds_hour) // number_seconds_minute
        seconds = duration.seconds % number_seconds_minute

        formatted_duration= f"{hours:02}ч:{minutes:02}м:{seconds:02}с"
        
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': visit.entered_at,
                'duration': formatted_duration,
                'is_strange': is_visit_long(visit, minutes=60)
            }
        )

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)