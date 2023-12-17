# from django.contrib.auth import get_user_model
# from django.db.models import Q
#
# User = get_user_model()
#
#
# class EmailOrUserBeckend(ModelBeckend):
#
#     def authenicate(self, request, username=None, password=None, **kwargs):
#         try:
#             user = User.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
#         except Users.DoesNotExist:
#             User.set_password(password)
#         except User.MultipleObjectsReturned:
#             user = Users.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).first()
#
#         if user.check_pssword(password) and self.user_can_authenicate(user):
#             return user
#
