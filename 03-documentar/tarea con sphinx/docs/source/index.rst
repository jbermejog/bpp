.. miau documentation master file, created by
   sphinx-quickstart on Sat Sep 18 11:34:12 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bienvenido a la documentacion de paquete miau!
================================
Este es un ejemplo de documentacion de un codigo que se realiza en el modulo dos de este curso, en dicho modulo teniamos que publicar un paquete

Para instalarlo deberas usar
----------------------------
>>> pip install miau

Ejemplo de uso
---------------
>>> import package.sub_package1.mod1 as modulo1
>>> import package.sub_package1.mod2 as modulo2
>>> import package.sub_package2.mod3 as modulo3
>>> import package.sub_package2.mod4 as modulo4
>>> 
>>> modulo1.printHello()
>>> modulo2.printHello()
>>> modulo3.printHello()
>>> modulo4.printHello()

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   modules



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
