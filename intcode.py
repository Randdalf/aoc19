#!/usr/bin/env python

"""Advent of Code 2019, Intcode computer"""

from inspect import signature


class OPCODE:
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    STOP = 99


class MODE:
    POSITION = 0
    IMMEDIATE = 1


def intcode_add(inputs, outputs, left, right):
    return left + right


def intcode_multiply(inputs, outputs, left, right):
    return left * right


def intcode_input(inputs, outputs):
    return inputs.pop()


def intcode_output(inputs, outputs, value):
    outputs.append(value)


class IntcodeOp:
    def __init__(slf, op):
        slf.op = op
        slf.num_inputs = len(signature(op).parameters) - 2

    def __call__(slf, *args):
        return slf.op(*args)


ops = {
    OPCODE.ADD: IntcodeOp(intcode_add),
    OPCODE.MULTIPLY: IntcodeOp(intcode_multiply),
    OPCODE.INPUT: IntcodeOp(intcode_input),
    OPCODE.OUTPUT: IntcodeOp(intcode_output)
}


class IntcodeComputer:
    def __init__(slf, memory):
        slf.memory = memory

    def execute(slf, *inputs):
        slf.outputs = []

        # Work from duplicates, to avoid mutation.
        memory = list(slf.memory)
        inputs = list(reversed(inputs))

        pc = 0
        while memory[pc] != OPCODE.STOP:
            # Reading opcode.
            head = memory[pc]
            pc += 1
            op = ops[head % 100]
            head //= 100

            # Loading parameters.
            params = []
            for i in range(op.num_inputs):
                mode = head % 10
                if mode == MODE.POSITION:
                    params.append(memory[memory[pc+i]])
                elif mode == MODE.IMMEDIATE:
                    params.append(memory[pc+i])
                head //= 10
            pc += op.num_inputs

            # Executing op.
            out = op(inputs, slf.outputs, *params)

            # Writing output.
            if out is not None:
                memory[memory[pc]] = out
                pc += 1
