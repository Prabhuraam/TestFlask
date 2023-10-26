import logging


def handler(event, context):
    logger = logging.getLogger()
    logger.info('Hello from main.py')

    data = event.get_data()  # event data
    time = event.get_time()  # event occurred time
    action = event.get_action()
    source_details = event.get_source()
    source_entity_id = event.get_source_entity_id()
    event_bus_details = event.get_event_bus_details()
    project_details = event.get_project_details()
    logging.info(f"This is the data:{data}")
    logging.info(f"This is the time:{time}")
    logging.info(f"This is the action:{action}")
    logging.info(f"This is the source_details:{source_details}")
    logging.info(f"This is the source_entity_id:{source_entity_id}")
    logging.info(f"This is the event_bus_details:{event_bus_details}")
    logging.info(f"This is the project_details:{project_details}")

    '''Context Functionalities'''
    remaining_execution_time_ms = context.get_remaining_execution_time_ms()
    max_execution_time_ms = context.get_max_execution_time_ms()
    logging.info(f"This is the remaining_execution_time_ms:{remaining_execution_time_ms}")
    logging.info(f"This is the max_execution_time_ms:{max_execution_time_ms}")
    # context.close_with_failure()
    context.close_with_success()
