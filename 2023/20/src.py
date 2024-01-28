from __future__ import annotations

import dataclasses
import enum
from dataclasses import dataclass

from utils import aoc_part


class Signal(enum.IntEnum):
    LOW = 0
    HIGH = 1

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class State(enum.IntEnum):
    OFF = 0
    ON = 1

    def __invert__(self):
        return State.OFF if self == State.ON else State.ON

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


@dataclass
class Module:
    name: str
    output_modules: list[Module] = dataclasses.field(default_factory=list)

    def act(self, signal: Signal, source: Module) -> list[tuple[Module, Signal, Module]] | None:
        pass


@dataclass
class FlipFlop(Module):
    state: State = State.OFF

    def act(self, signal: Signal, source: Module) -> list[tuple[Module, Signal, Module]] | None:
        if signal == Signal.HIGH:
            return
        out_signal = Signal.HIGH if self.state == State.OFF else Signal.LOW
        for module in self.output_modules:
            yield module, out_signal, self
        self.state = ~self.state


@dataclass
class Conjunction(Module):
    input_modules: dict[Module, str] = dataclasses.field(default_factory=dict)
    memory = Signal.LOW

    def act(self, signal: Signal, source: Module) -> list[tuple[Module, Signal, Module]] | None:
        self.input_modules[source.name] = signal
        if all(signal == Signal.HIGH for signal in self.input_modules.values()):
            self.memory = Signal.LOW
        else:
            self.memory = Signal.HIGH
        for module in self.output_modules:
            yield module, self.memory, self


@dataclass
class Broadcaster(Module):
    def act(self, signal: Signal, source: Module) -> list[tuple[Module, Signal, Module]] | None:
        for module in self.output_modules:
            yield module, signal, self


def load_input(file_name="in.txt"):
    res = {}
    with open(file_name) as f:
        for line in f:
            name, targets = line.strip().split('->')
            type_ = name[0]
            targets = targets.strip().split(', ')

            name = name.strip()[1:]
            if '%' == type_:
                type_ = FlipFlop
            elif '&' == type_:
                type_ = Conjunction
            else:
                name = 'broadcaster'
                type_ = Broadcaster
            res[name] = (type_(name), targets)

    cons = []
    for name, (module, targets) in res.items():
        if isinstance(module, Conjunction):
            cons.append(module)
        for target in targets:
            if target not in res:
                target_module = Module(target)
            else:
                target_module = res[target][0]
            module.output_modules.append(target_module)

    for con_module in cons:
        for name, (module, targets) in res.items():
            if con_module.name in targets:
                con_module.input_modules[module.name] = Signal.LOW

    return res['broadcaster'][0]


def push_button(broadcaster: Broadcaster):
    queue = list(broadcaster.act(Signal.LOW, None))
    low, high = 1, 0  # broadcaster received a low signal
    while queue:
        module, signal, source = queue.pop()
        pulsed_modules = module.act(signal, source)
        if signal == Signal.LOW:
            low += 1
        else:
            high += 1
        if pulsed_modules:
            queue.extend(pulsed_modules)
    return low, high


@aoc_part(1)
def solve_pt1():
    broadcaster = load_input()
    low, high = 0, 0
    for _ in range(1000):
        l, h = push_button(broadcaster)
        low += l
        high += h
    return low * high


# @aoc_part(2)
# def solve_pt2():
#     data = load_input()
#
#     pass


solve_pt1()
# solve_pt2()
