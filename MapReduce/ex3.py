from mrjob.job import MRJob
from mrjob.step import MRStep
import itertools


class MRWordFrequencyCount(MRJob):

    def steps(self):  # mapper -> reducer -> reducer structure
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer),  # First mapreduce
            MRStep(reducer=self.reducer2),
            MRStep(reducer=self.reducer3),
        ]

    def mapper(self, _, line):  # Count all node degress
        nodes = line.split()
        if int(nodes[0]) < int(nodes[1]):
            yield nodes[0], [nodes[0], nodes[1]]
            yield nodes[1], [nodes[0], nodes[1]]
        else:
            yield nodes[0], [nodes[1], nodes[0]]
            yield nodes[1], [nodes[1], nodes[0]]

    def reducer(self, key, values):  # Calculates degress for each node
        myvalues = list(values)
        for edge in myvalues:
            yield edge, "edge"
        combinations = itertools.combinations(myvalues, 2)
        for pair in combinations:
            difference = sorted(
                list(set(pair[0]).symmetric_difference(set(pair[1]))))
            yield difference, "triad"

    def reducer2(self, key, values):  # Calculates degress for each node
        a = list(values)
        if "edge" in a and "triad" in a:
            count = a.count("triad")
            yield "Number of triangles: ", count

    def reducer3(self, key, values):  # Calculates degress for each node
        yield "Number of triangles:", int(sum(values) / 3.0)

if __name__ == '__main__':
    MRWordFrequencyCount.run()
