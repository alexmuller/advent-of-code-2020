#!/usr/bin/env ruby

def all_possible_sums(list)
    list.combination(2).map(&:sum)
end

def part_1(xmas_encrypted_output)
    preamble_length = 25

    (0..1000).each do |start_element|
        end_element = start_element + preamble_length - 1
        input_elements = xmas_encrypted_output[start_element..end_element]
        target_element = xmas_encrypted_output[end_element+1]

        if all_possible_sums(input_elements).include? target_element
            next
        else
            return target_element
        end
    end
end

def part_2(xmas_encrypted_output, target_sum)
    contiguous_set_size = 2

    while true
        (0..1000).each do |start_element|
            end_element = start_element + contiguous_set_size - 1
            set = xmas_encrypted_output[start_element..end_element]
            if set.inject(0, :+) == target_sum
                return set.min + set.max
            end
        end

        contiguous_set_size += 1
    end
end

xmas_encrypted_output = File.read(ARGV[0]).split("\n").map { |x| x.to_i }

bad_output = part_1(xmas_encrypted_output)
puts(bad_output)
puts(part_2(xmas_encrypted_output, bad_output))
