#!/bin/ruby

x1,v1,x2,v2 = gets.strip.split(' ')
x1 = x1.to_i
v1 = v1.to_i
x2 = x2.to_i
v2 = v2.to_i

t = (x1 - x2)/((v2 - v1)*1.0)

if t <= 0
  puts 'NO'
elsif t == t.to_i
  puts 'YES'
else
  puts 'NO'
end
