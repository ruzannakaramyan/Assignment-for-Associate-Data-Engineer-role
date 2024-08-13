-- Create database
CREATE DATABASE user_metrics;

-- Switch to the new database

CREATE TABLE talked_time (
    id INT AUTO_INCREMENT PRIMARY KEY,
    time_stamp DATETIME NOT NULL,
    user_id VARCHAR(50) NOT NULL,
    session_id VARCHAR(50) NOT NULL,
    device_id VARCHAR(50),
    location VARCHAR(100),
    duration FLOAT NOT NULL,
    metadata JSON,
    UNIQUE KEY unique_timedata (time_stamp, user_id, session_id)
);


-- Table for storing microphone usage metrics
CREATE TABLE microphone_used (
    id INT AUTO_INCREMENT PRIMARY KEY,
    time_stamp DATETIME NOT NULL,
    user_id VARCHAR(50) NOT NULL,
    session_id VARCHAR(50) NOT NULL,
    device_id VARCHAR(50),
    location VARCHAR(100),
    usage_duration FLOAT NOT NULL,
    microphone_type VARCHAR(50),
    metadata JSON,
    UNIQUE KEY unique_microphone (time_stamp, user_id, session_id)
);

-- Table for storing speaker usage metrics
CREATE TABLE speaker_used (
    id INT AUTO_INCREMENT PRIMARY KEY,
    time_stamp DATETIME NOT NULL,
    user_id VARCHAR(50) NOT NULL,
    session_id VARCHAR(50) NOT NULL,
    device_id VARCHAR(50),
    location VARCHAR(100),
    usage_duration FLOAT NOT NULL,
    speaker_type VARCHAR(50),
    metadata JSON,
    UNIQUE KEY unique_speaker (time_stamp, user_id, session_id)
);

-- Table for storing voice sentiment metrics
CREATE TABLE voice_sentiment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    time_stamp DATETIME NOT NULL,
    user_id VARCHAR(50) NOT NULL,
    session_id VARCHAR(50) NOT NULL,
    device_id VARCHAR(50),
    location VARCHAR(100),
    sentiment_score FLOAT NOT NULL,
    sentiment_label VARCHAR(50),
    metadata JSON,
    UNIQUE KEY unique_sentiment (time_stamp, user_id, session_id)
);

-- Indexes to improve query performance
CREATE INDEX idx_timestamp_user ON talked_time (time_stamp, user_id);
CREATE INDEX idx_timestamp_user ON microphone_used (time_stamp, user_id);
CREATE INDEX idx_timestamp_user ON speaker_used (time_stamp, user_id);
CREATE INDEX idx_timestamp_user ON voice_sentiment (time_stamp, user_id);
