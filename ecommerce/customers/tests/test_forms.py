from django.test import TestCase
from core.models import User
from customers.forms import CustomerRegistrationForm


class CustomerRegistrationFormTest(TestCase):
    def setUp(self) -> None:
        #  users
        self.user1 = User.objects.create_user(email='test1@email.com', phone='09123456789', password='1234')
        self.user2 = User.objects.create_user(email='test2@email.com', phone='09123456780', password='1234')

        self.form1 = CustomerRegistrationForm
        self.data1 = {
            'phone': '09153456789',
            'email': 'test@email.com',
            'gender': '1',
            'password': '1234',
            'confirm_password': '1234'
        }

    def test1_form_valid(self):
        form = self.form1(self.data1)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.clean_phone(), self.data1['phone'])
        self.assertEqual(form.clean_email(), self.data1['email'])

    def test2_form_invalid(self):
        self.data1.pop('phone')
        self.assertFalse(self.form1(self.data1).is_valid())

    def test3_clean_phone_success(self):
        self.data1['phone'] = '09123456789'
        form = self.form1(data=self.data1)
        self.assertEqual(form.errors['phone'], ['User with this phone number already exists!'])
        form.is_valid()
        self.assertRaises(Exception, form.clean_phone)

    def test4_clean_email_success(self):
        self.data1['email'] = 'test2@email.com'
        form = self.form1(data=self.data1)
        self.assertEqual(form.errors['email'], ['Email already exists!'])
        form.is_valid()
        self.assertRaises(Exception, form.clean_email)

    def test5_clean(self):
        self.data1['confirm_password'] = '123'
        form = self.form1(data=self.data1)
        self.assertEqual(form.errors['__all__'], ['passwords does not match!'])

