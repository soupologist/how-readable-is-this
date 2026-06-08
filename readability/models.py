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
    region: OCRRegion

    foreground_luminance: float
    background_luminance: float

    contrast_ratio: float