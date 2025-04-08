from functools import total_ordering
from datacenter.models import Passcard, Visit
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

def calculate_visit_duration(visit):
    entered_at = timezone.localtime(visit.entered_at)
    leaved_at = timezone.localtime(visit.leaved_at) if visit.leaved_at else timezone.now()
    duration = leaved_at - entered_at
    return duration


def is_visit_long(visit, minutes):
    number_seconds_minute = 60

    duration = calculate_visit_duration(visit)
    return duration.total_seconds() >= minutes * number_seconds_minute


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for visit in visits:
        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': calculate_visit_duration(visit),
            'is_strange': is_visit_long(visit, minutes=60)
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits,
    }
    return render(request, 'passcard_info.html', context)
