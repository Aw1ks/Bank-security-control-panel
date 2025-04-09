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