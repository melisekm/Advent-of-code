from utils import aoc_part
from genetic import GeneticAlgorithm, GeneticAlgorithmConfig


@aoc_part(2)
def solve_pt2():
    best = None
    for i in range(10000):
        config = GeneticAlgorithmConfig(
            max_duration_sec=20
        )

        algo = GeneticAlgorithm(config)
        result = algo.run()
        if result.fitness < 10:
            with open('tmp.txt', "a") as f:
                f.write(str(result) + '\n')

        if not best or result.fitness < best.fitness:
            best = result
    return best


if __name__ == '__main__':
    solve_pt2()
