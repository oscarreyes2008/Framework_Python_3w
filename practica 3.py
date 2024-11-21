class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        return f"Titular: {self.titular}, Cantidad: {self.cantidad:.2f}"

    def ingresar(self, monto):
        if monto > 0:
            self.cantidad += monto

    def retirar(self, monto):
        if monto > 0:
            self.cantidad -= monto


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def get_bonificacion(self):
        return self.bonificacion

    def esTitularValido(self, edad):
        return 18 <= edad < 25

    def retirar(self, monto, edad):
        if self.esTitularValido(edad):
            super().retirar(monto)
        else:
            print("Retiro no permitido: titular no válido.")

    def mostrar(self):
        return f"Cuenta Joven - Titular: {self.titular}, Cantidad: {self.cantidad:.2f}, Bonificación: {self.bonificacion:.2f}%"


if __name__ == "__main__":
    titular = "Pancho Villa"
    edad = 50
    cuenta_joven = CuentaJoven(titular, cantidad=10000000, bonificacion=100)

    print(cuenta_joven.mostrar())  

    cuenta_joven.retirar(100, edad)
    print(cuenta_joven.mostrar())

    edad_no_valida = 70
    cuenta_joven.retirar(100, edad_no_valida)
    print(cuenta_joven.mostrar())

