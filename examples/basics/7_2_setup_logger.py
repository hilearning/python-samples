# 将日志信息写入文件
import logging

def setup_logger(log_file):
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

setup_logger('app.log')
logging.info("This is a log message.")
print("Log message written to app.log")
