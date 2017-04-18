#!/bin/ruby

n = gets.strip.to_i
for a0 in (0..n-1)
    grade = gets.strip.to_i
    # your code goes here
    if grade < 38 || grade % 5 == 0 || ((((grade/5 + 1) * 5) - grade) >= 3)
        puts grade
    else
        puts (grade/5 + 1) * 5
    end
end
