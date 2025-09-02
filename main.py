from colorama import Fore, Style, init

init(autoreset=True)

def saluda(nom=None):
    """
    Affiche un message de salutation en couleur avec un emoji. Si un nom est fourni, il salue la personne.
    Exemple : saluda() -> "👋 Hello world!"
    Exemple : saluda("Marie") -> "👋 Hello Marie!"
    """
    if nom:
        print(Fore.GREEN + f"👋 Hello {nom}!" + Style.RESET_ALL)
    else:
        print(Fore.BLUE + "👋 Hello world!" + Style.RESET_ALL)

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

if __name__ == "__main__":

    saluda()