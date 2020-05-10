from django.core.management import BaseCommand
from django.db.models.functions import datetime

from apps.league.models import LeagueUser, Competition, Category, Team, Ranking, Submit, Files


class Command(BaseCommand):
    CATEGORY_NAMES = ['Cryptography', 'AI', 'Blockchain', 'Machine Learning', 'Deep Learning',
                      'Reinforcement Learning', 'Complexity']
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
        'Are you good enough to develop the best efficient programs? You should try one of this competitions!',
    ]

    USERS_NAME = ['latra', 'Oriolac', 'Marta99', 'sergisi', 'quimpm', 'horno', 'Doasy', 'pau1838', 'notaiax']
    GITHUB = 'https://github.com/'
    USERS = {}

    def handle(self, *args, **options):
        admin = LeagueUser.objects.create_superuser(username='admin', password='admin')
        admin.save()
        for name in self.USERS_NAME:
            user = LeagueUser.objects.create(username=name, email=f'{name}@gmail.com',
                                             github_link=f'{self.GITHUB}{name}')
            user.set_password(r'password')
            self.USERS[user.username] = user
            user.save()

        cats = []
        for name, desc in zip(self.CATEGORY_NAMES, self.CATEGORY_DESC):
            cat = Category.objects.create(name=name, description=desc)
            cats.append(cat)
            cat.save()
        comp = Competition.objects.create(title='I Blockchain League',
                                          description='Now it comes the I Blockhain League sponsered by Amazon.',
                                          owner=admin,
                                          data_start_inscription=datetime.datetime(year=2012, month=3, day=19, hour=11,
                                                                                   minute=55, second=00,
                                                                                   microsecond=182371),
                                          data_finish_inscription=datetime.datetime(year=2013, month=4, day=20, hour=11,
                                                                                    minute=12, second=00,
                                                                                    microsecond=182371),
                                          data_start_competition=datetime.datetime(year=2015, month=5, day=10, hour=20,
                                                                                   minute=23, second=00,
                                                                                   microsecond=182371),
                                          data_finish_competition=datetime.datetime(year=2017, month=5, day=31, hour=21,
                                                                                    minute=16, second=00,
                                                                                    microsecond=182371),
                                          )
        comp.categories.add(cats[0])
        comp.categories.add(cats[2])
        comp.save()

        team = Team.objects.create(name='Patatas de Gimeno')
        team.members.add(self.USERS['latra'])
        team.members.add(self.USERS['Oriolac'])
        team.members.add(self.USERS['Marta99'])
        team.members.add(self.USERS['Doasy'])
        team.competition = comp
        team.ranking = Ranking.create(100)
        team.submition = Submit.objects.create(description='Submition of Patatas de Gimeno',
                                               githuburl='https://github.com/Oriolac/codeleague/',
                                               submit_date=datetime.datetime(year=2016, month=5, day=10, hour=20,
                                                                             minute=23, second=00,
                                                                             microsecond=182371), team_id=team.id)
        team.save()

        comp = Competition.objects.create(title='II Blockchain League',
                                          description='Now it comes the II Blockhain League sponsered by Amazon.',
                                          owner=admin,
                                          data_start_inscription=datetime.datetime(year=2017, month=3, day=19, hour=11,
                                                                                   minute=55, second=00,
                                                                                   microsecond=182371),
                                          data_finish_inscription=datetime.datetime(year=2018, month=4, day=20, hour=11,
                                                                                    minute=12, second=00,
                                                                                    microsecond=182371),
                                          data_start_competition=datetime.datetime(year=2019, month=5, day=10, hour=20,
                                                                                   minute=23, second=00,
                                                                                   microsecond=182371),
                                          data_finish_competition=datetime.datetime(year=2022, month=5, day=31, hour=21,
                                                                                    minute=16, second=00,
                                                                                    microsecond=182371),
                                          )
        comp.categories.add(cats[0])
        comp.categories.add(cats[2])
        comp.save()
        comp = Competition.objects.create(title='III Blockchain League',
                                          description='Now it comes the III Blockhain League sponsered by Amazon.',
                                          owner=admin,
                                          data_start_inscription=datetime.datetime(year=2017, month=3, day=19, hour=11,
                                                                                   minute=55, second=00,
                                                                                   microsecond=182371),
                                          data_finish_inscription=datetime.datetime(year=2021, month=4, day=20, hour=11,
                                                                                    minute=12, second=00,
                                                                                    microsecond=182371),
                                          data_start_competition=datetime.datetime(year=2021, month=5, day=10, hour=20,
                                                                                   minute=23, second=00,
                                                                                   microsecond=182371),
                                          data_finish_competition=datetime.datetime(year=2024, month=5, day=31, hour=21,
                                                                                    minute=16, second=00,
                                                                                    microsecond=182371),
                                          )
        comp.categories.add(cats[0])
        comp.categories.add(cats[2])
        comp.save()
        comp = Competition.objects.create(title='I Deep Learning League',
                                          description='LleidaHack has creted the first Deep Learning League. You can join the league before competition starts.',
                                          owner=admin,
                                          data_start_inscription=datetime.datetime(year=2017, month=3, day=19, hour=11,
                                                                                   minute=55, second=00,
                                                                                   microsecond=182371),
                                          data_finish_inscription=datetime.datetime(year=2023, month=4, day=20, hour=11,
                                                                                    minute=12, second=00,
                                                                                    microsecond=182371),
                                          data_start_competition=datetime.datetime(year=2019, month=5, day=10, hour=20,
                                                                                   minute=23, second=00,
                                                                                   microsecond=182371),
                                          data_finish_competition=datetime.datetime(year=2024, month=5, day=31, hour=21,
                                                                                    minute=16, second=00,
                                                                                    microsecond=182371),
                                          )
        comp.categories.add(cats[1])
        comp.categories.add(cats[3])
        comp.categories.add(cats[4])
        comp.categories.add(cats[5])
        comp.save()
        comp = Competition.objects.create(title='I Data Jam',
                                          description='Data Jam is a competition where the teams have to develop programs to solve some high-complex problems. Are you prepared?',
                                          owner=admin,
                                          data_start_inscription=datetime.datetime(year=2016, month=3, day=19, hour=11,
                                                                                   minute=55, second=00,
                                                                                   microsecond=182371),
                                          data_finish_inscription=datetime.datetime(year=2018, month=4, day=20, hour=11,
                                                                                    minute=12, second=00,
                                                                                    microsecond=182371),
                                          data_start_competition=datetime.datetime(year=2018, month=5, day=10, hour=20,
                                                                                   minute=23, second=00,
                                                                                   microsecond=182371),
                                          data_finish_competition=datetime.datetime(year=2029, month=5, day=31, hour=21,
                                                                                    minute=16, second=00,
                                                                                    microsecond=182371),
                                          )
        comp.categories.add(cats[6])
        comp.save()

        comp = Competition.objects.create(title='II Data Jam',
                                          description='Data Jam is a competition where the teams have to develop programs to solve some high-complex problems. Are you prepared?',
                                          owner=admin,
                                          data_start_inscription=datetime.datetime(year=2017, month=3, day=19, hour=11,
                                                                                   minute=55, second=00,
                                                                                   microsecond=182371),
                                          data_finish_inscription=datetime.datetime(year=2023, month=4, day=20, hour=11,
                                                                                    minute=12, second=00,
                                                                                    microsecond=182371),
                                          data_start_competition=datetime.datetime(year=2019, month=5, day=10, hour=20,
                                                                                   minute=23, second=00,
                                                                                   microsecond=182371),
                                          data_finish_competition=datetime.datetime(year=2024, month=5, day=31, hour=21,
                                                                                    minute=16, second=00,
                                                                                    microsecond=182371),
                                          )
        comp.categories.add(cats[6])
        comp.save()
