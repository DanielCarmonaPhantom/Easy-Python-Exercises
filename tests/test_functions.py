class Function_testing:

    def test_excercise_one(self, resultado, esperado):
        self.resultado = resultado
        self.esperado = esperado
        if self.resultado == self.esperado:
            print('¡Superaste la prueba!')
        else: 

            print('Test no existoso')

    def test_excercise_two(self, resultado, esperado):
        self.resultado = resultado
        self.esperado = esperado
        if self.resultado == self.esperado:
            print('¡Superaste la prueba!')
        else: 
            print(f'Test no existoso \nSe esperaba {self.esperado} y tu resultado fue {self.resultado}' )

    def test_excercise_three(self, resultado, esperado, prueba):
        self.resultado = resultado
        self.esperado = esperado
        if self.resultado == self.esperado:
            print(f'¡Superaste la prueba {prueba}!')
        else: 
            print(f'Test {prueba }no existoso \nSe esperaba {self.esperado} y tu resultado fue {self.resultado}' )


    
