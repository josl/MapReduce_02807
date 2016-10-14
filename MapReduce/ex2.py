from mrjob.job import MRJob
from mrjob.step import MRStep


class MRWordFrequencyCount(MRJob):

    def steps(self):  # mapper -> reducer -> reducer structure
        return [
            MRStep(mapper=self.mapper,
                   combiner=self.combiner,
                   reducer=self.reducer),  # First mapreduce
            MRStep(reducer=self.reducerEuler)  # Second reducer
        ]

    def mapper(self, _, line):  # Count all node degress
        nodes = line.split()
        yield nodes[0], 1
        yield nodes[1], 1

    def combiner(self, key, values):  # Decreases the data transfer
        yield key, sum(values)  # to the reducer. OPTIONAL!

    def reducer(self, key, values):  # Calculates degress for each node
        if sum(values) % 2 == 0:
            yield "All", True
        else:
            yield "All", False

    def reducerEuler(self, key, values):  # Test if all degress are even
        euler = str(all(list(values)))
        yield "Has Euler Tour?", euler

if __name__ == '__main__':
    MRWordFrequencyCount.run()
