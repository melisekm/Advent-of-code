import random
import timeit
from dataclasses import dataclass
from enum import IntEnum

from tqdm import tqdm

from utils17 import CPU, program, make_output, expected_output


@dataclass
class Chromosome:
    data: list[int]  # 16 octal digits
    value: int = None
    fitness: int = None
    output: list[int] = None

    def __post_init__(self):
        self.value = int("".join(map(str, self.data)), 8)
        self.fitness = self.fitness_fn()

    def fitness_fn(self):
        """
        Register a should be an octal number consisting of 16 octal digits.
        0o1000000000000000 <= a <= 0o7777777777777777
        """

        cpu = CPU(self.value)
        while cpu.ptr < len(program):
            opcode, operand = program[cpu.ptr], program[cpu.ptr + 1]
            fn = cpu.op_map[opcode]
            fn(operand)
            if opcode == 3 and cpu.A != 0:
                continue
            cpu.ptr += 2

        self.output = cpu.output
        output = make_output(cpu.output)
        return abs(expected_output - output)

    def __lt__(self, other):
        return self.fitness < other.fitness


class SelectionMethod(IntEnum):
    ROULETTE = 1
    RANK = 2
    TOURNAMENT = 3


@dataclass
class GeneticAlgorithmConfig:
    population_size: int = 500
    max_crossovers: int = 320
    max_mutations: int = 140
    max_random_chromosomes: int = 40
    mutation_probability: int = 40
    selection_method: SelectionMethod = SelectionMethod.ROULETTE
    max_iterations: int = -1
    max_duration_sec: int = 999


class GeneticAlgorithm:
    def __init__(self, config: GeneticAlgorithmConfig):
        self.config = config
        self.min_value = 0o1000000000000000
        self.max_value = 0o7777777777777777
        self.min_digit = 0
        self.max_digit = 7
        self.max_digits = 16
        self.runtime = 0

    def run(self) -> Chromosome:
        population = self.random_population(self.config.population_size)
        population.sort()

        init_time = timeit.default_timer()
        iteration = 0

        parent_selection = ParentSelection(self.config.selection_method)
        crossover = Crossover(self.config.max_crossovers, parent_selection)
        mutation = Mutation(self.config.max_mutations, self.config.mutation_probability)

        pbar = tqdm()

        while not self.stop(iteration, init_time):
            crossover_population = crossover.crossover(population)
            mutation_population = mutation.mutate(crossover_population)
            random_population = self.random_population(self.config.max_random_chromosomes)
            population = self.survival_of_fittest(
                population + crossover_population + mutation_population + random_population
            )
            iteration += 1
            pbar.update(1)
            pbar.set_description(f"{population[0]}")

        self.runtime = timeit.default_timer() - init_time
        return population[0]

    def stop(self, iteration, init_time):
        return iteration == self.config.max_iterations or timeit.default_timer() - init_time > self.config.max_duration_sec

    def random_population(self, size) -> list[Chromosome]:
        return [
            Chromosome(
                [random.randint(self.min_digit, self.max_digit) for _ in range(self.max_digits)]
            ) for _ in range(size)
        ]

    def survival_of_fittest(self, population: list[Chromosome]):
        return sorted(population)[:self.config.population_size]


class ParentSelection:
    def __init__(self, selection_method: SelectionMethod):
        self.selection_method = selection_method
        if self.selection_method == SelectionMethod.ROULETTE:
            self.method = self.roulette
        elif self.selection_method == SelectionMethod.RANK:
            self.method = self.rank
        elif self.selection_method == SelectionMethod.TOURNAMENT:
            self.method = self.tournament
        else:
            raise Exception(f"Unknown selection method: {self.selection_method}")

    def select(self, population: list[Chromosome]):
        return self.method(population)

    def roulette(self, population: list[Chromosome]):
        fitness_sum = sum(x.fitness for x in population)
        parents = []
        for _ in range(2):
            throw = random.uniform(0, fitness_sum)
            cnt = 0
            for chromosome in population:
                cnt += chromosome.fitness
                if cnt > throw:
                    parents.append(chromosome)
                    break
        return parents

    def rank(self, population: list[Chromosome]):
        fitness_sum = (len(population) + 1) * len(population) / 2
        parents = []
        for _ in range(2):
            throw = random.uniform(0, 1)
            cnt = 0
            for i, chromosome in enumerate(reversed(population), start=1):
                cnt += i / fitness_sum
                if cnt >= throw:
                    parents.append(chromosome)
                    break
        return parents

    def tournament(self, population: list[Chromosome]):
        parents = []
        for _ in range(2):
            first = random.choice(population)
            second = random.choice(population)
            if first < second:
                parents.append(first)
            else:
                parents.append(second)
        return parents


class Crossover:
    def __init__(self, max_crossovers: int, parent_selection: ParentSelection):
        self.max_crossovers = max_crossovers
        self.parent_selection = parent_selection

    def crossover(self, population: list[Chromosome]):
        children = []
        for _ in range(self.max_crossovers):
            parent1, parent2 = self.parent_selection.select(population)
            child = self.two_point_crossover(parent1, parent2)
            children.append(child)
        return children

    def two_point_crossover(self, parent1: Chromosome, parent2: Chromosome) -> Chromosome:
        start, end = random_part(parent1)
        child = parent1.data[:start] + parent2.data[start:end] + parent1.data[end:]
        return Chromosome(child)


class Mutation:
    def __init__(self, max_mutations, mutation_probability):
        self.max_mutations = max_mutations
        self.mutation_probability = mutation_probability

    def mutate(self, population: list[Chromosome]):
        mutated = []
        for _ in range(self.max_mutations):
            chance = random.randint(1, 100)
            if chance <= self.mutation_probability:
                parent = random.choice(population)
                child = self.swap_genes_mutation(parent)
                mutated.append(child)
        return mutated

    def swap_genes_mutation(self, parent: Chromosome):
        start, end = random_part(parent)
        child = parent.data[:start] + list(reversed(parent.data[start:end])) + parent.data[end:]
        return Chromosome(child)


def random_part(chromosome: Chromosome) -> tuple[int, int]:
    start = random.randint(0, len(chromosome.data) - 2)
    end = random.randint(start + 1, len(chromosome.data) - 1)
    return start, end
