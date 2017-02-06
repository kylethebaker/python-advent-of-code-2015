#!/usr/bin/env python

import sys


class Circuit(object):
    def __init__(self):
        self.wires = {}

    def add_wire(self, wire):
        self.wires[wire.id] = wire

    def get_signal(self, wire_id):
        if isinstance(wire_id, int):
            return wire_id

        if wire_id not in self.wires:
            return None

        wire = self.wires[wire_id]
        if wire.signal is not None:
            return wire.signal

        wire.inputs = [self.get_signal(i) for i in wire.inputs]
        wire.evaluate()
        return wire.signal


class Wire(object):
    def __init__(self, instruction):
        self.id = None
        self.inputs = None
        self.signal = None
        self.operation = None
        self.__parse_instruction(instruction)

    def __parse_instruction(self, instruction):
        split = instruction.split()
        self.id = split.pop()
        split.pop()

        # [signal]
        if len(split) == 1:
            self.operation = "ASSIGN"
            self.inputs = [split[0]]

        # NOT [signal]
        elif len(split) == 2:
            self.operation = split[0]
            self.inputs = [split[1]]

        # [a] [operation] [b]
        elif len(split) == 3:
            self.operation = split[1]
            self.inputs = [split[0], split[2]]

        self.inputs = [int(i) if i.isdigit() else i for i in self.inputs]

    def evaluate(self):
        if not self.inputs_known():
            return False

        if self.operation == "ASSIGN":
            self.signal = self.inputs[0]
        elif self.operation == "LSHIFT":
            self.signal = self.inputs[0] << self.inputs[1]
        elif self.operation == "RSHIFT":
            self.signal = self.inputs[0] >> self.inputs[1]
        elif self.operation == "AND":
            self.signal = self.inputs[0] & self.inputs[1]
        elif self.operation == "OR":
            self.signal = self.inputs[0] | self.inputs[1]
        elif self.operation == "NOT":
            self.signal = ~self.inputs[0]
        else:
            raise ValueError("Unknown Operation")

        return True

    def inputs_known(self):
        return all([isinstance(i, int) for i in self.inputs])

circuit = Circuit()

for instruction in sys.stdin:
    circuit.add_wire(Wire(instruction))

# for part two, we override signal B to the previously found value for A,
# which was 3176.
circuit.wires["b"].signal = 3176

print(circuit.get_signal("a"))
