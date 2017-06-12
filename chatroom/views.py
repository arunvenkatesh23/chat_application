from django.shortcuts import HttpResponseRedirect, render
from accounts.models import User
from .models import Message
from .forms import MessageForm


def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        first_name = User.objects.all()
        room = Message.objects.filter(user=request.user)
        context = {
            'first_name': first_name,
            'room': room,
        }
        return render(request, 'chatroom/index.html', context)


def send(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        first_name = User.objects.all()
        form = MessageForm(request.POST or None, request.FILES or None)
        if request.method == "POST":
            if form.is_valid():
                user = form.save(commit=False)
                user.user_id = request.user.id
                user.receiver = request.GET.get('r', '')
                user.msg = request.POST['message']
                user.room = request.POST['room']
                if user.msg != '':
                    user.save()
                    message_ids1 = []
                    for message in Message.objects.filter(room=user.room):
                        message_ids1.append(message.pk)
                    user_message1 = Message.objects.filter(pk__in=message_ids1)
                    context = {
                        'form': form,
                        'first_name': first_name,
                        'message': user_message1,
                        'receiver': user.receiver,
                    }
                    return render(request, 'chatroom/index.html', context)
                message_ids1 = []
                for message in Message.objects.filter(room=user.room):
                    message_ids1.append(message.pk)
                user_message1 = Message.objects.filter(pk__in=message_ids1)
                context = {
                    'form': form,
                    'first_name': first_name,
                    'message': user_message1,
                }
                return render(request, 'chatroom/index.html', context)
            context = {
                'form': form,
                'first_name': first_name,
            }
            return render(request, 'chatroom/index.html', context)
        context = {
            'form': form,
            'first_name': first_name,
        }
        return render(request, 'chatroom/index.html', context)
