from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """
        Test creating a new user with an email is successful
        :return:
        """
        email = "test@email.com"
        password = "pwd@123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = "test@EMAIL.COM"
        user = get_user_model().objects.create_user(email, "test@123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "Test@123")

    def test_create_new_superuser(self):
        super_user = get_user_model().objects.create_superuser(
            "superusertest@email.com",
            "test@2314"
        )
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
