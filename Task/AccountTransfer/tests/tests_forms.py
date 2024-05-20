from django.test import TestCase
from AccountTransfer.forms import TransferForm
from AccountTransfer.models import Accounts


class TestForm(TestCase):

    def setUp(self):
        self.from_user = Accounts.objects.create(
            user_id="acedrg45s",
            name="Jeremy Pennington", balance=5000)
        self.to_user = Accounts.objects.create(
            user_id="fasdfsdfds",
            name="Joseph Price", balance=300)

    def test_form_valid_data(self):
        form_data = {
            'from_user': self.from_user.user_id,
            'to_user': self.to_user.user_id,
            'amount': 100
        }
        form = TransferForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_send_same_user(self):
        form_data = {
            'from_user': self.from_user.user_id,
            'to_user': self.from_user.user_id,
            'amount': 100
        }
        form = TransferForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_send_negative_amount(self):
        form_data = {
            'from_user': self.from_user.user_id,
            'to_user': self.from_user.user_id,
            'amount': -100
        }
        form = TransferForm(data=form_data)
        self.assertFalse(form.is_valid())
