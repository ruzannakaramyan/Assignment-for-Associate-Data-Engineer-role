import mysql.connector
import os
from datetime import datetime
import json
import random

# Environment variables
DB_HOST = os.getenv('DATABASE_HOST', 'db')
DB_USER = os.getenv('DATABASE_USER', 'root')
DB_PASSWORD = os.getenv('DATABASE_PASSWORD', 'examplepassword')
DB_NAME = os.getenv('DATABASE_NAME', 'user_metrics')


# Connect to MySQL database
def connect_to_db():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )


# Generate random data for simulation
def generate_random_data():
    now = datetime.now()
    data = {
        'talked_time': {
            'time_stamp': now,
            'user_id': 'user_{}'.format(random.randint(1, 10)),
            'session_id': 'session_{}'.format(random.randint(1, 10)),
            'device_id': 'device_{}'.format(random.randint(1, 10)),
            'location': 'location_{}'.format(random.randint(1, 10)),
            'duration': random.uniform(1.0, 120.0),
            'metadata': json.dumps({'key': 'value'})
        },
        'microphone_used': {
            'time_stamp': now,
            'user_id': 'user_{}'.format(random.randint(1, 10)),
            'session_id': 'session_{}'.format(random.randint(1, 10)),
            'device_id': 'device_{}'.format(random.randint(1, 10)),
            'location': 'location_{}'.format(random.randint(1, 10)),
            'usage_duration': random.uniform(1.0, 60.0),
            'microphone_type': 'type_{}'.format(random.randint(1, 5)),
            'metadata': json.dumps({'key': 'value'})
        },
        'speaker_used': {
            'time_stamp': now,
            'user_id': 'user_{}'.format(random.randint(1, 10)),
            'session_id': 'session_{}'.format(random.randint(1, 10)),
            'device_id': 'device_{}'.format(random.randint(1, 10)),
            'location': 'location_{}'.format(random.randint(1, 10)),
            'usage_duration': random.uniform(1.0, 60.0),
            'speaker_type': 'type_{}'.format(random.randint(1, 5)),
            'metadata': json.dumps({'key': 'value'})
        },
        'voice_sentiment': {
            'time_stamp': now,
            'user_id': 'user_{}'.format(random.randint(1, 10)),
            'session_id': 'session_{}'.format(random.randint(1, 10)),
            'device_id': 'device_{}'.format(random.randint(1, 10)),
            'location': 'location_{}'.format(random.randint(1, 10)),
            'sentiment_score': random.uniform(-1.0, 1.0),
            'sentiment_label': 'label_{}'.format(random.randint(1, 5)),
            'metadata': json.dumps({'key': 'value'})
        }
    }
    return data


# Insert data into the database
def insert_data(table_name, data):
    conn = connect_to_db()
    cursor = conn.cursor()

    if table_name == 'talked_time':
        cursor.execute("""
            INSERT INTO talked_time (time_stamp, user_id, session_id, device_id, location, duration, metadata)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
        data['time_stamp'], data['user_id'], data['session_id'], data['device_id'], data['location'], data['duration'],
        data['metadata']))

    elif table_name == 'microphone_used':
        cursor.execute("""
            INSERT INTO microphone_used (time_stamp, user_id, session_id, device_id, location, usage_duration, microphone_type, metadata)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (data['time_stamp'], data['user_id'], data['session_id'], data['device_id'], data['location'],
              data['usage_duration'], data['microphone_type'], data['metadata']))

    elif table_name == 'speaker_used':
        cursor.execute("""
            INSERT INTO speaker_used (time_stamp, user_id, session_id, device_id, location, usage_duration, speaker_type, metadata)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (data['time_stamp'], data['user_id'], data['session_id'], data['device_id'], data['location'],
              data['usage_duration'], data['speaker_type'], data['metadata']))

    elif table_name == 'voice_sentiment':
        cursor.execute("""
            INSERT INTO voice_sentiment (time_stamp, user_id, session_id, device_id, location, sentiment_score, sentiment_label, metadata)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (data['time_stamp'], data['user_id'], data['session_id'], data['device_id'], data['location'],
              data['sentiment_score'], data['sentiment_label'], data['metadata']))

    conn.commit()
    cursor.close()
    conn.close()


# Main function to run data ingestion
def ingest_data():
    data = generate_random_data()

    for table_name, record in data.items():
        insert_data(table_name, record)


if __name__ == "__main__":
    ingest_data()
