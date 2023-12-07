#!/bin/bash

# Log files to be compressed
log_files=( "/var/log/syslog" "/var/log/wtmp" )

# Backup directory
backup_dir="/var/log/backups"

# Get timestamp
timestamp=$(date +"%Y%m%d%H%M%S")

for log_file in "${log_files[@]}"; do
  # Get original file size
  original_size=$(stat -c%s "$log_file")

  # Compress the log file
  gzip -c "$log_file" > "$backup_dir/$log_file-$timestamp.gz"

  # Clear the original log file
  truncate -s 0 "$log_file"

  # Get compressed file size
  compressed_size=$(stat -c%s "$backup_dir/$log_file-$timestamp.gz")

  # Print size comparison
  echo "Original file size: $original_size bytes"
  echo "Compressed file size: $compressed_size bytes"
  echo "Compression ratio: $(echo "scale=2; $compressed_size / $original_size" | bc)"
  echo
done

echo "Log files compressed and cleared successfully."
