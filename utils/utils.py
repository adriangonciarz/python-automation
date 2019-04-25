from faker import Faker

fake = Faker()


def randomize_string(prefix):
    return '{}{}'.format(prefix, fake.uuid4())
