# Enter your code here. Read input from STDIN. Print output to STDOUT

len, shifts = gets.chomp.split.map(&:to_i)
array = gets.chomp.split.map(&:to_i)

app_shifts = shifts % len

puts array.join(' ') if (len < 2 || app_shifts == 0)

app_shifts.times do
    array = array[1,len - 1] << array[0]
end

puts array.join(' ')
