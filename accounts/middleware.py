
# # from .signals import custom_signal


# class LoginRedirectMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Get the user from the request
#         user = request.user

#         # Get the response generated by the view
#         response = self.get_response(request)
#         print(response)
#         # Check if the user is authenticated
#         if user.is_authenticated:
#             try:
#                 # Get the first role associated with the user
#                 role = user.roles.first().role
                
#                 if role == 'admin':
#                     # Add a custom field to the response
#                     user_role = 'Admin'
#                 elif role == 'user':
#                     # Add a custom field to the response
#                     user_role = 'User'
#                 else:
#                     # Add a custom field to the response
#                     user_role = 'Guest'
#             except AttributeError:
#                 # Handle the case where the user has no roles assigned
#                 user_role= 'No roles assigned'
        
#         # custom_signal.send(sender=self.__class__, data=user_role)
        
#         return response
