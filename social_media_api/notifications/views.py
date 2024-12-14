from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

@login_required
def get_notifications(request):
    notifications = request.user.notifications.all()
    unread_notifications = notifications.filter(read=False)

    context = {
        'unread_notifications': unread_notifications,
        'all_notifications': notifications,
    }
    return render(request, 'notifications/notifications.html', context)

@login_required
def mark_notification_as_read(request, pk):
    notification = get_object_or_404(Notification, pk=pk, recipient=request.user)
    notification.mark_as_read()
    return JsonResponse({'status': 'marked as read'})

