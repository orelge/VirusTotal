URLS_CSV_FILE_PATH = r"C:\Users\אוראל\PycharmProjects\elementor_task\src\data\csv_files\urls.csv"
URLS_COLUMN = 'urls'
URL_COLUMN = 'url'
URL_CLASSIFICATION_COLUMN = 'url_classification'
DB_NAME = 'virus-risk.db'
URLS_CLASSIFICATION_TABLE = 'urls-classification'
CATEGORIES_TABLE = 'categories'
VOTING_TABLE = 'voting'
GET_DATA_FROM_URLS_CLASSIFICATION_TABLE_QUERY = f'''
SELECT *
FROM {URLS_CLASSIFICATION_TABLE}
'''
IS_TABLE_EXIST_QUERY = '''
SELECT * FROM sqlite_master where type='table';
'''
