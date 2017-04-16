#!/bin/ruby

arr = gets.strip.split(' ').map(&:to_i)

min, max = arr.minmax

sum = 0
arr.each { |i| sum = sum + i }

puts "#{sum-max} #{sum-min}"
