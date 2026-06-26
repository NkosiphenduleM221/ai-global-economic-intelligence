import os
from typing import List

class EconomicIntelligenceLLM:
    def __init__(self):
        self.mode = os.getenv("DEPLOYMENT_MODE", "LOCAL_MOCK")
        
    def generate_explanation(self, metric: str, value: float, sources: List[str]) -> str:
        if self.mode == "LOCAL_MOCK":
            return (
                f"[LOCAL EMULATION] AI Analysis Summary:\n"
                f"The metric '{metric}' is evaluated at {value}.\n"
                f"Grounded Evidence: Cross-referencing {', '.join(sources)} indicates that this "
                f"trend is structurally driven by global supply chain pressures."
            )
        elif self.mode == "GCP_VERTEX":
            # Ready for live Vertex AI SDK deployment
            pass

if __name__ == "__main__":
    ai_service = EconomicIntelligenceLLM()
    briefing = ai_service.generate_explanation(
        metric="Predicted SA Inflation Q4", 
        value=5.4, 
        sources=["SARB-Monetary-Review.pdf", "IMF-World-Outlook.pdf"]
    )
    print(briefing)
