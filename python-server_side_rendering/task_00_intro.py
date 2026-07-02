#!/usr/bin/env python3
"""Uses a template to create personalized invitation files"""

import logging  # Useful to track how script behaves.
import os       # Required to manipulate filesystem.
import re       # Required to find and replace template's placeholders.

log = logging.getLogger('task_00_generator')
logging.basicConfig(
    # filename='task_00_traces.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s')
script_dir = os.path.dirname(os.path.abspath(__file__))


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


def inject_data_in_text(data, text):
    """Finds placeholders in text and replaces them with dict value or N/A"""
    placeholders = re.findall(r'\{(\w+)\}', text)
    for placeholder_name in placeholders:
        replacement = data.get(placeholder_name) or 'N/A'
        text = text.replace('{' + placeholder_name + '}', replacement)
    return text


def generate_invitations(template: str, attendees: list):
    """Uses provided template and event data list to generate invitations"""
    log.debug("@dev: inside generate_invitations")
    if not is_exploitable_input(template, attendees):
        return
    # We have a template and data, hoping they are actually exploitable.
    # Logic imo should be:
    # We traverse the data list.
    attendees_count = 0
    for attendee in attendees:
        # For each...
        # We define its number.
        attendees_count += 1
    # 0) We generate the filename and check if it exists already
        # Filename imposed as output_X.txt with X being number attributed.
        filename = f"output_{attendees_count}.txt"
        output_path = os.path.join(script_dir, filename)
        if os.path.exists(output_path):
            log.info(f"Invitation with name {filename} exists, skipping")
            continue
        else:
            personalized_invite = inject_data_in_text(attendee, str(template))
            with open(output_path, 'w') as output_file:
                output_file.write(personalized_invite)
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
    log.info("===== Task__00__intro.py: STARTING RUN =====")
    # VALID USE-CASE
    log.info("=== Calling function with valid input (expected: 3 files ===")
    attendees = [
        {"name": "Alice", "event_title": "Python Conference",
         "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop",
         "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit",
         "event_date": None, "event_location": "Boston"}
    ]
    log.debug(f"Attendees list: {attendees}")

    # REQUIRED to have the pre-commit hook run properly
    #   (needs to get an absolute path to files used)
    template_path = os.path.join(script_dir, 'template.txt')
    log.debug(f"Full path for template is: {template_path}")
    with open(template_path, 'r') as file:
        template_content = file.read()
    generate_invitations(template_content, attendees)

    # INVALID inputs
    # Invalid list content 1
    log.info("=== Generating invitations from invalid list content 1")
    generate_invitations("string", [1, 3, "toto"])
    # Invalid list content 2
    log.info("=== Generating invitations from invalid list content 2")
    generate_invitations(
        "string",
        [
          {"name": "Toto", "event_title": "-",
           "event_date": "2023-07-15",
           "event_location": "X"}, {}, "WRONG"
        ]
    )
    # Empty template
    log.info("=== Generating invitations from empty template")
    generate_invitations("", [{"name": "Empty template"}])
    # Empty list
    log.info("=== Generating invitations from empty list")
    generate_invitations("Empty list", [])

    # Incomplete dictionary
    log.info("=== Generating invitations for a single, incomplete attendee")
    generate_invitations(template_content, [{"name": "Incomplete"}])

# ===== BUSINESS REQUIREMENTS =====
# Errors must be logged for each of these situations
# - Parameters don't match expected types (string, list of dictionaries)
#     -> A custom error message indicating the type of invalid input.
# - Template is empty
#     -> "Template is empty, no output files generated."
# - List is empty
#     ->  "No data provided, no output files generated."
# If any error found terminate function

# ===== DESIGN NOTES =====
# == On placeholder identification and replacement process ===
# Warning: it is the template which should be "Source of Truth" because it
#   is the thing exposed to end-users. NOT the data.
# Especially since (now that I think about it) my previous logic made code
#   parse all dict elements even those which aren't expected in template
#   generating useless process.
# So we must dynamically get the list of placeholders from the template
#   and ensure "fallback value" so generator works in all situations.

# == On regex pattern used ==
# Note: '\{' '\}' required to have {} searched literally.
# Enclosing "any word" '\w+' in () ensures we can "extract" that word
#   without the brackets so we directly have the key to search in dict.
