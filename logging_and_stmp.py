#!/usr/bin/env python3

import sys
import configparser

# logging
import logging

# https://docs.python.org/ja/3/library/logging.html#formatter-objects
# formatter = '%(levelname)s: %(message)s'
formatter = "%(asctime)s: %(levelname)s: %(message)s"
# logging.basicConfig(
#     level=logging.INFO, filename="test.log", filemode="w", format=formatter
# )

logging.basicConfig(level=logging.INFO, format=formatter)


class NoPasswdFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        return "password" not in log_message


logging.critical("critical")
logging.error("error")
logging.warning("warning")
logging.info("info")
logging.debug("debug")

logging.info("%s %s", "foo", "bar")

logging.info("%s %s", "foo", "bar", extra={"key": "value"})
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.debug("debug")

import logtest

logger = logging.getLogger(__name__)
logger.addFilter(NoPasswdFilter())
logger.info("from main")
logger.info("from main passwd: %s", "password")

logtest.do_something()

import logging.config

logging.config.fileConfig("logging.ini")
logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "sampleFormatter": {"format": "%(asctime)s: %(levelname)s: %(message)s"},
        },
        "handlers": {
            "sampleHandlers": {
                "class": "logging.StreamHandler",
                "formatter": "sampleFormatter",
                "level": logging.DEBUG,
            }
        },
        "root": {"handers": ["sampleHandlers"], "level": logging.WARNING},
        "loggers": {
            "sampleLoggers": {
                "handlers": ["sampleHandlers"],
                "level": logging.DEBUG,
                "propagate": 0,
            }
        },
    }
)
logger = logging.getLogger(__name__)
logger = logging.getLogger("sampleLoggers")

logger.debug("debug message from main")
logger.info("info message from main")
logger.warning("warning message from main")
logger.error("error message from main")
logger.critical("critical message from main")

# https://docs.python.org/ja/3/library/email.message.html
# from email import message # Only send text
from email.mime import multipart
from email.mime import text
import smtplib
import ssl

import config

config = config.make_config()

smtp_host = "smtp.gmail.com"
smtp_port = 465
from_email = config["EMAIL"]["address"]
to_email = config["EMAIL"]["address"]
user_name = config["EMAIL"]["user_name"]
password = config["EMAIL"]["password"]

print(f"smtp_host: {smtp_host} type: {type(smtp_host)}")
print(f"smtp_port: {smtp_port} type: {type(smtp_port)}")

# msg = message.EmailMessage()
msg = multipart.MIMEMultipart()
# msg.set_content("This is a test email")
msg["Subject"] = "Test from Python Script"
msg["From"] = from_email
msg["To"] = to_email
msg.attach(text.MIMEText("Test email", "plain"))

# attachment
with open("code_fragments.py", "r") as f:
    attachment = text.MIMEText(f.read(), "plain")
    attachment.add_header(
        "Content-Disposition", "attachment", filename="code_fragments.txt"
    )
    msg.attach(attachment)

# server = smtplib.SMTP(smtp_host, smtp_port)
server = smtplib.SMTP_SSL(smtp_host, smtp_port, context=ssl.create_default_context())

server.set_debuglevel(True)
server.ehlo()
if server.has_extn("STARTTLS"):
    server.starttls()
server.ehlo()
server.login(user_name, password)
server.send_message(msg)
server.quit()

import logging.handlers

ssl = smtplib.SMTP_SSL(smtp_host, smtp_port, context=ssl.create_default_context())

logger = logging.getLogger("email")
logger.setLevel(logging.CRITICAL)

logger.addHandler(
    logging.handlers.SMTPHandler(
        (smtp_host, smtp_port),
        from_email,
        to_email,
        subject="Admin test log",
        credentials=(user_name, password),
        secure=(ssl),
        timeout=20,
    )
)

logger.info("test")
logger.critical("critical")

if __name__ == "__main__":
    sys.exit(0)
