import inkex
import datetime

class LockUnlockAllLayers(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.log_file = 'extension_log.txt'  # Log file path
        self.enable_logging = False  # Control logging with this variable

    def effect(self):
        if self.enable_logging:
            with open(self.log_file, 'a') as f:
                f.write(f"--- LockUnlockAllLayers ---\n")  # Function name
                f.write(f"{datetime.datetime.now()}\n")  # Timestamp

        # Select layers using XPath
        layers = self.svg.xpath('//svg:g[@inkscape:groupmode="layer"]')

        # Check if ANY layer is unlocked
        any_unlocked = any(layer.get('sodipodi:insensitive') != 'true' for layer in layers)

        # Print initial state
        self.print_to_log("Initial state:")
        for layer in layers:
            self.print_layer_info(layer)

        # Lock or unlock all layers
        for layer in layers:
            if any_unlocked:
                layer.set('sodipodi:insensitive', 'true')  # Lock
                self.print_to_log(f"Locked layer: {layer.get(inkex.addNS('label', 'inkscape'))}")
            else:
                layer.set('sodipodi:insensitive', None)  # Unlock by setting to None
                self.print_to_log(f"Unlocked layer: {layer.get(inkex.addNS('label', 'inkscape'))}")

        # Print final state
        self.print_to_log("\nFinal state:")
        for layer in layers:
            self.print_layer_info(layer)

        # Output the SVG
        self.document.write(self.options.input_file)

        if self.enable_logging:
            with open(self.log_file, 'a') as f:
                f.write('\n\n')  # Double newline at the end of the log event


    def print_to_log(self, message):
        """Prints a message to the log file if logging is enabled."""
        if self.enable_logging:
            with open(self.log_file, 'a') as f:
                f.write(message + '\n')  # Single newline for each message

    def print_layer_info(self, layer):
        """Prints information about a layer to the log file."""
        label = layer.get(inkex.addNS('label', 'inkscape'))
        insensitive = layer.get('sodipodi:insensitive')
        self.print_to_log(f"  Layer: {label}, sodipodi:insensitive={insensitive}")

if __name__ == '__main__':
    LockUnlockAllLayers().run()