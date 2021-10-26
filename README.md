# logram
Python logger with different handlers

```
pip install logram
```

### Add LOGGING configurations

Only different part is telegram handler

```python
import logging
from logging.config import dictConfig
from logram.handlers import Telegram


Telegram.token = "20**:AA*****"
Telegram.chat_id = "-6***"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(levelname)s] [%(asctime)s] [%(module)s] [line:%(lineno)d] %(message)s"
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "logs/log",
            "formatter": "verbose",
            "encoding": "UTF-8",
        },
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "telegram": {
            "level": "WARNING",
            "class": "logram.handlers.Telegram",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {"handlers": ["console"], "level": "INFO", "propagate": True},
        "offices": {"handlers": ["console", "file"], "level": "INFO", "propagate": False},
        "smsreport": {"handlers": ["console", "telegram",  "file"], "level": "INFO", "propagate": True},
        "qinspect": {"handlers": ["console"], "level": "INFO", "propagate": True,},
    },
}

dictConfig(LOGGING)

```

Then this will send messages right into the Telegram Group 
```
logging.warning("Send directly to the Telegram group")
```