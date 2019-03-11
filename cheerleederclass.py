class BaseCheerer():
    """Base cheerer class."""
    def cheer() -> str:
        return "woo"

class Cheerleader(BaseCheerer):
    """Cheerleader-style cheerer class."""
    def cheer() -> str:
        return "Woo-hoo!"

class SadCheerer(BaseCheerer):
    """Depressed cheerer class."""
    def cheer() -> str:
        return "I'm sad."

def cheer(cheererclass: BaseCheerer) -> None: ## pass someting that knows how to cheer doesnt have to be jjust basecheerrer
    #type hint is the -> None
    """Uses a BaseCheerer class to cheer."""
    cheerer = cheererclass()
    print(cheererclass.cheer())


cheer(BaseCheerer)
cheer(Cheerleader)
cheer(SadCheerer)
