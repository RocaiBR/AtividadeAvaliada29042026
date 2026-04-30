from controller.usuario_controller import UsuarioController
from view.usuario_view import UsuarioView

def main():
    view = UsuarioView()
    controller = UsuarioController(view)

    while True:
        view.mostrar_menu()
        opcao = input("Opção: ")

        if opcao == "C":
            controller.criar_usuario()
        elif opcao == "L":
            controller.listar_usuarios()
        elif opcao == "T":
            break
        else:
            view.mostrar_mensagem("Opção inválida")

if __name__ == "__main__":
    main()