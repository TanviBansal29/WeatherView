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
    LOGGING_FORMAT = None
    DATE_TIME_FORMAT = None
    LOGS_LOCATION = None
    APP_START = None
    APP_END = None
    START_MENU = None
    ROLE = None
    GET_ZIPCODE_START = None
    USER_ID : None
    INVALID_ZIPCODE = None
    SIGNIN_INPUTS = None
    VERIFY_USERNAME = None
    GET_CITYNAME = None
    INVALID_CITYNAME = None
    GET_USERNAME = None
    VALID_USERNAME = None
    GET_PASSWORD = None
    TYPE_WEATHER = None
    TYPE_FORECAST = None
    TYPE_HISTORY = None
    BLANK = None
    TYPE_USERNAME = None
    TYPE_CITY = None
    USERNAME_HEADERS = None
    CITY_HEADERS = None
    FORECAST_HEADER = None
    WEATHER_HEADER = None
    HISTORY_HEADER = None
    NEW_USER_SIGNUP = None
    LOGIN_SUCCESS = None
    VERIFYING_USERNAME = None
    CREATE_ACCOUNT = None
    FETCH_DATA = None
    LOGGING = None
    WEATHER_DATA_LOG = None
    FETCH_USER_DATA = None
    FETCH_USER_DATA_IN_CITY = None
    FETCH_ALL_USER = None
    WEATHER_URL = None
    FORECAST_URL = None
    SECRET_KEY = None
    API_HOST = None
    SECRET_KEY_FORECAST = None
    FORECAST_API_HOST = None
    X_RAPIDAPI_HOST = None
    X_RAPIDAPI_KEY = None
    USERS_SUCCESS_LOG = None
    SUNSET= None              
    SUNRISE= None              
    MAXTEMP= None
    HISTORY_VIEW = None
    INSERTED_HISTORY = None
    INSERTING_HISTORY = None
    GET_WEATHER_CITY = None
    GET_WEATHER_SUCCESS = None
    GET_WEATHER_COORDINATES = None
    GET_WEATHER_COORDINATES_SUCCESS = None
    GET_FORECAST = None
    GET_FORECAST_SUCCESS = None

    @classmethod
    def load_print_statements(cls):
        with open('src\\config\\print_statements.yml', 'r') as f:
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
        with open('src\\config\\queries.yml', 'r') as f:
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
        with open('src\\config\\prompts.yml', 'r') as f:
            data = yaml.safe_load(f)
            cls.MENU_PROMPTS = data['MENU_PROMPTS']
            cls.USER_PROMPTS = data['USER_PROMPTS']
            cls.ADMIN_PROMPTS = data['ADMIN_PROMPTS']
            cls.USER_VIEW_PROMPTS = data['USER_VIEW_PROMPTS']

    @classmethod
    def load_constants(cls):
        with open('src\\config\\constants.yml', 'r') as f:
            data = yaml.safe_load(f)
            cls.LOGGING_FORMAT = data['LOGGING_FORMAT']
            cls.DATE_TIME_FORMAT = data['DATE_TIME_FORMAT']
            cls.LOGS_LOCATION = data['LOGS_LOCATION']
            cls.APP_START = data['APP_START']
            cls.APP_END = data['APP_END']
            cls.START_MENU = data['START_MENU']
            cls.LOGIN_INPUTS = data['LOGIN_INPUTS']
            cls.ROLE = data['ROLE']
            cls.USER_ID = data['USER_ID']
            cls.GET_ZIPCODE_START = data['GET_ZIPCODE_START']
            cls.INVALID_ZIPCODE = data['INVALID_ZIPCODE']
            cls.SIGNIN_INPUTS = data['SIGNIN_INPUTS']
            cls.VERIFY_USERNAME = data['VERIFY_USERNAME']
            cls.GET_CITYNAME = data['GET_CITYNAME']
            cls.INVALID_CITYNAME = data['INVALID_CITYNAME']
            cls.GET_USERNAME = data['GET_USERNAME']
            cls.VALID_USERNAME = data['VALID_USERNAME']
            cls.GET_PASSWORD = data['GET_PASSWORD']
            cls.TYPE_WEATHER = data['TYPE_WEATHER']
            cls.TYPE_FORECAST = data['TYPE_FORECAST']
            cls.TYPE_HISTORY = data['TYPE_HISTORY']
            cls.BLANK = data['BLANK']
            cls.TYPE_USERNAME = data['TYPE_USERNAME']
            cls.TYPE_CITY = data['TYPE_CITY']
            cls.USERNAME_HEADERS = data['USERNAME_HEADERS']
            cls.CITY_HEADERS = data['CITY_HEADERS']
            cls.WEATHER_HEADER = data['WEATHER_HEADER']
            cls.FORECAST_HEADER = data['FORECAST_HEADER']
            cls.HISTORY_HEADER = data['HISTORY_HEADER']
            cls.NEW_USER_SIGNUP = data['NEW_USER_SIGNUP']
            cls.LOGIN_SUCCESS = data['LOGIN_SUCCESS']
            cls.VERIFYING_USERNAME = data['VERIFY_USERNAME']
            cls.CREATE_ACCOUNT = data['CREATE_ACCOUNT']
            cls.FETCH_DATA = data['FETCH_DATA']
            cls.LOGGING = data['LOGGING']
            cls.WEATHER_DATA_LOG = data['WEATHER_DATA_LOG']
            cls.FETCH_USER_DATA = data['FETCH_USER_DATA ']
            cls.FETCH_USER_DATA_IN_CITY = data['FETCH_USER_DATA_IN_CITY']
            cls.FETCH_ALL_USER = data['FETCH_ALL_USER']
            cls.WEATHER_URL = data['WEATHER_URL']
            cls.FORECAST_URL = data['FORECAST_URL']
            cls.SECRET_KEY = data['SECRET_KEY']
            cls.API_HOST = data['API_HOST']
            cls.SECRET_KEY_FORECAST = data['SECRET_KEY_FORECAST']
            cls.FORECAST_API_HOST = data['FORECAST_API_HOST']
            cls.X_RAPIDAPI_HOST = data['X_RAPIDAPI_HOST']
            cls.X_RAPIDAPI_KEY = data['X_RAPIDAPI_KEY']
            cls.USERS_SUCCESS_LOG = data['USERS_SUCCESS_LOG']
            cls.SUNSET = data['SUNSET']
            cls.SUNRISE = data['SUNRISE']
            cls.MAXTEMP = data['MAXTEMP']
            cls.HISTORY_VIEW = data['HISTORY_VIEW']
            cls.INSERTED_HISTORY = data['INSERTED_HISTORY']
            cls.INSERTING_HISTORY = data['INSERTING_HISTORY']
            cls.GET_WEATHER_CITY = data['GET_WEATHER_CITY']
            cls.GET_WEATHER_SUCCESS = data['GET_WEATHER_SUCCESS']
            cls.GET_WEATHER_COORDINATES = data['GET_WEATHER_COORDINATES']
            cls.GET_WEATHER_COORDINATES_SUCCESS = data['GET_WEATHER_COORDINATES_SUCCESS']
            cls.GET_FORECAST = data['GET_FORECAST']
            cls.GET_FORECAST_SUCCESS = data['GET_FORECAST_SUCCESS']


Config.load_print_statements()
Config.load_queries()
Config.load_prompts()
Config.load_constants()
