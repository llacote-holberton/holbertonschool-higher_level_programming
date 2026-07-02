#!/usr/bin/env python3
"""Uses a template to create personalized invitation files"""

import logging
import os

log = logging.getLogger('task_00_generator')
logging.basicConfig(
    filename='task_00_errors.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')


def valid_inputs(template, attendees):
    log.debug("@dev inside check_inputs function")
    return (
        isinstance(template, str)
        and isinstance(attendees, list)
        and all(isinstance(subscription, dict) for subscription in attendees)
    )


def is_exploitable_input(template, attendees):
    """Makes all checks to ensure we have all needed to generate invitations"""

    # Template checks: non-empty string (no check on placeholders existing)
    if not isinstance(template, str):
        log.error(f"Template given is of type {type(template)}, str required")
        return False
    if not template:
        log.error("Template is empty, no output files generated.")
        return False
    # Attendees check: list containing only dictionaries, no deeper check.
    if not isinstance(attendees, list):
        log.error(f"Attendees arg is of type {type(attendees)}, list required")
        return False
    if not all(isinstance(subscription, dict) for subscription in attendees):
        log.error("No data provided, no output files generated.")
        return False
    return True


def generate_invitations(template: str, attendees: list):
    """Uses provided template and event data list to generate invitations"""
    print("@dev: inside generate_invitations")
    if not is_exploitable_input(template, attendees):
        return
    # We have a template and data, hoping they are actually exploitable.
    # Logic imo should be:
    # We traverse the data list. For each...
    # 0) We generate the filename and check if it exists already
    #    (making the assumption no external process would have affected it).
    #    If it already exists we consider it's already processed and continue.
    #    Otherwise...
    # 1) We grab a copy of the template.
    # 2) We make a subloop charged to check, for each data key,
    #    if a placeholder exists in template for it.
    #    And case arising replacing the {placeholder} with associated value.
    # 3) Once the invitation string has been adjusted, we write it down
    #    inside the same folder with a predetermined filename.
    #    Then continue to the next "outer loop" cycle.


if __name__ == "__main__":
    # VALID USE-CASE
    attendees = [
        {"name": "Alice", "event_title": "Python Conference",
         "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop",
         "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit",
         "event_date": None, "event_location": "Boston"}
    ]

    # REQUIRED to have the pre-commit hook run properly
    #   (needs to get an absolute path to files used)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, 'template.txt')
    with open(template_path, 'r') as file:
        template_content = file.read()
    generate_invitations(template_content, attendees)

    # INVALID inputs
    # Invalid list content 1
    print("=== Generating invitations from invalid list content 1")
    generate_invitations("string", [1, 3, "toto"])
    # Invalid list content 2
    print("=== Generating invitations from invalid list content 2")
    generate_invitations(
        "string",
        [
          {"name": "Toto", "event_title": "-",
           "event_date": "2023-07-15",
           "event_location": "X"}, {}, "WRONG"
        ]
    )
    # Empty template
    print("=== Generating invitations from empty template")
    generate_invitations("", [{"name": "Empty template"}])
    # Empty list
    print("=== Generating invitations from empty list")
    generate_invitations("Empty list", [])

# ===== BUSINESS REQUIREMENTS =====
# Errors must be logged for each of these situations
# - Parameters don't match expected types (string, list of dictionaries)
#     -> A custom error message indicating the type of invalid input.
# - Template is empty
#     -> "Template is empty, no output files generated."
# - List is empty
#     ->  "No data provided, no output files generated."
# If any error found terminate function
