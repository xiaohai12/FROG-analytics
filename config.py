path_to_db = "etherpad\\var\\dirty.db"  # Path to database
editor = 'etherpad'  # Style of the database
maximum_time_between_elem_ops = 7000  # milliseconds
delay_sync = 50000  # delay to differentiate if two ops are in sync in ms
time_to_reset_day = int(288e5)  # time to reinitialize the first op of the day (8h)
time_to_reset_break = 600000  # time to reset first op after a break (10min)
length_edit = 10  # Threshold in length to differentiate a Write type from an Edit or an edit from a Deletion.
length_delete = 10  # Threshold in length to consider the op as a deletion
