from dataclasses import dataclass


@dataclass
class OCRRegion:
    text: str
    confidence: float

    x: int
    y: int
    width: int
    height: int


@dataclass
class AnalysisResult:
    text: str

    brightness: float
    complexity: float
    blur: float

    score: float