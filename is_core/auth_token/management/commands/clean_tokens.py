from __future__ import unicode_literals

from datetime import timedelta

from django.utils import timezone
from django.core.management.base import NoArgsCommand

try:
    from django.apps import apps
    get_model = apps.get_model
except ImportError:
    from django.db.models.loading import get_model

from is_core import config
from is_core.auth_token.models import Token, AUTH_USER_MODEL


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        for user in get_model(*AUTH_USER_MODEL.split('.', 1)).objects.all():
            user_last_preserved_token_pks = Token.objects.filter(
                user=user
            ).order_by('-created_at')[:config.AUTH_COUNT_USER_PRESERVED_TOKENS].values_list('pk', flat=True)
            removing_tokens_qs = Token.objects.filter(
                last_access__lt=timezone.now() - timedelta(seconds=config.AUTH_MAX_TOKEN_AGE),
                user=user
            ).exclude(pk__in=user_last_preserved_token_pks)
            self.stdout.write('Removing {} tokens of user {}'.format(removing_tokens_qs.count(), user))
            removing_tokens_qs.delete()
