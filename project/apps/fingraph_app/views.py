from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Person, Follows
from django.db.models import Exists, OuterRef

# Create your views here.

def user_list_view(request):
    current_user = None
    try:
        current_user = Person.objects.get(id=1)
    except Person.DoesNotExist:
        current_user = Person.objects.first()

    if not current_user:
        # No users in the database at all
        return render(request, 'fingraph_app/user_list.html', {'users_data': [], 'current_user': None})

    all_users = Person.objects.all()
    
    users_data = []
    for person in all_users:
        is_following = Follows.objects.filter(follower=current_user, followed_person=person).exists()
        users_data.append({
            'person': person,
            'is_following': is_following
        })
        
    return render(request, 'fingraph_app/user_list.html', {'users_data': users_data, 'current_user': current_user})

def follow_view(request, user_to_follow_id):
    current_user = None
    try:
        current_user = Person.objects.get(id=1)
    except Person.DoesNotExist:
        current_user = Person.objects.first()

    if not current_user:
        # Should not happen if there's any user to follow
        return redirect(reverse('fingraph_app:user_list'))

    user_to_follow = get_object_or_404(Person, id=user_to_follow_id)

    if current_user == user_to_follow:
        # User cannot follow themselves
        return redirect(reverse('fingraph_app:user_list'))

    Follows.objects.get_or_create(follower=current_user, followed_person=user_to_follow)
    
    return redirect(reverse('fingraph_app:user_list'))

def unfollow_view(request, user_to_unfollow_id):
    current_user = None
    try:
        current_user = Person.objects.get(id=1)
    except Person.DoesNotExist:
        current_user = Person.objects.first()

    if not current_user:
         # Should not happen if there's any user to unfollow
        return redirect(reverse('fingraph_app:user_list'))

    user_to_unfollow = get_object_or_404(Person, id=user_to_unfollow_id)

    Follows.objects.filter(follower=current_user, followed_person=user_to_unfollow).delete()
    
    return redirect(reverse('fingraph_app:user_list'))
