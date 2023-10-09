# main.py
from Boarding_pass_sorter import BoardingPassSorter

def main():
    # Define your list of unordered boarding passes
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

    # Creating a BoardingPassSorter instance
    sorter = BoardingPassSorter(boarding_passes)

    # Sort the boarding passes
    sorter.sort_boarding_passes()

    # Generating and displaying instructions
    instructions = sorter.generate_instructions()

    for instruction in instructions:
        print(instruction)

if __name__ == '__main__':
    main()
