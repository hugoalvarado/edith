import factory


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'users.User'

    username = 'user'
    email = 'hugo-alvarado@example.com'
    full_name = 'Hugo Alvarado'
