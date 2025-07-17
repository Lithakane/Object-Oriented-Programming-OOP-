class Sick:
    """Base class for sickness types."""
    pass


class Cancer(Sick):
    """Represents cancer treatment details."""

    def __init__(self, medication: float, scan: float):
        self.medication = medication
        self.scan = scan

    def treatment(self) -> float:
        """Calculate treatment cost based on scan value."""
        self.amount = self.medication + self.scan

        if self.scan > 600:
            print("Sorry we cannot treat you")
            return float('inf')  # Represent untreatable case
        else:
            print(f"Treatment cost: R{self.amount:.2f}")
            return self.amount


class Influenza(Sick):
    """Represents influenza treatment details."""

    def __init__(self, medication: float, consultation: float):
        self.medication = medication
        self.consultation = consultation

    def treatment(self) -> float:
        """Calculate treatment cost with possible discount."""
        if self.consultation > 600:
            self.amount = self.medication + (self.consultation * 0.98)
        else:
            self.amount = self.medication + self.consultation

        print(f"Treatment cost: R{self.amount:.2f}")
        return self.amount


# Example usage
if __name__ == "__main__":
    cancer_case = Cancer(medication=400, scan=500)
    cancer_case.treatment()

    flu_case = Influenza(medication=350, consultation=900)
    flu_case.treatment()