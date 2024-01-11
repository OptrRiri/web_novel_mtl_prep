class ReplacementPair:
    def __init__(
        self,  
        *trigger: str, 
        replacement: str = None
    ) -> None:
        self.replacement: str = replacement
        self.trigger: tuple[str] = trigger
