
Boarding Pass Sorter
=====================

Overview
--------

This Python code is designed to sort a stack of boarding cards for various modes of transportation and generate a sorted list of instructions on how to complete a journey from point A to point B. The boarding cards may be provided in an unordered format, and the code will sort them based on the cities of arrival and departure.

Installation
------------

This code does not require any external libraries or dependencies apart from Python itself.

Usage
-----

To use this code, follow these steps:

1. Clone the repository or download the code.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the code.
4. Run the code using Python:



```
python main.py
```



This will execute the example provided in `main.py`. You can modify this file to include your own boarding pass data.

Input Format
------------

The input for this code consists of a list of unordered boarding passes, where each boarding pass is represented as a dictionary with the following fields:

- `'transport_type'`: The type of transportation (e.g., 'train', 'bus', 'flight').
- `'departure'`: The departure city.
- `'arrival'`: The arrival city.
- `'gate'` (optional): The gate information for flights.
- `'seat'` (optional): The seat assignment.
- `'baggage_info'` (optional): Baggage information.

Example Input:
-------------

change these according to use cases inside main.py file 

```
boarding_passes = [
 {
     'transport_type': 'train',
     'departure': 'Madrid',
     'arrival': 'Barcelona',
     'seat': '45B',
 },
 {
     'transport_type': 'bus',
     'departure': 'Barcelona',
     'arrival': 'Gerona Airport',
 },

]

```


Output Format
---------
The code will generate a sorted list of instructions as strings. Each instruction will provide details on how to complete a specific leg of the journey, including transportation type, departure, arrival, gate (if applicable), seat assignment (if applicable), and baggage information (if applicable). The final instruction indicates the arrival at the final destination.


Example Output:
------
1. Take train 78A from Madrid to Barcelona. Sit in seat 45B.
2. Take the airport bus from Barcelona to Gerona Airport. No seat assignment.
3. From Gerona Airport, take flight SK455 to Stockholm. Gate 45B, seat 3A. Baggage drop at ticket counter 344.
4. From Stockholm, take flight SK22 to New York JFK. Gate 22, seat 7B. Baggage will be automatically transferred from your last leg.
5. You have arrived at your final destination.



Contact
-----
For any questions or issues, please contact Fawas at fawazzist@gmail.com.
