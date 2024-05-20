from django.test import TestCase, Client
from django.urls import reverse
from AccountTransfer.models import Accounts
from decimal import Decimal
from django.contrib.messages import get_messages


class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.transfer_url = reverse('transfer')

        self.from_user = Accounts.objects.create(
            user_id="adafd556",
            name="ali",
            balance=Decimal('10000.00'),
        )
        self.to_user = Accounts.objects.create(
            user_id="bcdef5658",
            name="noor",
            balance=Decimal('200.00'),
        )

    def test_accounts_list_GET(self):

        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')

    def test_accounts_update_Update(self):

        response = self.client.get(self.transfer_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'update.html')

    def test_transfer_view_POST_valid(self):
        form_data = {
            'from_user': self.from_user.user_id,
            'to_user': self.to_user.user_id,
            'amount': '1000',
        }

        response = self.client.post(self.transfer_url, data=form_data)
        # referesh database
        self.from_user.refresh_from_db()
        self.to_user.refresh_from_db()

        self.assertEquals(self.from_user.balance, Decimal('9000'))
        self.assertEquals(self.to_user.balance, Decimal('1200'))

        self.assertRedirects(response, self.transfer_url)

    def test_transfer_view_POST_insufficient_balance(self):
        form_data = {
            'from_user': self.from_user.user_id,
            'to_user': self.to_user.user_id,
            'amount': '11000'
        }
        response = self.client.post(self.transfer_url, data=form_data)

        self.from_user.refresh_from_db()
        self.to_user.refresh_from_db()

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update.html')
        self.assertContains(response, 'Insufficient balance!')

    def test_transfer_view_POST_same_user(self):
        form_data = {
            'from_user': self.from_user.user_id,
            'to_user': self.from_user.user_id,
            'amount': '1000'
        }
        response = self.client.post(self.transfer_url, data=form_data)
        self.from_user.refresh_from_db()
        self.to_user.refresh_from_db()

        self.assertEquals(self.from_user.balance, Decimal('10000'))

        self.assertEquals(self.to_user.balance, Decimal('200.00'))
        errors = response.context['form'].errors
        self.assertIn('to_user', errors)
        self.assertIn(
            'You cannot transfer amount to the same user', errors['to_user'])
