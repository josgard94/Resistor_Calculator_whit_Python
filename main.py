class BandCodeCalculator:

	def print_options(self):
		
		print("Este programa calcula los ohms de un resistor por su codigo de colores");
		self.NumberBand = int(input("Numero de bandas del resistor: 4, 5, 6 ?"))
		if self.NumberBand > 6 or self.NumberBand < 4:
			print("Numero de bandas incorrecto.")
			self.print_options();
		else:
			return self.NumberBand;

	def get_band_color(self):
		
		self.ColorsBand = { "negro":0, "marron":1, "rojo":2, "naranja":3, "amarrillo":4, "verde":5, "azul":6, "violeta":7, "gris":8, "blanco":9};
		print("color banda: Negro, Marron, Rojo, Naranja, Amarrillo, Verde, Azul, Violeta, Gris, Blanco");
		self.color = input(f"color de la banda:")
		self.color = self.color.lower()
		if self.color in self.ColorsBand:
			return self.ColorsBand.get(self.color)

	def get_multiplicador(self):
		
		print("color multiplicador: Negro, Marron, Rojo, Naranja, Amarrillo, Verde, Azul, Violeta, Oro, Plateado");
		self.ColorMult ={"negro":0, "marron":1, "rojo":2, "naranja":3, "amarrillo":4, "verde":5, "azul":6,"violeta":7,"oro":-1,"plateado":-2}
		self.color = input(f"color del multiplicador:")
		self.color = self.color.lower()
		if self.color in self.ColorMult:
			return self.ColorMult.get(self.color)

	def get_tolerance(self):
		
		print("Color tolerancia: Marron, Rojo, Oro, Plateado, Verde, Azul, Violeta, Gris");
		self.tolerance = {"marron":"+/- 1%", "rojo":"+/- 2%", "oro":"+/- 5%","plateado":"+/- 20%", "verde":"+/- 5%", "azul":"+/- 0.25", "violeta":"+/- 0.10", "gris":"+/- 0.05"};
		self.Ntolerance = {"marron":0.01, "rojo":0.02, "oro":0.05,"plateado":0.20, "verde":0.05, "azul":0.0025, "violeta":0.0010, "gris":0.0005};
		self.color = input(f"color de tolerancia:")
		self.color = self.color.lower()
		if self.color in self.tolerance:
			return self.tolerance.get(self.color), self.Ntolerance.get(self.color);

	def get_PPM(self):
		
		print("Color PPM: Marron, Rojo, Naranja, Amarrillo")
		self.dicPPM = {"marron":"100 ppm/K", "rojo":"50 ppm/k", "naranja":"15 ppm/k", "amarrillo":"25 ppm/k"}
		self.color = input(f"color de PPM:")
		self.color = self.color.lower()
		if self.color in self.dicPPM:
			return self.dicPPM.get(self.color)

	def Calculation_logic(self, NumberBand, Val, mul, tol, ntol):
		
		if self.NumberBand == 4:
			self.omhs = (Val[0]*10 + Val[1])*10**mul;
			self.Rango1 = self.omhs - (self.omhs * ntol);
			self.Rango2 = self.omhs + (self.omhs * ntol);

			return self.omhs, self.Rango1,self.Rango2;

		elif self.NumberBand == 5 or self.NumberBand == 6:
			self.omhs = (Val[0]*10**2 + Val[1]*10 + Val[2])*10**mul;
			self.Rango1 = self.omhs - (self.omhs * ntol);
			self.Rango2 = self.omhs + (self.omhs * ntol);

			return self.omhs, self.Rango1,self.Rango2;

	

if __name__  == '__main__':

	ObjClass = BandCodeCalculator();
	ValColorBan = [];
	NumberBand = ObjClass.print_options();

	if NumberBand == 4:

		for i in range(4):
			
			if i < 2:
				ValColorBan.append(ObjClass.get_band_color());
			elif i == 2:
				Mul = ObjClass.get_multiplicador();
			elif i == 3:
				tol,Ntol = ObjClass.get_tolerance();
		ohms1,Rango11,Rango22 = ObjClass.Calculation_logic(NumberBand, ValColorBan, Mul, tol, Ntol)
		print("valor de la resistencia: ",ohms1,"ohms tolerancia: ",tol);
		print("rango de tolerancia: [", Rango11," , ", Rango22, "] ohms");
	
	if NumberBand == 5:
		
		for i in range(5):
			
			if i < 3:
				ValColorBan.append(ObjClass.get_band_color());
			elif i == 3:
				Mul = ObjClass.get_multiplicador();
			elif i == 4:
				tol,Ntol = ObjClass.get_tolerance();
		
		ohms1,Rango11,Rango22 = ObjClass.Calculation_logic(NumberBand, ValColorBan, Mul, tol, Ntol)
		print("valor de la resistencia: ",ohms1,"ohms tolerancia: ",tol);
		print("rango de tolerancia: [", Rango11," , ", Rango22, "] ohms");
	
	if NumberBand == 6:
		
		for i in range(6):
			
			if i < 3:
				ValColorBan.append(ObjClass.get_band_color());
			elif i == 3:
				Mul = ObjClass.get_multiplicador();
			elif i == 4:
				tol,Ntol = ObjClass.get_tolerance();
			elif i == 5:
				ppm = ObjClass.get_PPM();
		ohms1,Rango11,Rango22 = ObjClass.Calculation_logic(NumberBand, ValColorBan, Mul, tol, Ntol)
		print("valor de la resistencia: ",ohms1,"ohms tolerancia: ",tol," ", ppm,);
		print("rango de tolerancia: [", Rango11," , ", Rango22, "] ohms");