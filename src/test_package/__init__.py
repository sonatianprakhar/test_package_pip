# src/smarttest_utils/__init__.py

def help():
    """
    Displays information about the smarttest_utils package.
    """
    info = """
    ===================================
    SmartTest Utils - Help Documentation
    ===================================

    Overview:
    SmartTest Utils provides utility functions for various tasks in the SmartTestLLM project,
    developed by TUI Group.

    Modules:
    - config_u_new: Configuration utilities, including environment-specific settings.
    - llm_utils: Language Model utilities, such as prompt generation and text processing.

    Installation:
    Ensure that pandas and any other dependencies are installed.
    Install the package with:
        pip install smarttest_utils

    Usage:
    Import the package and use its functions like this:
        import smarttest_utils
        smarttest_utils.some_function()

    For more details on each function, use Python's built-in help function:
        help(smarttest_utils.llm_utils)
    
    Author:
    Prakhar Gupta
    """
    print(info)

# Make `help` function accessible directly from `smarttest_utils`
__all__ = ['help']
