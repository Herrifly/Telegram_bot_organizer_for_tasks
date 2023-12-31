import os


class DevConfig:
    db_name = os.environ.get('DB_NAME', 'organiser')
    db_user = os.environ.get('DB_USER', 'postgres')
    db_password = os.environ.get('DB_PASSWORD', 'postgres')
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_port = os.environ.get('DB_PORT', 5432)

    @property
    def alchemy_url(self):
        return f'postgresql://{self.db_user}:{self.db_password}@' \
               f'{self.db_host}:{self.db_port}/{self.db_name}'


proj_conf = DevConfig()
