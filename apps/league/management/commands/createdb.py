from django.core.management import BaseCommand

from apps.league.models import LeagueUser, Competition, Category, Team, Ranking


class Command(BaseCommand):
    CATEGORY_NAMES = ['Cryptography', 'AI', 'Blockchain', 'Machine Learning', 'Deep Learning',
                      'Reinforcement Learning']
    CATEGORY_DESC = [
        'Cryptography or cryptology is the practice and study of techniques for secure communication in the presence '
        'of third parties called adversaries.',
        'Artificial Intelligence is intelligence demonstrated by machines, in contrast to the natural intelligence '
        'displayed by humans and animals.',
        'Blockchain is a growing list of records, called blocks, that are linked using cryptography. Each block '
        'contains a cryptographic hash of the previous block, a timestamp, and transaction data.',
        'ML  is the study of computer algorithms that improve automatically through experience. It is seen as a '
        'subset of artificial intelligence.Machine learning algorithms build a mathematical model based on sample '
        'data, known as "training data", in order to make predictions or decisions without being explicitly '
        'programmed to do so.',
        'Deep Learning is part of a broader family of machine learning methods based on artificial neural networks '
        'with representation learning. Learning can be supervised, semi-supervised or unsupervised.',
        'Reinforcement Learning is an area of machine learning concerned with how software agents ought to take '
        'actions in an environment in order to maximize the notion of cumulative reward. Reinforcement learning is '
        'one of three basic machine learning paradigms, alongside supervised learning and unsupervised learning.',
    ]

    USERS_NAME = ['latra', 'Oriolac', 'Marta99']
    GITHUB = 'https://github.com/'

    def handle(self, *args, **options):
        admin = LeagueUser.objects.create_superuser(username='admin', password='admin')
        admin.save()
        for name in self.USERS_NAME:
            user = LeagueUser.objects.create(username=name, email=f'{name}@gmail.com',
                                             github_link=f'{self.GITHUB}{name}')
            user.set_password(r'password')
            user.save()

        cats = []
        for name, desc in zip(self.CATEGORY_NAMES, self.CATEGORY_DESC):
            cat = Category.objects.create(name=name, description=desc)
            cats.append(cat)
            cat.save()
        comp = Competition.objects.create(title='I Blockchain League',
                                          description='Now it comes the I Blockhain League sponsered by Amazon.',
                                          owner=admin,
                                          )
        comp.categories.add(cats[0])
        comp.categories.add(cats[2])
        comp.save()
