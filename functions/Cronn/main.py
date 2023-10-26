import logging


def handler(cron_details, context):
    logger = logging.getLogger()
    logger.info('Hello from main.py')

    '''CronDetails Functionalities'''
    cron_param = cron_details.get_cron_param('')
    remaining_execution_count = cron_details.get_remaining_execution_count()
    cron_details1 = cron_details.get_cron_details()
    project_details = cron_details.get_project_details()
    logging.info(f"cron_param:{cron_param}")
    logging.info(f"remaining_execution_count:{remaining_execution_count}")
    logging.info(f"cron_details:{cron_details1}")
    logging.info(f"project_details:{project_details}")

    '''Context Functionalities'''
    remaining_execution_time_ms = context.get_remaining_execution_time_ms()
    max_execution_time_ms = context.get_max_execution_time_ms()
    logging.info(f"remaining_execution_time_ms:{remaining_execution_time_ms}")
    logging.info(f"max_execution_time_ms:{max_execution_time_ms}")
    # context.close_with_failure()
    context.close_with_success()
