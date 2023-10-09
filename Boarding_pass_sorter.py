#boarding_pass_sorter.py

class BoardingPassSorter:
    def __init__(self, boarding_passes):
        self.boarding_passes = boarding_passes

    def sort_boarding_passes(self):
        n = len(self.boarding_passes)

        for i in range(n - 1):
            for j in range(0, n - i - 1):
                # Compare the departure and arrival cities
                if self.boarding_passes[j]['arrival'] != self.boarding_passes[j + 1]['departure']:
                    # Swap the boarding passes if they are out of order
                    self.boarding_passes[j], self.boarding_passes[j + 1] = self.boarding_passes[j + 1], self.boarding_passes[j]

    def generate_instructions(self):
        instructions = []

        for i, boarding_pass in enumerate(self.boarding_passes, start=1):
            instruction = f"{i}. Take {boarding_pass['transport_type']}"

            # Add departure and arrival cities
            instruction += f" from {boarding_pass['departure']} to {boarding_pass['arrival']}"

            # Add gate information if available
            if 'gate' in boarding_pass:
                instruction += f". Gate {boarding_pass['gate']}"

            # Add seat assignment if available
            if 'seat' in boarding_pass:
                instruction += f". Sit in seat {boarding_pass['seat']}"

            # Add baggage information if available
            if 'baggage_info' in boarding_pass:
                instruction += f". {boarding_pass['baggage_info']}"

            instructions.append(instruction)

        # Add the final destination instruction
        instructions.append(f"{len(self.boarding_passes) + 1}. You have arrived at your final destination.")

        return instructions
