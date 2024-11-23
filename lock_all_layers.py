import inkex
import datetime

class LockAllLayers(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.log_file = 'extension_log.txt'
        self.enable_logging = True

    def effect(self):
        if self.enable_logging:
            with open(self.log_file, 'a') as f:
                f.write(f"--- LockAllLayers ---\n")
                f.write(f"{datetime.datetime.now()}\n")

        # Select layers using XPath
        layers = self.svg.xpath('//svg:g[@inkscape:groupmode="layer"]')

        # Lock all layers
        for layer in layers:
            layer.set('sodipodi:insensitive', 'true')  # Lock
            self.print_to_log(f"Locked layer: {layer.get(inkex.addNS('label', 'inkscape'))}")

        # Output the SVG
        self.document.write(self.options.input_file)

        if self.enable_logging:
            with open(self.log_file, 'a') as f:
                f.write('\n\n')

    def print_to_log(self, message):
        """Prints a message to the log file if logging is enabled."""
        if self.enable_logging:
            with open(self.log_file, 'a') as f:
                f.write(message + '\n')

if __name__ == '__main__':
    LockAllLayers().run()
