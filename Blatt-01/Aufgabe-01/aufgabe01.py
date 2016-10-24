
class Thermostat(object):
	
	outsideTemp = [10.0, 25.0, 30.0]
	tMin = 15.0
	tMax = 20.0
	current = 18.0

	def main(self): 
		for temp in self.outsideTemp:
			mean = (temp + self.current) / 2
			print "Outside Temperature: " + str(temp) + ", Room Temperature: " \
				+ str(self.current) + ", Mean temperature: " + str(mean)
			# Auch wenn nicht explizit in der Aufgabenstellung angegeben: Die Raumtemperatur
			# wird auf das Mittel gesetzt (ansonsten kuehlt das Thermostat bei 30 Grad 
			# Aussentemperatur auf 13 Grad Raumtemperatur)
			self.current = mean
			if mean < self.tMin:
				self.heat()
			elif mean > self.tMax:
				self.cool()
			else:
				self.idle()

	def heat(self):
		print "Heating up: " + str(self.current) + " + 5.0 C -> " + str(self.current + 5.0)
		self.current += 5.0

	def cool(self):
		print "Cooling down: " + str(self.current) + " - 5.0 C -> " + str(self.current - 5.0)
		self.current -= 5.0

	def idle(self):
		print "Idle: " + str(self.current)

if __name__ == "__main__":
	thermostat = Thermostat()
	thermostat.main()
