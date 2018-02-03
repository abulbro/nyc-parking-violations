# Exploring NYC Parking Violations with MapReduce

#### The subset of the data used is available at:
https://vgc.poly.edu/~juliana/courses/BigData2017/Data/parking-violations.tar.gz

*Note that you only need the files parking-violations.csv and open-violations.csv in the tar file above. The
included file mysql-load.sql will tell you the ordering of the columns in each table (which can also be found
by reading about the data on the NYC Open Data sites).* 

## Problems explored 

### Task 1
- Write a map-reduce job that finds all parking violations that have been paid, i.e., that do not occur in open-violations.csv.
- Output: A key-value pair per line — use a “tab” to separate the key and the value, a comma and space between values — where:   
  - key = summons_number
  - values = plate_id, violation_precinct, violation_code, issue_date

Here’s a sample output with 1 key-value pair:

    1307964308 GBH2444, 74, 46, 2016-03-07

### Task 2

- Write a map-reduce job that finds the distribution of the violation types, i.e., for each violation code, the
number of violations that have this code.
- Output: A key-value pair per line — use a “tab” to separate the key and the value — where
   - key = violation_code
   - value = number of violations

Here’s a sample output with 1 key-value pair:

     46 100
     54 1000

### Task 3 

- Write a map-reduce job that finds the total and average amount due in open violations for each license
type.
- Output: A key-value pair per line — use a “tab” to separate the key and the value, a comma and space between values — where
  - key = license_type
  - value = total, average
  
where total and average are rounded to 2 decimal places.
Here’s a sample output with 1 key-value pair:

    PAS 10000.00, 55.00
    OMS 100000.00, 115.00

### Task 4

- Write a map-reduce job that computes the total number of violations for vehicles registered in the state of
NY and all other vehicles.
- Output: 2 key-value pairs with one key-value pair per line — use a “tab” to separate the key and the value
— following the key-value format below:

    NY [total number]
  
    Other [total number]
  
### Task 5 

- Write a map-reduce job that finds the vehicle that has had the greatest number of violations (assume that
plate_id and registration_state uniquely identify a vehicle).

- Output: One key-value pair — use a “tab” to separate the key and the value, a comma and space between
entries within the key/value; you should output 1 key value pair, following the key-value format below:

    plate_id, registration_state <total_number>

### Task 6

- Write a map-reduce job that finds the top-20 vehicles in terms of total violations (assume that plate id and
registration state uniquely identify a vehicle).

- Output: List of 20 key-value pairs — use a “tab” to separate the key and the value, a comma and space
between entries within the key/value — using the following format:

    plate_id, registration_state <total_number>

*Order results by decreasing number of violations.*

### Task 7

- In March 2016, the 5th, 6th, 12th, 13th, 19th, 20th, 26th, and 27th were weekend days (i.e., Sat. and Sun.).

Write a map-reduce job that, for each violation code, lists the average number of violations with that code
issued per day on weekdays and weekend days. You may hardcode “8” as the number of weekend days
and “23” as the number of weekdays in March 2016.

- Output: List of key-value pairs — use a “tab” to separate the key and the value, a comma and space
between values using the following format:

    violation_code weekend_average, week_average

*where weekend_average and week_average are rounded to 2 decimal places.*
