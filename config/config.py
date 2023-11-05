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
            cls.LATITUDE = data['LATITUDE']
            cls.LONGITUDE = data['LONGITUDE']
            cls.NO_DATA = data['NO_DATA']
            cls.ENTER_CITYNAME = data['ENTER_CITYNAME']
            cls.ENTER_DAYS = data['ENTER_DAYS']
            cls.ENTER_USERID = data['ENTER_USERID']
            cls.FORMAT_DATE_TIME = data['FORMAT_DATE_TIME']
            cls.ADMIN = data['ADMIN']
            cls.LAT = data['LAT']
            cls.LON = data['LON']
            cls.CITY = data['CITY']
            cls.DAYS = data['DAYS']
            cls.QUIT = data['QUIT']
            cls.CITY_INPUT = data['CITY_INPUT']
            cls.FIRST = data['FIRST']
            cls.SECOND = data['SECOND']
            cls.THIRD = data['THIRD']
            cls.USER_DATA_HEADER = data['USER_DATA_HEADER']
            cls.TABLE_FORMAT = data['TABLE_FORMAT']
            cls.USER_BY_CITY_HEADER = data['USER_BY_CITY_HEADER']
            cls.HISTORY_HEADER = data['HISTORY_HEADER']
            cls.ALL_USERS_HEADER = data['ALL_USERS_HEADER']


    @classmethod
    def load_queries(cls):
        with open('config\\queries.yml','r') as f:
            data = yaml.safe_load(f)
            cls.QUERY_TO_CREATE_USERS_TABLE = data['QUERY_TO_CREATE_USERS_TABLE']
            cls.QUERY_TO_VERIFY_USERNAME = data['QUERY_TO_VERIFY_USERNAME']
            cls.QUERY_TO_CREATE_USER = data['QUERY_TO_CREATE_USER']
            cls.QUERY_TO_VERIFY_USER = data['QUERY_TO_VERIFY_USER']
            cls.QUERY_TO_FETCH_ROLE = data['QUERY_TO_FETCH_ROLE']
            cls.QUERY_TO_INSERT_SEARCH_HISTORY = data['QUERY_TO_INSERT_SEARCH_HISTORY']
            cls.QUERY_TO_CREATE_SEARCH_HISTORY_TABLE = data['QUERY_TO_CREATE_SEARCH_HISTORY_TABLE']
            cls.QUERY_TO_VIEW_USER = data['QUERY_TO_VIEW_USER']
            cls.QUERY_TO_VIEW_USER_BY_PLACE = data['QUERY_TO_VIEW_USER_BY_PLACE']
            cls.QUERY_TO_VIEW_HISTORY = data['QUERY_TO_VIEW_HISTORY']
            cls.QUERY_TO_FETCH_ALL_USERS = data['QUERY_TO_FETCH_ALL_USERS']


    @classmethod
    def load_prompts(cls):
        with open('config\\prompts.yml','r') as f:
            data = yaml.safe_load(f)     
            cls.MENU_PROMPTS = data['MENU_PROMPTS']   
            cls.USER_PROMPTS = data['USER_PROMPTS']
            cls.ADMIN_PROMPTS = data['ADMIN_PROMPTS']
            cls.USER_VIEW_PROMPTS = data['USER_VIEW_PROMPTS']
            



