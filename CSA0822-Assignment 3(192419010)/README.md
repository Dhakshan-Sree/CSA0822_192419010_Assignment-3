# CO3 Assignment 3 – Python Programming

## Contents
- `Python_Source_Code/` contains one Python file for each of Tasks 1–7.
- `Input_Files/` is included for any separate input files.

## Task files
1. `Task1_Rainfall_Analysis.py` – weekly rainfall, extremes, dry days, moving averages and timing comparison.
2. `Task2_Bus_Stop_Tuples.py` – tuple-keyed bus-stop dictionary, aliasing, copying, unpacking, memory and indexing.
3. `Task3_Complaint_Dictionary.py` – complaint word counts, top words, district/crop summaries, dictionary and Counter comparison.
4. `Task4_Elective_Sets.py` – set operations, Venn counts, membership and intersection comparisons, duplicate removal.
5. `Task5_Cold_Storage.py` – temperature filtering, Fahrenheit conversion, alarm indices, filter/map and list/generator comparisons.
6. `Task6_Railway_Timetable.py` – timetable queries, sorting, unknown-station handling, station index and performance comparison.
7. `Task7_Contact_Merge.py` – merge contacts from two phones and a SIM, normalise phone numbers, match by phone/email, handle missing details and test larger inputs.

## Requirements
Python 3.8 or newer. No third-party packages are needed. The scripts use Python's standard library.

## Run
From the assignment folder, run each program separately:
```bash
python Python_Source_Code/Task1_Rainfall_Analysis.py
python Python_Source_Code/Task2_Bus_Stop_Tuples.py
python Python_Source_Code/Task3_Complaint_Dictionary.py
python Python_Source_Code/Task4_Elective_Sets.py
python Python_Source_Code/Task5_Cold_Storage.py
python Python_Source_Code/Task6_Railway_Timetable.py
python Python_Source_Code/Task7_Contact_Merge.py
```
Use `python3` instead of `python` if required by your system.

## Input files
No separate input files are required. Each script defines or generates its own sample data. The `Input_Files` folder is intentionally empty.

## Notes
- Performance timings vary by computer and Python version.
- `sys.getsizeof()` reports the shallow size of an object, not the full size of all referenced objects.
- Task 1 has 52 complete seven-day weeks and one remaining day.
- Task 7 uses phone numbers and email addresses as matching identifiers; real contact systems should account for recycled or shared identifiers.
