from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
import time

def format_duration(duration):
    duration_in_seconds = time.gmtime(duration)
    formatted_duration = time.strftime("%H ч %M мин", duration_in_seconds)
    return formatted_duration

def storage_information_view(request):
    # Программируем здесь

    guards_in_storage = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for guard_in_storage in guards_in_storage:
        duration = format_duration(guard_in_storage.get_duration())
        who_entered = guard_in_storage.passcard.owner_name
        entered = localtime(guard_in_storage.entered_at)
        non_closed_visits.append(
            {
                'who_entered': who_entered,
                'entered_at': entered,
                'duration': duration,
            }
        )

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
