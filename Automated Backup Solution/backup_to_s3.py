#!/usr/bin/env python3
import boto3
import os
import datetime

# Configuration
SOURCE_DIR = "/home/ubuntu/data"  # directory to back up
BUCKET_NAME = "my-ubuntu-backups-12345"  # change to your bucket name
s3 = boto3.client("s3")

def backup_to_s3():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    print(f"\n--- Backup Operation: {timestamp} ---")

    if not os.path.exists(SOURCE_DIR):
        print(f"[ERROR] Source directory not found: {SOURCE_DIR}")
        return

    try:
        for root, dirs, files in os.walk(SOURCE_DIR):
            for file in files:
                local_path = os.path.join(root, file)
                # Put files inside timestamped folder in S3
                s3_path = os.path.join(f"backups/{timestamp}", os.path.relpath(local_path, SOURCE_DIR))
                s3.upload_file(local_path, BUCKET_NAME, s3_path)
                print(f"Uploaded: {s3_path}")

        print(f"[SUCCESS] Backup to S3 bucket '{BUCKET_NAME}' completed.")
    except Exception as e:
        print(f"[ERROR] Backup failed: {e}")

if __name__ == "__main__":
    backup_to_s3()

