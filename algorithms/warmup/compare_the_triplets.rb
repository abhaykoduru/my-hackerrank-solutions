#!/bin/ruby

result = [0, 0]

a = gets.strip.split(' ')
a = a.map(&:to_i)
b = gets.strip.split(' ')
b = b.map(&:to_i)

for index in 0..2
  if a[index] > b[index] then
    result[0] += 1
  elsif a[index] < b[index] then
    result[1] += 1
  end
end

puts result.join(' ')
