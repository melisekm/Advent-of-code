import dataclasses
import operator
import re
from dataclasses import dataclass
from typing import Union

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
    op: Union[operator.lt, operator.gt] = None
    operand_L: str = None
    operand_R: int = None


@dataclass
class Workflow:
    name: str
    rules: list[Rule] = dataclasses.field(default_factory=list)


def load_input(file_name="in.txt"):
    with open(file_name) as f:
        data = f.read().split("\n\n")
    workflows = {}
    for line in data[0].split("\n"):
        match = re.search(r"(\w+){(.*?)}", line.strip())
        workflow = Workflow(match.group(1))
        rules_split = match.group(2).split(",")
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
        workflow.rules = rules
        workflows[workflow.name] = workflow
    ratings = []
    for line in data[1].split("\n"):
        ratings.append(Rating(*map(int, re.findall(r"\d+", line.strip()))))

    return workflows, ratings


def resolve_workflow(workflow, workflows, rating):
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
        rating.x + rating.m + rating.a + rating.s
        for rating in ratings
        if resolve_workflow(workflows['in'], workflows, rating)
    )


# @aoc_part(2)
# def solve_pt2():
#     data = load_input()
#
#     pass


solve_pt1()
# solve_pt2()
