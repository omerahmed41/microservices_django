import logging

logger = logging.getLogger(__name__)
def send_rejection_email(client_id, rejected_docs_ids):
    logger.warning('DQ task')
    return "send_rejection_email successes"


def print_text(text):
    write_test_file(text)
    return True


def write_test_file(text):
    file1 = open("myfile.txt", "w")
    L = [text]

    # \n is placed to indicate EOL (End of Line)
    file1.write("Hello \n")
    file1.writelines(L)
    file1.close()


def print_result(task):
    logger.warning('Task.result:')
    logger.warning(task.result)

