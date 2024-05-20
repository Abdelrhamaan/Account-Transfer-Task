from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.contrib import messages
from django.db import transaction
from .models import Accounts
from .forms import TransferForm


class ListAccounts(ListView):
    """View to list all accounts with pagination."""
    model = Accounts
    template_name = 'list.html'
    context_object_name = 'data'
    paginate_by = 24


class TransferView(FormView):
    """View to handle money transfers between accounts."""
    template_name = 'update.html'
    form_class = TransferForm
    success_url = '/update/'

    def form_valid(self, form):
        """Handle the transaction if the form is valid."""
        if self.handle_transaction(form):
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def handle_transaction(self, form):
        """Perform the transfer operation within a transaction."""
        from_user = form.cleaned_data['from_user']
        to_user = form.cleaned_data['to_user']
        amount = form.cleaned_data['amount']
        try:
            with transaction.atomic():
                if from_user.balance >= amount:
                    from_user.balance -= amount
                    to_user.balance += amount
                    from_user.save()
                    to_user.save()
                    transaction.on_commit(lambda: messages.success(
                        self.request, f'Transfer successful from {from_user.name} to {to_user.name} and the amount was {amount}'))
                    self.save_form_data_to_context(from_user, to_user, amount)
                    return True
                else:
                    messages.error(
                        self.request, f'Insufficient balance {from_user.name} doesn\'t have this value {amount}!', extra_tags='danger')
                    self.save_form_data_to_context(from_user, to_user, amount)
                    return False
        except TransferExceptionError:
            messages.error(
                self.request, 'Transfer Failed due to something wrong!', extra_tags='danger')
            self.save_form_data_to_context(from_user, to_user, amount)
            return False

    def save_form_data_to_context(self, from_user, to_user, amount):
        """Save form data to context to display it back in the form."""
        self.extra_context = {
            'from_user': from_user,
            'to_user': to_user,
            'amount': amount
        }

    def get_context_data(self, **kwargs):
        """Add any extra context data saved during the transaction handling."""
        context = super().get_context_data(**kwargs)
        if hasattr(self, 'extra_context'):
            if self.extra_context:
                context.update(self.extra_context)
        return context


class TransferExceptionError(Exception):
    """Custom exception for transfer errors."""
    pass
