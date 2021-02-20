PyTadoLog -- CSV logging functionality for PyTado 
=================================================

Author: Josh Gibson <josh-gibson@outlook.com>

Licence: MIT

Copyright: Josh Gibson 2020-2021

PyTadoLog is a Python module which builds off PyTado to log data from the Tado web API to a csv file.  It allows a user to track their Tado heating system for the purposes of monitoring their heating system and could enable machine learning for custom heating control.

Disclaimer
----------
I receive no help (financial or otherwise) from Tado, and have no business interest with them.  This software is provided without warranty, according to the MIT Licence, and should therefore not be used where it may endanger life, financial stakes, or cause discomfort and inconvenience to others.

Example basic usage
-------------------

    >>> from PyTadoLog import TadoLogger
    >>> TadoLogger().start()
