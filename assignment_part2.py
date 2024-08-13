############
 #
 # Cheap Crowdfunding Problem
 #
 # There is a crowdfunding project that you want to support. This project
 # gives the same reward to every supporter, with one peculiar condition:
 # the amount you pledge must not be equal to any earlier pledge amount.
 #
 # You would like to get the reward, while spending the least amount > 0.
 #
 # You are given a list of amounts pledged so far in an array of integers.
 # You know that there is less than 100,000 of pledges and the maximum
 # amount pledged is less than $1,000,000.
 #
 # Implement a function find_min_pledge(pledge_list) that will return
 # the amount you should pledge.
 #
 ############
def find_min_pledge(pledge_list):
    pledged_set = set(pledge_list)

    smallest_positive = 1

    while smallest_positive in pledged_set:
        smallest_positive += 1

    return smallest_positive

# Test cases
assert find_min_pledge([1, 3, 6, 4, 1, 2]) == 5
assert find_min_pledge([1, 2, 3]) == 4
assert find_min_pledge([-1, -3]) == 1

import requests
import xml.etree.ElementTree as ET


def get_headlines(rss_url):

    try:
        # Fetch the RSS feed
        response = requests.get(rss_url)
        response.raise_for_status()  # Raise an error for bad responses (e.g., 404, 500)

        # Parse the XML content
        root = ET.fromstring(response.content)

        # Extract titles
        titles = []
        for item in root.findall('.//item'):
            title = item.find('title').text
            if title:
                titles.append(title)

        return titles

    except requests.RequestException as e:
        print(f"Error fetching RSS feed: {e}")
        return []
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return []


# Example usage
google_news_url = "https://news.google.com/news/rss"
print(get_headlines(google_news_url))

############
#
# Streaming Payments Processor

############

import io


# This is a library function, you can't modify it.
def get_payments_storage():
    # Sample implementation to make the code run in coderpad.
    # Do not rely on this exact implementation.
    return open('/dev/null', 'wb')


# This is a library function, you can't modify it.
def stream_payments_to_storage(storage):
    # Sample implementation to make the code run in coderpad.
    # Do not rely on this exact implementation.
    for i in range(10):
        storage.write(bytes([1, 2, 3, 4, 5]))


class ChecksumBufferedWriter(io.BufferedWriter):
    def __init__(self, underlying):
        super().__init__(underlying)
        self.checksum = 0

    def write(self, b):
        # Calculate checksum of the bytes being written
        self.checksum += sum(b)
        super().write(b)


def process_payments():
    # Get the underlying storage
    underlying_storage = get_payments_storage()

    # Wrap the underlying storage with ChecksumBufferedWriter
    checksum_storage = ChecksumBufferedWriter(underlying_storage)

    # Stream payments to the checksum_storage
    stream_payments_to_storage(checksum_storage)

    # Print the checksum of all bytes written
    print(checksum_storage.checksum)


# Here print the check sum of all of the bytes written by
# `stream_payments_to_storage()`
process_payments()


############
# Streaming Payments Processor, two vendors edition.

# This is a library function, you can't modify it.
def stream_payments(callback_fn):
    # Sample implementation to make the code run in coderpad.
    # Do not rely on this exact implementation.
    for i in range(10):
        callback_fn(i)


# This is a library function, you can't modify it.
def store_payments(amount_iterator):
    """
    Iterates over the payment amounts from amount_iterator
    and stores them to a remote system.
    """
    # Sample implementation to make the code run in coderpad.
    # Do not rely on this exact implementation.
    for i in amount_iterator:
        print(i)


def callback_example(amount):
    print(amount)
    return True


class PaymentIterator:
    def __init__(self):
        self.payments = []
        self.index = 0

    def add_payment(self, amount):
        self.payments.append(amount)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.payments):
            raise StopIteration
        payment = self.payments[self.index]
        self.index += 1
        return payment


def process_payments_2():
    """
    TODO:
    Modify `process_payments_2()`, write glue code that enables
    `store_payments()` to consume payments produced by `stream_payments()`
    """

    # Create an instance of PaymentIterator
    payment_iterator = PaymentIterator()

    # Define a callback function to add payments to the iterator
    def callback_fn(amount):
        payment_iterator.add_payment(amount)

    # Stream payments and use the callback function to populate the iterator
    stream_payments(callback_fn)

    # Use the iterator to store the payments
    store_payments(payment_iterator)


process_payments_2()


############
#
# Code Review
#
# Please do a code review for the following snippet.
# Add your review suggestions inline as python comments
#
############
def get_value(data, key, default, lookup=None, mapper=None):
    """
         Finds the value from data associated with key, or default if the
         key isn't present.
         If a lookup enum is provided, this value is then transformed to its
         enum value.
         If a mapper function is provided, this value is then transformed
         by applying mapper to it.
         """
    # Check if the key exists in the data dictionary
    if key not in data:
        return default  # Return default if the key is not present

    return_value = data[key]

    if return_value is None or return_value == "":
        return_value = default

    if lookup:
        # Ensure lookup is a dictionary or similar mapping
        if isinstance(lookup, dict):
            # Use default if key not found in lookup
            return_value = lookup.get(return_value, default)
        else:
            raise ValueError("lookup must be a dictionary")  # Raise error if lookup is not a dictionary

    if mapper:
        # Ensure mapper is callable
        if callable(mapper):
            return_value = mapper(return_value)
        else:
            raise ValueError("mapper must be a callable function")  # Raise error if mapper is not callable

    return return_value


def ftp_file_prefix(namespace):
    """
     Given a namespace string with dot-separated tokens, returns the
     string with
     the final token replaced by 'ftp'.
     Example: a.b.c => a.b.ftp
     """

    # return ".".join(namespace.split(".")[:-1]) + '.ftp'

    # Here is how I see more efficient solution
    # Split the namespace into tokens based on dots
    tokens = namespace.split(".")

    # Ensure there is at least one token to avoid index errors
    if not tokens:
        raise ValueError("Namespace cannot be empty")

    # Replace the last token with 'ftp'
    # Join all tokens except the last one, appending '.ftp'
    return ".".join(tokens[:-1]) + '.ftp'


def string_to_bool(string):
    """
     Returns True if the given string is 'true' case-insensitive,
     False if it is
     'false' case-insensitive.
     Raises ValueError for any other input.
     """
    # we can add this block to check that only string inputs are processed
    if not isinstance(string, str):
        raise TypeError(f'Expected string, got {type(string).__name__}')

    if string.lower() == 'true':
        return True
    if string.lower() == 'false':
        return False
    raise ValueError(f'String {string} is neither true nor false')


def config_from_dict(dict):
    """
    Given a dict representing a row from a namespaces csv file,
    returns a DAG configuration as a pair whose first element is the
    DAG name
    and whose second element is a dict describing the DAG's properties
    """

    # It's better to avoid using 'dict' as a variable name because it shadows the built-in dict type.
    # Use a more descriptive name like 'row_data'.So instead of namespace = dict['Namespace'] I would write

    row_data = dict
    namespace = row_data['Namespace']
    # I would then change dict everywhere with row data

    return (row_data['Airflow DAG'],
            {"earliest_available_delta_days": 0,
             "lif_encoding": 'json',
             "earliest_available_time":
                 get_value(row_data, 'Available Start Time', '07:00'),
             "latest_available_time":
                 get_value(row_data, 'Available End Time', '08:00'),
             "require_schema_match":
                 get_value(row_data, 'Requires Schema Match', 'True',
                           mapper=string_to_bool),
             "schedule_interval":
                 get_value(row_data, 'Schedule', '1 7 * * * '),
             "delta_days":
                 get_value(row_data, 'Delta Days', 'DAY_BEFORE',
                           lookup=DeltaDays),
             "ftp_file_wildcard":
                 get_value(row_data, 'File Naming Pattern', None),
             "ftp_file_prefix":
                 get_value(row_data, 'FTP File Prefix',
                           ftp_file_prefix(namespace)),
             "namespace": namespace
             }
            )




