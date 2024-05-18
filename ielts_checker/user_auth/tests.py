from django.test import TestCase
import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import RegisterForm, LoginForm

@pytest.fixture
def client():
    from django.test import Client
    return Client()

@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser', password='testpassword')

@pytest.fixture
def profile(user):
    return UserProfile.objects.create(user=user, profile_pic='profile_pics/default.png')

def test_user_register(client):
    response = client.post(reverse('user-register'), data={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password1': 'testpassword',
        'password2': 'testpassword'
    })
    assert response.status_code == 302
    assert User.objects.filter(username='testuser').exists()

def test_user_login(client, user):
    response = client.post(reverse('user-login'), data={
        'username': 'testuser',
        'password': 'testpassword'
    })
    assert response.status_code == 302
    assert '_auth_user_id' in client.session

def test_user_logout(client, user):
    client.force_login(user)
    response = client.get(reverse('user-logout'))
    assert response.status_code == 302
    assert '_auth_user_id' not in client.session

def test_profile(client, user, profile):
    response = client.get(reverse('profile'))
    assert response.status_code == 302  # Redirect to login page

    client.force_login(user)
    response = client.get(reverse('profile'))
    assert response.status_code == 200
    assert b'Profile' in response.content

def test_profile_form(client, user):
    client.force_login(user)
    response = client.post(reverse('profile'), data={
        'username': 'newusername',
        'email': 'newemail@example.com',
        'first_name': 'New',
        'last_name': 'User',
        'location': 'New York',
        'phone_number': '1234567890',
        'birth_date': '2000-01-01',
    })
    assert response.status_code == 302
    user.refresh_from_db()
    assert user.username == 'newusername'
    assert user.email == 'newemail@example.com'
    assert user.first_name == 'New'
    assert user.last_name == 'User'
    profile = user.userprofile
    assert profile.location == 'New York'
    assert profile.phone_number == '1234567890'
    assert str(profile.birth_date) == '2000-01-01'

def test_profile_invalid_user_id(client, user):
    client.force_login(user)
    response = client.get(reverse('profile') + '?user_id=999')
    assert response.status_code == 404
