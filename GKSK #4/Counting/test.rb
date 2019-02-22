full = ''
3.times do |i|
  print "Input the : "
  number = gets.chomp
  if number.include? "A"
    print "OK"
  end
  full += number
end
puts eval(full)
