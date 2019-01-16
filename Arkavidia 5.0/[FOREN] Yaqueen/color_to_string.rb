file = []

black_color = File.open("um_1.jpg", "rb").read
white_color = File.open("um_8.jpg", "rb").read

for number in 1..625
  file_color = File.open("um_#{number}.jpg", "rb").read

  file << 1 if file_color == black_color
  file << 0 if file_color == white_color
end

qr_code = file.each_slice(25).to_a
qr_code.each {|qr| p qr.join}
