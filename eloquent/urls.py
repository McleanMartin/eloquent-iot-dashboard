
from django.urls import path,include
from eloquent_app.admin import server
from strawberry.django.views import AsyncGraphQLView
from eloquent_app.scripts.schema import schema

urlpatterns = [
    path('graphQL/', AsyncGraphQLView.as_view(schema=schema)),
    path('', server.urls),
    
    
]
