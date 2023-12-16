import random

class RandomPlacementGenerator:
    @staticmethod
    def generate_random_placement(num_elements):
        placements = [(random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10)) for _ in range(num_elements)]
        print("Generated random placements:", placements)
        return placements
