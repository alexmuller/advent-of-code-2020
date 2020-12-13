def extended_gcd(a, b)
    previous_remainder, remainder = a, b
    previous_s, s = 1, 0
    previous_t, t = 0, 1

    while remainder != 0
        previous_remainder, (quotient, remainder) = remainder, previous_remainder.divmod(remainder)
        s, previous_s = previous_s - quotient*s, s
        t, previous_t = previous_t - quotient*t, t
    end

    {
        gcd: previous_remainder,
        bezout_coefficient: previous_s
    }
end

def inverse_modulo(a, b)
    res = extended_gcd(a, b)

    if res[:gcd] != 1
        raise 'Greatest common divisor is not 1, inverse modulo does not exist'
    end

    res[:bezout_coefficient] % b
end

def chinese_remainder_theorem(modulo_remainders)
    product = modulo_remainders.map{ |elem| elem[:divisor] }.reduce(:*)

    sum = 0

    modulo_remainders.each do |elem|
        product_except_divisor = product / elem[:divisor]
        sum += elem[:remainder] * product_except_divisor * inverse_modulo(product_except_divisor, elem[:divisor])
    end

    sum % product
end
