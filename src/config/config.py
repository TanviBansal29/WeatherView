import yaml

class Config:
    SIGNUP_PROMPT = None
    WELCOME_MESSAGE = None
    ENTER_USERNAME = None
    ENTER_PASSWORD = None
    ENTER_CITY = None
    ENTER_ZIPCODE = None
    DATABASE_NAME = None
    LOGIN_ADMIN = None
    INVALID_INPUT = None
    LOGIN_USER = None
    USERNAME_ERROR = None
    INVALID_CREDENTIALS = None
    LATITUDE = None
    LONGITUDE = None
    NO_DATA = None
    ENTER_CITYNAME = None
    ENTER_DAYS = None
    ENTER_USERID = None
    FORMAT_DATE_TIME = None
    ADMIN = None
    LAT = None
    LON = None
    CITY = None
    DAYS = None
    QUIT = None
    CITY_INPUT = None
    FIRST = None
    SECOND = None
    THIRD = None
    TABLE_FORMAT = None
    CITY_NAME = None
    LAT_LON = None
    CURRENT_WEATHER = None
    FORECAST = None
    STRONG_PASSWORD_PROMPT = None
    CITY_REGEX = None
    ZIPCODE_REGEX = None
    PASSWORD_REGEX = None
    SIGNUP_PRMOMPT = None
    USERNAME_REGEX = None
    QUERY_TO_CREATE_USERS_TABLE = None
    QUERY_TO_VERIFY_USERNAME = None
    QUERY_TO_CREATE_USER = None
    QUERY_TO_VERIFY_USER = None
    QUERY_TO_FETCH_ROLE = None
    QUERY_TO_INSERT_SEARCH_HISTORY = None
    QUERY_TO_CREATE_SEARCH_HISTORY_TABLE = None
    QUERY_TO_VIEW_USER = None
    QUERY_TO_VIEW_USER_BY_PLACE = None
    QUERY_TO_VIEW_HISTORY = None
    QUERY_TO_FETCH_ALL_USERS = None
    MENU_PROMPTS = None
    USER_PROMPTS = None
    ADMIN_PROMPTS = None
    USER_VIEW_PROMPTS = None

    @classmethod
    def load_print_statements(cls):
        with open('config\\print_statements.yml', 'r') as f:
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
            cls.TABLE_FORMAT = data['TABLE_FORMAT']
            cls.CITY_NAME = data['CITY_NAME']
            cls.LAT_LON = data['LAT_LON']
            cls.CURRENT_WEATHER = data['CURRENT_WEATHER']
            cls.FORECAST = data['FORECAST']
            cls.STRONG_PASSWORD_PROMPT = data['STRONG_PASSWORD_PROMPT']
            cls.CITY_REGEX = data['CITY_REGEX']
            cls.ZIPCODE_REGEX = data['ZIPCODE_REGEX']
            cls.PASSWORD_REGEX = data['PASSWORD_REGEX']
            cls.SIGNUP_PROMPT = data['SIGNUP_PROMPT']
            cls.USERNAME_REGEX = data['USERNAME_REGEX']

    @classmethod
    def load_queries(cls):
        with open('config\\queries.yml', 'r') as f:
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
        with open('config\\prompts.yml', 'r') as f:
            data = yaml.safe_load(f)
            cls.MENU_PROMPTS = data['MENU_PROMPTS']
            cls.USER_PROMPTS = data['USER_PROMPTS']
            cls.ADMIN_PROMPTS = data['ADMIN_PROMPTS']
            cls.USER_VIEW_PROMPTS = data['USER_VIEW_PROMPTS']


Config.load_print_statements()
Config.load_queries()
Config.load_prompts()
