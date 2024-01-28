import dataclasses
import operator
import re
from dataclasses import dataclass
from typing import Callable

from utils import aoc_part


@dataclass
class Rating:
    x: int
    m: int
    a: int
    s: int


@dataclass
class Rule:
    value: str
    op: Callable[[object, object], bool] = None
    operand_L: str = None
    operand_R: int = None


@dataclass
class Workflow:
    name: str
    rules: list[Rule] = dataclasses.field(default_factory=list)


def load_input(file_name="in.txt") -> tuple[dict[str, Workflow], list[Rating]]:
    with open(file_name) as f:
        data = f.read().split("\n\n")
    workflows = {}
    for line in data[0].split("\n"):
        workflow = create_workflow(line)
        workflows[workflow.name] = workflow
    ratings = []
    for line in data[1].split("\n"):
        ratings.append(Rating(*map(int, re.findall(r"\d+", line.strip()))))

    return workflows, ratings


def create_workflow(line: str) -> Workflow:
    match = re.search(r"(\w+){(.*?)}", line.strip())
    workflow = Workflow(match.group(1))
    rules_split = match.group(2).split(",")
    workflow.rules = extract_rules(rules_split)
    return workflow


def extract_rules(rules_split: list[str]) -> list[Rule]:
    rules = []
    for rule in rules_split:
        rule_split = rule.split(":")
        if len(rule_split) == 1:
            rules.append(Rule(rule_split[0]))
        else:
            op = operator.lt if '<' in rule_split[0] else operator.gt
            operand_L = rule_split[0][0]
            operand_R = int(re.search(r"\d+", rule_split[0]).group())
            rules.append(Rule(rule_split[1], op, operand_L, operand_R))
    return rules


def resolve_workflow(workflow: Workflow, workflows: dict[str, Workflow], rating: Rating):
    for rule in workflow.rules:
        if rule.op is None or rule.op(getattr(rating, rule.operand_L), rule.operand_R):
            if rule.value == 'A':
                return True
            if rule.value == 'R':
                return False
            return resolve_workflow(workflows[rule.value], workflows, rating)


@aoc_part(1)
def solve_pt1():
    workflows, ratings = load_input()
    return sum(
        sum(dataclasses.astuple(rating))
        for rating in ratings
        if resolve_workflow(workflows['in'], workflows, rating)
    )


@dataclass
class RatingRange:
    x: tuple[int, int] = (1, 4000)
    m: tuple[int, int] = (1, 4000)
    a: tuple[int, int] = (1, 4000)
    s: tuple[int, int] = (1, 4000)

    def size(self):
        return (
                (self.x[1] - self.x[0] + 1) * (self.m[1] - self.m[0] + 1) *
                (self.a[1] - self.a[0] + 1) * (self.s[1] - self.s[0] + 1)
        )


def split(rating: RatingRange, rule: Rule) -> tuple[RatingRange, RatingRange]:
    operands = {'x': rating.x, 'm': rating.m, 'a': rating.a, 's': rating.s}
    opposite_operands = {'x': rating.x, 'm': rating.m, 'a': rating.a, 's': rating.s}

    if rule.operand_L in operands:
        if rule.op == operator.lt:  # 1,4000 and <2023
            opposite_operands[rule.operand_L] = (rule.operand_R, operands[rule.operand_L][1])  # 2023,4000
            operands[rule.operand_L] = (operands[rule.operand_L][0], rule.operand_R - 1)  # 1,2022
        else:  # 1,4000 and >2023
            opposite_operands[rule.operand_L] = (operands[rule.operand_L][0], rule.operand_R)  # 1,2023
            operands[rule.operand_L] = (rule.operand_R + 1, operands[rule.operand_L][1])  # 2024,4000

    return RatingRange(*operands.values()), RatingRange(*opposite_operands.values())


def resolve_new_rating(workflow: Workflow, workflows: dict[str, Workflow], rating: RatingRange) -> int:
    cnt = 0
    for rule in workflow.rules:
        new_rating, rating = split(rating, rule)
        if rule.value == 'A':
            cnt += new_rating.size()
        elif rule.value != 'R':
            cnt += resolve_new_rating(workflows[rule.value], workflows, new_rating)
    return cnt


@aoc_part(2)
def solve_pt2():
    workflows, _ = load_input()
    return resolve_new_rating(workflows['in'], workflows, RatingRange())


solve_pt1()
solve_pt2()
