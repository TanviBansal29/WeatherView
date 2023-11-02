import yaml

class Config:

    @classmethod
    def load_print_statements(cls):
        with open('config\\print_statements.yml','r') as f:
            data = yaml.safe_load(f)
            cls.WELCOME_MESSAGE = data['WELCOME_MESSAGE']
            cls.ENTER_USERNAME = data['ENTER_USERNAME']
            cls.ENTER_PASSWORD = data['ENTER_PASSWORD']
            cls.ENTER_CITY = data['ENTER_CITY']
            cls.ENTER_ZIPCODE = data['ENTER_ZIPCODE']
            cls.DATABASE_NAME = data['DATABASE_NAME']
            cls.LOGIN_ADMIN = data['LOGIN_ADMIN']
            cls.INVALID_INPUT = data['INVALID_INPUT']
            cls.LOGIN_USER = data['LOGIN_USER']
            cls.USERNAME_ERROR = data['USERNAME_ERROR']
            cls.INVALID_CREDENTIALS = data['INVALID_CREDENTIALS']

    @classmethod
    def load_queries(cls):
        with open('config\\queries.yml','r') as f:
            data = yaml.safe_load(f)
            cls.QUERY_TO_CREATE_USERS_TABLE = data['QUERY_TO_CREATE_USERS_TABLE']
            cls.QUERY_TO_VERIFY_USERNAME = data['QUERY_TO_VERIFY_USERNAME']
            cls.QUERY_TO_CREATE_USER = data['QUERY_TO_CREATE_USER']
            cls.QUERY_TO_VERIFY_USER = data['QUERY_TO_VERIFY_USER']
            cls.QUERY_TO_FETCH_ROLE = data['QUERY_TO_FETCH_ROLE']

    @classmethod
    def load_prompts(cls):
        with open('config\\prompts.yml','r') as f:
            data = yaml.safe_load(f)     
            cls.MENU_PROMPTS = data['MENU_PROMPTS']   
            cls.USER_PROMPTS = data['USER_PROMPTS']
            cls.ADMIN_PROMPTS = data['ADMIN_PROMPTS']
            



