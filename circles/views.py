from django.shortcuts import render, redirect, get_object_or_404
from .models import Circle


def circle_list(request):
    circles = Circle.objects.all()
    return render(request, 'circles/index.html', {'circles': circles})


def create_circle(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        img = request.FILES.get('image')
        Circle.objects.create(owner=request.user, name=name, description=desc, cover_image=img)
        return redirect('circle_list')
    return render(request, 'circles/form2.html', {'title': 'Create Circle'})


def update_circle(request, pk):
    circle = get_object_or_404(Circle, id=pk)
    if request.method == "POST":
        circle.name = request.POST.get('name')
        circle.description = request.POST.get('desc')
        if request.FILES.get('image'):
            circle.cover_image = request.FILES.get('image')
        circle.save()
        return redirect('circle_list')
    return render(request, 'circles/form2.html', {'circle': circle, 'title': 'Update Circle'})


def delete_circle(request, pk):
    circle = get_object_or_404(Circle, id=pk)
    circle.delete()
    return redirect('circle_list')


from .models import Member
from django.contrib.auth.models import User


def add_member(request, circle_id):
    circle = get_object_or_404(Circle, id=circle_id)

    users = User.objects.all()

    if request.method == "POST":
        user_id = request.POST.get('user_id')
        relation = request.POST.get('relationship')

        if user_id:
            member_user = User.objects.get(id=user_id)
            Member.objects.create(circle=circle, user=member_user, relationship=relation)
            return redirect('circle_list')

    return render(request, 'circles/add_member.html', {'circle': circle, 'users': users})
def delete_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    circle_id = member.circle.id
    member.delete()
    return redirect('circle_list')
from .models import TrustedRequest

def send_request(request, circle_id):
    circle = get_object_or_404(Circle, id=circle_id)
    if request.method == "POST":
        email = request.POST.get('email')

        TrustedRequest.objects.create(
            sender=request.user,
            receiver_email=email,
            circle=circle
        )
        return redirect('circle_list')
    return render(request, 'circles/send_request.html', {'circle': circle})