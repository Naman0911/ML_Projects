import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Creating a Log file name , Which will use the current date time in the format which is given
# for Example --> 02_01_2026_14_35_20 then after wards the .log is added as the extension
# Every time you run the script → a unique log file is created.


logs_path = os.path.join(os.getcwd(),"logs")
# Whenever a log file will be created it will be created in the current working directory cwd with the prefix as logs
# current_directory + "logs" + LOG_FILE
# Example --> C:\Users\Naman\Project\logs\02_01_2026_14_35_20.log


os.makedirs(logs_path,exist_ok=True)
# It tell if there is logs_path file is there then append inside that file everytime when the logging is done

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


# For testing the logging
# if __name__ == "__main__":
#     logging.info("Logging Has Started")


# When you write:

# from logger import logging
# Executes logger.py
# That runs logging.basicConfig(...)
# Then gives you the configured logging object
# Now all your logs follow your custom configuration.