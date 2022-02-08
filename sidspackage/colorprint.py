class ColorPrint():
    def __init__(self):
        self.colors = {
            # Colors
            "red" : '\033[91m',
            "yellow" : '\033[93m',
            "green" : '\033[92m',
            "blue" : '\033[94m',
            "cyan" : '\033[96m',
            "magenta" : "\u001b[35m",
            "purple" : '\033[95m',
            "black": "\u001b[30m",
            # Effects
            "reset" : "\u001b[0m",
            "bold" : '\033[1m',
            "underline" : '\033[4m',
        }
        

    def print(self, color, text):
        color = color.lower()

        if color not in self.colors:
            return print(self.colors["bold"]+self.colors["red"]+"ERROR: "+self.colors["reset"]+self.colors['yellow']+"Color does not exist")
        color = self.colors[color]
        reset = self.colors["reset"]
        print(f"{color}{text}{reset}")

    @property
    def help(self):
        reset = self.colors["reset"]
        colors = []
        for key, value in self.colors.items():
            colors.append(value+key)
        print("\nColors List:\n"+", ".join(colors)+f"\n{reset}")