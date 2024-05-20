from django.test import SimpleTestCase
from django.urls import resolve, reverse
from AccountTransfer.views import ListAccounts, TransferView


class TestUrls(SimpleTestCase):

    def test_url_list_is_resolved(self):
        url = reverse('list')
        self.assertEquals(resolve(url).func.view_class, ListAccounts)

    def test_url_transfer_is_resolved(self):
        url = reverse('transfer')
        self.assertEquals(resolve(url).func.view_class, TransferView)
