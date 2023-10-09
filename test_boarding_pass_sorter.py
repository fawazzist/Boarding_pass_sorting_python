# test_boarding_pass_sorter.py
import unittest
from Boarding_pass_sorter import BoardingPassSorter

class TestBoardingPassSorter(unittest.TestCase):
    def test_sort_boarding_passes(self):
        # Create a list of unordered boarding passes for testing
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
            {
                'transport_type': 'flight',
                'departure': 'Gerona Airport',
                'arrival': 'Stockholm',
                'gate': '45B',
                'seat': '3A',
                'baggage_info': 'Baggage drop at ticket counter 344',
            },
            {
                'transport_type': 'flight',
                'departure': 'Stockholm',
                'arrival': 'New York JFK',
                'gate': '22',
                'seat': '7B',
                'baggage_info': 'Baggage will be automatically transferred',
            },
        ]

        # Create a BoardingPassSorter instance and sort the boarding passes
        sorter = BoardingPassSorter(boarding_passes)
        sorter.sort_boarding_passes()

        # Check if the boarding passes are sorted correctly
        self.assertEqual(
            [pass_['arrival'] for pass_ in boarding_passes],
            ['Barcelona', 'Gerona Airport', 'Stockholm', 'New York JFK']
        )

    def test_generate_instructions(self):
        # Create a list of sorted boarding passes for testing
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
            {
                'transport_type': 'flight',
                'departure': 'Gerona Airport',
                'arrival': 'Stockholm',
                'gate': '45B',
                'seat': '3A',
                'baggage_info': 'Baggage drop at ticket counter 344',
            },
            {
                'transport_type': 'flight',
                'departure': 'Stockholm',
                'arrival': 'New York JFK',
                'gate': '22',
                'seat': '7B',
                'baggage_info': 'Baggage will be automatically transferred',
            },
        ]

        # Create a BoardingPassSorter instance
        sorter = BoardingPassSorter(boarding_passes)

        # Generate instructions from the sorted boarding passes
        instructions = sorter.generate_instructions()

        # Check if the generated instructions are correct
        expected_instructions = [
            "1. Take train from Madrid to Barcelona. Sit in seat 45B",
            "2. Take bus from Barcelona to Gerona Airport",
            "3. Take flight from Gerona Airport to Stockholm. Gate 45B. Sit in seat 3A. Baggage drop at ticket counter 344",
            "4. Take flight from Stockholm to New York JFK. Gate 22. Sit in seat 7B. Baggage will be automatically transferred",
            "5. You have arrived at your final destination.",
        ]

        self.assertEqual(instructions, expected_instructions)

if __name__ == '__main__':
    unittest.main()
