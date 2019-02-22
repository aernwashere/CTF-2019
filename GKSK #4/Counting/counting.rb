def main 
	full = ''

	puts "I can counting all number you input backwards"
	puts "Dont believe me?? OK lets try out"
	3.times do |i|
		print "Input the number please : " 
		number = gets.chomp

		if number.include? "sl" or number.include? "tac" or number.include? "metsys" or number.include? "sys" or number.include? "met" or number.include? "*" or number.include? "dnif" or number.include? "tsy"
			abort "eeyy dude what are you doing? why you input something like that??"
		else
			full += number
		end

	end
	
	full.reverse!
	puts eval(full)
end

print <<-'BANNER'
   
 _______  _______           _       __________________ _        _______ 
(  ____ \(  ___  )|\     /|( (    /|\__   __/\__   __/( (    /|(  ____ \
| (    \/| (   ) || )   ( ||  \  ( |   ) (      ) (   |  \  ( || (    \/
| |      | |   | || |   | ||   \ | |   | |      | |   |   \ | || |      
| |      | |   | || |   | || (\ \) |   | |      | |   | (\ \) || | ____ 
| |      | |   | || |   | || | \   |   | |      | |   | | \   || | \_  )
| (____/\| (___) || (___) || )  \  |   | |   ___) (___| )  \  || (___) |
(_______/(_______)(_______)|/    )_)   )_(   \_______/|/    )_)(_______)

by SilentMary                        



BANNER

if __FILE__ == $0
	$stdout.sync = true
	$stdout.sync = true
	main
end	
