"""Core functionality for glslib."""


def greeting(name: str = "World") -> str:
    """Return a greeting message.
    
    Args:
        name: The name to greet
        
    Returns:
        A formatted greeting string
    """
    return f"Hello, {name}!"
