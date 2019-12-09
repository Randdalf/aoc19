#!/usr/bin/env python

"""Advent of Code 2019, Intcode computer"""

from collections import defaultdict
from inspect import signature


class OPCODE:
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    OFFSET_RB = 9
    STOP = 99


class MODE:
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


def intcode_add(cpu, left, right):
    return left + right


def intcode_multiply(cpu, left, right):
    return left * right


def intcode_input(cpu):
    if len(cpu.inputs) > 0:
        cpu.waiting_for_input = False
        return cpu.inputs.pop()
    else:
        cpu.pc -= 1
        cpu.waiting_for_input = True


def intcode_output(cpu, value):
    cpu.outputs.append(value)


def intcode_jump_if_true(cpu, cond, pc):
    if cond != 0:
        cpu.pc = pc


def intcode_jump_if_false(cpu, cond, pc):
    if cond == 0:
        cpu.pc = pc


def intcode_less_than(cpu, left, right):
    return 1 if left < right else 0


def intcode_equals(cpu, left, right):
    return 1 if left == right else 0


def intcode_offset_rb(cpu, offset):
    cpu.rb += offset


class IntcodeOp:
    def __init__(slf, op):
        slf.op = op
        slf.num_inputs = len(signature(op).parameters) - 1

    def __call__(slf, *args):
        return slf.op(*args)


ops = {
    OPCODE.ADD: IntcodeOp(intcode_add),
    OPCODE.MULTIPLY: IntcodeOp(intcode_multiply),
    OPCODE.INPUT: IntcodeOp(intcode_input),
    OPCODE.OUTPUT: IntcodeOp(intcode_output),
    OPCODE.JUMP_IF_TRUE: IntcodeOp(intcode_jump_if_true),
    OPCODE.JUMP_IF_FALSE: IntcodeOp(intcode_jump_if_false),
    OPCODE.LESS_THAN: IntcodeOp(intcode_less_than),
    OPCODE.EQUALS: IntcodeOp(intcode_equals),
    OPCODE.OFFSET_RB: IntcodeOp(intcode_offset_rb)
}


class IntcodeCPU:
    def __init__(slf, memory, *inputs):
        slf.memory = defaultdict(int, enumerate(memory))
        slf.inputs = list(reversed(inputs))
        slf.outputs = []
        slf.pc = 0
        slf.rb = 0
        slf.waiting_for_input = False

    def execute(slf):
        while slf.memory[slf.pc] != OPCODE.STOP:
            # Reading opcode.
            head = slf.memory[slf.pc]
            slf.pc += 1
            op = ops[head % 100]
            head //= 100

            # Loading parameters.
            params = []
            for i in range(op.num_inputs):
                mode = head % 10
                param = slf.memory[slf.pc+i]
                if mode == MODE.POSITION:
                    params.append(slf.memory[param])
                elif mode == MODE.IMMEDIATE:
                    params.append(param)
                elif mode == MODE.RELATIVE:
                    params.append(slf.memory[slf.rb + param])
                else:
                    raise Exception('Unknown parameter mode')
                head //= 10
            slf.pc += op.num_inputs

            # Executing op.
            out = op(slf, *params)
            if slf.waiting_for_input:
                break

            # Writing output.
            if out is not None:
                mode = head % 10
                param = slf.memory[slf.pc]
                if mode == MODE.POSITION:
                    slf.memory[param] = out
                elif mode == MODE.RELATIVE:
                    slf.memory[slf.rb + param] = out
                else:
                    raise Exception('Invalid output parameter mode')
                slf.pc += 1


def intcode(memory, *inputs):
    cpu = IntcodeCPU(memory, *inputs)
    cpu.execute()
    return cpu
