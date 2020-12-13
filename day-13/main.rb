#!/usr/bin/env ruby

require_relative './lib/terrible_maths'

def part_1(earliest_departure_time, timetable)
    available_buses = timetable.reject { |bus| bus == 'x' }.map { |bus| bus.to_i }

    smallest_time = Float::INFINITY
    chosen_bus = nil

    available_buses.each do |bus|
        waiting_time = bus - (earliest_departure_time % bus)

        if smallest_time > waiting_time
            smallest_time = waiting_time
            chosen_bus = bus
        end
    end

    smallest_time * chosen_bus
end

def part_2(timetable)
    modulo_remainders = []

    timetable.each_with_index do |bus, index|
        if bus == 'x'
            next
        else
            bus = bus.to_i
        end

        wait_time = bus - index

        while wait_time < 0
            wait_time += bus
        end

        if wait_time == bus
            wait_time = 0
        end

        modulo_remainders << {divisor: bus, remainder: wait_time}
    end

    chinese_remainder_theorem(modulo_remainders)
end

buses = File.read(ARGV[0]).split("\n")

earliest_departure_time = buses[0].to_i
timetable = buses[1].split(',')

puts("Part 1: #{part_1(earliest_departure_time, timetable)}")
puts("Part 2: #{part_2(timetable)}")
