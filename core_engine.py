import numpy as np

class LoveOSCore:
    """
    Love-OS Engine: Formalizing the rotation between 
    Potential (Imaginary) and Reality (Real).
    """
    def __init__(self, E_initial=1.0 + 0.0j, alpha=1.0, gamma=0.05):
        self.E = E_initial    # State Vector: Er + iEl
        self.alpha = alpha    # Rotation speed (Intent/Wisdom)
        self.gamma = gamma    # Decay rate (Ego/Friction)

    def process_resistance(self, R, dt):
        """
        Converts Resistance (R) into Phase Rotation (Intent/Meaning).
        R > 0 is required for charging the Imaginary Axis.
        """
        # 1. Calculate Decay (Real axis loss)
        decay = np.exp(-self.gamma * R * dt)
        
        # 2. Calculate Phase Shift (Imaginary axis gain)
        theta = self.alpha * R * dt
        rotation = np.exp(1j * theta)
        
        # 3. Apply Transformation
        self.E = self.E * decay * rotation
        return self.E

    def manifest(self, threshold_phase=np.pi/2, efficiency=1.0):
        """
        The 'Attraction' Event: Projecting Imaginary potential into Real results.
        Usually triggered when phase (arg E) reaches a critical point.
        """
        current_phase = np.angle(self.E)
        
        if current_phase >= threshold_phase:
            magnitude = np.abs(self.E)
            # Manifestation: Collapse the complex vector onto the Real Axis
            # Er = |E|, El = 0
            self.E = (magnitude * efficiency) + 0.0j
            return True, self.E
        
        return False, self.E

    def get_status(self):
        return {
            "Real_Energy (Results)": self.E.real,
            "Imaginary_Energy (Potential)": self.E.imag,
            "Phase_Angle (Alignment)": np.angle(self.E),
            "Total_Magnitude": np.abs(self.E)
        }

# Example Usage:
# architect = LoveOSCore(alpha=0.1)
# architect.process_resistance(R=50, dt=1) # High resistance leads to high charging
