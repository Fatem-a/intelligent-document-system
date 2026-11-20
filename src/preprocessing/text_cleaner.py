def clean_text(text: str) -> str:
    """
        Remove unnecessary whitespace from text.
    """

    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    
    cleaned_text = " ".join(text.split())

    return cleaned_text
