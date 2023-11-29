#!/bin/bash
#variablesgh
date=$(date "+%D")
source_file="/var/log/syslog"
backup_dir="newsysfiledestination"

echo "Date: $date"
echo "Source file: $source_file"
echo "Destination directory: $backup_dir"
#appends date
backup_dir="${backup_dir}syslog_${date}"
mkdir -p "$backup_dir"cd
echo "Destination directory created"
#copyfile
cp "$source_file" "$backup_dir"
echo "File copied"

End
