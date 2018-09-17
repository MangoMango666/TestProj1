from dataclasses import dataclass

@dataclass
class Client:
    name: str
    last_name: str
    phone: str
    address : str = 'Adresse bidon'

@dataclass
class Product:
    name: str
    unitPrice: float
    ref: str

@dataclass
class InvoiceLine:
    product: Product
    units: int = 0

@dataclass
class Invoice:
    client: str
    ref: str
    vat: float=0.2
    lines: []
