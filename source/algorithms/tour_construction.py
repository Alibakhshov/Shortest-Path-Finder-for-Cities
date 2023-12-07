from .base_algorithm import BaseAlgorithm
from operator import itemgetter
from random import randrange

class TourConstructionHeuristics(BaseAlgorithm):
    
    def closest_neighbor(self, tour, node, in_tour=False, farthest=False):
        neighbors = self.distances[node]
        current_dist = [(c, d) for c, d in neighbors.items()
                        if (c in tour if in_tour else c not in tour)]
        return sorted(current_dist, key=itemgetter(1))[-farthest]

    def add_closest_to_tour(self, tour):
        best_dist, new_tour = float('inf'), None
        for city in self.cities:
            if city in tour:
                continue
            for index in range(len(tour) - 1):
                dist = self.add(tour[index], tour[index + 1], city)
                if dist < best_dist:
                    best_dist = dist
                    new_tour = tour[:index + 1] + [city] + tour[index + 1:]
        return best_dist, new_tour

    def nearest_neighbor(self):
        city = randrange(1, self.size)
        current, tour, tour_length, tour_lengths = city, [city], 0, []
        while len(tour) != len(self.cities):
            arg_min, edge_length = self.closest_neighbor(tour, current)
            tour_length += edge_length
            tour_lengths.append(tour_length)
            tour.append(arg_min)
            current = arg_min
        tour_length += self.distances[current][city]
        tour_lengths.append(tour_length)
        intermediate_steps = [self.format_solution(tour[:i+1]) for i in range(len(tour))]
        print("\nIntermediate Steps for Nearest Neighbor:")
        for step in intermediate_steps[1:]:
            print(step)
        print("\nTour Lengths for Nearest Neighbor:")
        print(tour_lengths)
        return intermediate_steps[1:], tour_lengths

    def nearest_insertion(self, farthest=False):
        city = randrange(1, self.size)
        tour, tours = [city], []
        neighbor, length = self.closest_neighbor(tour, city, False, farthest)
        tour.append(neighbor)
        tour_length = length

        while len(tour) != len(self.cities):
            best, dist = None, 0 if farthest else float('inf')

            for candidate in self.cities:
                if candidate in tour:
                    continue

                _, length = self.closest_neighbor(tour, candidate, True)

                if (length > dist if farthest else length < dist):
                    best, dist = candidate, length

            idx, dist = None, float('inf')
            tour = tour + [tour[0]]

            for i in range(len(tour) - 1):
                add = self.add(tour[i], tour[i + 1], best) if i < len(tour) - 1 else float('inf')
                if add < dist:
                    idx, dist = i, add

            if idx is not None and idx + 1 is not None and idx < len(tour) - 1:
                tour_length += self.add(tour[idx], tour[idx + 1], best)
                tours.append(tour)
                tour.insert(idx + 1, best)
                tour = tour[:-1]

        tour_length += self.distances[tour[0]][tour[-1]]
        best_lengths = list(map(self.compute_length, tours))
        intermediate_steps = [self.format_solution(step) for step in tours]
        print("\nIntermediate Steps for Nearest Insertion:")
        for step in intermediate_steps:
            print(step)
        print("\nBest Lengths for Nearest Insertion:")
        print(best_lengths)
        return intermediate_steps, best_lengths

    def farthest_insertion(self):
        return self.nearest_insertion(farthest=True)

    def cheapest_insertion(self):
        best_tour, best_length = None, float('inf')
        best_tours, best_lengths = [], []
        city = randrange(1, self.size)
        tour, tours, tour_lengths = [city], [], []
        neighbor, length = self.closest_neighbor(tour, city)
        tour_length = length
        tour_lengths.append(length)
        tour.append(neighbor)
        while len(tour) != len(self.cities):
            length, tour = self.add_closest_to_tour(tour)
            tour_length += length
            tours.append(tour)
            tour_lengths.append(tour_length)
        tour_length += self.distances[tour[-1]][tour[0]]
        tour_lengths.append(tour_length)
        lengths = [sum(tour_lengths[:3])] + tour_lengths[3:]
        intermediate_steps = [self.format_solution(step) for step in tours]
        print("\nIntermediate Steps for Cheapest Insertion:")
        for step in intermediate_steps:
            print(step)
        print("\nLengths for Cheapest Insertion:")
        print(lengths)
        return intermediate_steps, lengths