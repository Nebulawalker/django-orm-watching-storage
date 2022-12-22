from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.format_duration import format_duration


def storage_information_view(request):
    guards_in_storage = Visit.objects.filter(leaved_at__isnull=True)
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
        'non_closed_visits': non_closed_visits,  
    }
    return render(request, 'storage_information.html', context)
