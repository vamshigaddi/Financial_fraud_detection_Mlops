import logging
import logging.config
import os

# Define log file path
log_file_path = os.path.join(os.path.dirname(__file__), 'project_logs.log')

# Logging configuration
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': log_file_path,
            'formatter': 'standard',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)
