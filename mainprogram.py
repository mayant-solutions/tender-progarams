import dynamic, cochincorperation, smartnet

output = []
search = 'led'

output = output + dynamic.main(search)
output = output + cochincorperation.main(search)
output = output + smartnet.main(search)

print(output)
