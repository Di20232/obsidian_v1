"""Popula/enriquece o banco com categorias e produtos (peças de PC e periféricos).

Idempotente: pode ser rodado várias vezes sem duplicar produtos/categorias já
existentes (identificados pelo slug). Também atualiza a imagem de TODOS os
produtos para o ícone da categoria correspondente.

Rodar com:  python -m app.seed
"""

from app import models
from app.database import Base, SessionLocal, engine
from app.utils import slugify

CATEGORIES = [
    "Processadores",
    "Placas de Vídeo",
    "Placas-Mãe",
    "Memória RAM",
    "Armazenamento",
    "Fontes",
    "Gabinetes",
    "Coolers",
    "Monitores",
    "Teclados",
    "Mouses",
    "Headsets",
]

CATEGORY_IMAGES = {
    "Processadores": "cpu.svg",
    "Placas de Vídeo": "gpu.svg",
    "Placas-Mãe": "motherboard.svg",
    "Memória RAM": "ram.svg",
    "Armazenamento": "storage.svg",
    "Fontes": "psu.svg",
    "Gabinetes": "case.svg",
    "Coolers": "cooler.svg",
    "Monitores": "monitor.svg",
    "Teclados": "keyboard.svg",
    "Mouses": "mouse.svg",
    "Headsets": "headset.svg",
}

PRODUCTS = [
    # ---------- Processadores (10) ----------
    dict(name="Processador Ryzen 5 5600", category="Processadores", brand="AMD", price=749.90, stock=25,
         specs={"nucleos": 6, "threads": 12, "clock_base": "3.5GHz", "clock_turbo": "4.4GHz", "socket": "AM4"}),
    dict(name="Processador Ryzen 7 7800X3D", category="Processadores", brand="AMD", price=2599.00, stock=12,
         specs={"nucleos": 8, "threads": 16, "clock_base": "4.2GHz", "clock_turbo": "5.0GHz", "socket": "AM5"}),
    dict(name="Processador Core i5-13400F", category="Processadores", brand="Intel", price=1199.00, stock=20,
         specs={"nucleos": 10, "threads": 16, "clock_base": "2.5GHz", "clock_turbo": "4.6GHz", "socket": "LGA1700"}),
    dict(name="Processador Core i7-13700K", category="Processadores", brand="Intel", price=2399.00, stock=10,
         specs={"nucleos": 16, "threads": 24, "clock_base": "3.4GHz", "clock_turbo": "5.4GHz", "socket": "LGA1700"}),
    dict(name="Processador Ryzen 5 7600", category="Processadores", brand="AMD", price=1349.00, stock=18,
         specs={"nucleos": 6, "threads": 12, "clock_base": "3.8GHz", "clock_turbo": "5.1GHz", "socket": "AM5"}),
    dict(name="Processador Ryzen 9 7950X", category="Processadores", brand="AMD", price=3899.00, stock=6,
         specs={"nucleos": 16, "threads": 32, "clock_base": "4.5GHz", "clock_turbo": "5.7GHz", "socket": "AM5"}),
    dict(name="Processador Core i3-13100F", category="Processadores", brand="Intel", price=699.00, stock=30,
         specs={"nucleos": 4, "threads": 8, "clock_base": "3.4GHz", "clock_turbo": "4.5GHz", "socket": "LGA1700"}),
    dict(name="Processador Core i5-14600K", category="Processadores", brand="Intel", price=1899.00, stock=14,
         specs={"nucleos": 14, "threads": 20, "clock_base": "3.5GHz", "clock_turbo": "5.3GHz", "socket": "LGA1700"}),
    dict(name="Processador Core i9-14900K", category="Processadores", brand="Intel", price=4299.00, stock=5,
         specs={"nucleos": 24, "threads": 32, "clock_base": "3.2GHz", "clock_turbo": "6.0GHz", "socket": "LGA1700"}),
    dict(name="Processador Ryzen 7 5800X3D", category="Processadores", brand="AMD", price=1799.00, stock=11,
         specs={"nucleos": 8, "threads": 16, "clock_base": "3.4GHz", "clock_turbo": "4.5GHz", "socket": "AM4"}),

    # ---------- Placas de Vídeo (10) ----------
    dict(name="Placa de Vídeo RTX 4060 8GB", category="Placas de Vídeo", brand="NVIDIA", price=2199.00, stock=15,
         specs={"memoria": "8GB GDDR6", "interface": "PCIe 4.0", "saidas": "3x DP, 1x HDMI"}),
    dict(name="Placa de Vídeo RTX 4070 Super 12GB", category="Placas de Vídeo", brand="NVIDIA", price=4599.00, stock=8,
         specs={"memoria": "12GB GDDR6X", "interface": "PCIe 4.0", "saidas": "3x DP, 1x HDMI"}),
    dict(name="Placa de Vídeo RX 7600 8GB", category="Placas de Vídeo", brand="AMD", price=1899.00, stock=14,
         specs={"memoria": "8GB GDDR6", "interface": "PCIe 4.0", "saidas": "3x DP, 1x HDMI"}),
    dict(name="Placa de Vídeo RTX 4090 24GB", category="Placas de Vídeo", brand="NVIDIA", price=11999.00, stock=4,
         specs={"memoria": "24GB GDDR6X", "interface": "PCIe 4.0", "saidas": "3x DP, 1x HDMI"}),
    dict(name="Placa de Vídeo RTX 4080 Super 16GB", category="Placas de Vídeo", brand="NVIDIA", price=7499.00, stock=6,
         specs={"memoria": "16GB GDDR6X", "interface": "PCIe 4.0", "saidas": "3x DP, 1x HDMI"}),
    dict(name="Placa de Vídeo RTX 4060 Ti 16GB", category="Placas de Vídeo", brand="NVIDIA", price=3199.00, stock=10,
         specs={"memoria": "16GB GDDR6", "interface": "PCIe 4.0", "saidas": "3x DP, 1x HDMI"}),
    dict(name="Placa de Vídeo RX 7800 XT 16GB", category="Placas de Vídeo", brand="AMD", price=3699.00, stock=9,
         specs={"memoria": "16GB GDDR6", "interface": "PCIe 4.0", "saidas": "3x DP, 1x HDMI"}),
    dict(name="Placa de Vídeo RX 6600 8GB", category="Placas de Vídeo", brand="AMD", price=1299.00, stock=20,
         specs={"memoria": "8GB GDDR6", "interface": "PCIe 4.0", "saidas": "3x DP, 1x HDMI"}),
    dict(name="Placa de Vídeo RTX 4070 Ti 12GB", category="Placas de Vídeo", brand="NVIDIA", price=5299.00, stock=7,
         specs={"memoria": "12GB GDDR6X", "interface": "PCIe 4.0", "saidas": "3x DP, 1x HDMI"}),
    dict(name="Placa de Vídeo Arc A750 8GB", category="Placas de Vídeo", brand="Intel", price=1599.00, stock=13,
         specs={"memoria": "8GB GDDR6", "interface": "PCIe 4.0", "saidas": "3x DP, 1x HDMI"}),

    # ---------- Placas-Mãe (10) ----------
    dict(name="Placa-Mãe B550M Gaming", category="Placas-Mãe", brand="ASUS", price=799.00, stock=18,
         specs={"socket": "AM4", "chipset": "B550", "formato": "Micro-ATX", "memoria": "DDR4"}),
    dict(name="Placa-Mãe B650 Gaming Plus", category="Placas-Mãe", brand="MSI", price=1199.00, stock=16,
         specs={"socket": "AM5", "chipset": "B650", "formato": "ATX", "memoria": "DDR5"}),
    dict(name="Placa-Mãe Z790 AORUS Elite", category="Placas-Mãe", brand="Gigabyte", price=1899.00, stock=9,
         specs={"socket": "LGA1700", "chipset": "Z790", "formato": "ATX", "memoria": "DDR5"}),
    dict(name="Placa-Mãe A520M-K", category="Placas-Mãe", brand="ASUS", price=449.00, stock=28,
         specs={"socket": "AM4", "chipset": "A520", "formato": "Micro-ATX", "memoria": "DDR4"}),
    dict(name="Placa-Mãe X670E AORUS Master", category="Placas-Mãe", brand="Gigabyte", price=3299.00, stock=5,
         specs={"socket": "AM5", "chipset": "X670E", "formato": "ATX", "memoria": "DDR5"}),
    dict(name="Placa-Mãe H610M-H", category="Placas-Mãe", brand="Gigabyte", price=549.00, stock=24,
         specs={"socket": "LGA1700", "chipset": "H610", "formato": "Micro-ATX", "memoria": "DDR4"}),
    dict(name="Placa-Mãe Z690-A Pro", category="Placas-Mãe", brand="MSI", price=1599.00, stock=11,
         specs={"socket": "LGA1700", "chipset": "Z690", "formato": "ATX", "memoria": "DDR4"}),
    dict(name="Placa-Mãe B760M Gaming", category="Placas-Mãe", brand="ASUS", price=899.00, stock=17,
         specs={"socket": "LGA1700", "chipset": "B760", "formato": "Micro-ATX", "memoria": "DDR5"}),
    dict(name="Placa-Mãe X570 Gaming Plus", category="Placas-Mãe", brand="MSI", price=1099.00, stock=13,
         specs={"socket": "AM4", "chipset": "X570", "formato": "ATX", "memoria": "DDR4"}),
    dict(name="Placa-Mãe A620M Gaming", category="Placas-Mãe", brand="Gigabyte", price=699.00, stock=19,
         specs={"socket": "AM5", "chipset": "A620", "formato": "Micro-ATX", "memoria": "DDR5"}),

    # ---------- Memória RAM (10) ----------
    dict(name="Memória RAM 16GB DDR4 3200MHz", category="Memória RAM", brand="Corsair", price=249.90, stock=40,
         specs={"capacidade": "16GB (2x8GB)", "tipo": "DDR4", "frequencia": "3200MHz"}),
    dict(name="Memória RAM 32GB DDR5 6000MHz", category="Memória RAM", brand="Kingston", price=899.00, stock=22,
         specs={"capacidade": "32GB (2x16GB)", "tipo": "DDR5", "frequencia": "6000MHz"}),
    dict(name="Memória RAM 16GB DDR5 5600MHz RGB", category="Memória RAM", brand="G.Skill", price=549.00, stock=30,
         specs={"capacidade": "16GB (2x8GB)", "tipo": "DDR5", "frequencia": "5600MHz", "rgb": True}),
    dict(name="Memória RAM 8GB DDR4 3200MHz", category="Memória RAM", brand="Kingston", price=139.00, stock=50,
         specs={"capacidade": "8GB (1x8GB)", "tipo": "DDR4", "frequencia": "3200MHz"}),
    dict(name="Memória RAM 32GB DDR4 3600MHz", category="Memória RAM", brand="Corsair", price=599.00, stock=25,
         specs={"capacidade": "32GB (2x16GB)", "tipo": "DDR4", "frequencia": "3600MHz"}),
    dict(name="Memória RAM 64GB DDR5 6000MHz", category="Memória RAM", brand="G.Skill", price=1799.00, stock=8,
         specs={"capacidade": "64GB (2x32GB)", "tipo": "DDR5", "frequencia": "6000MHz"}),
    dict(name="Memória RAM 16GB DDR4 3600MHz RGB", category="Memória RAM", brand="HyperX", price=379.00, stock=27,
         specs={"capacidade": "16GB (2x8GB)", "tipo": "DDR4", "frequencia": "3600MHz", "rgb": True}),
    dict(name="Memória RAM 8GB DDR5 4800MHz", category="Memória RAM", brand="Kingston", price=229.00, stock=35,
         specs={"capacidade": "8GB (1x8GB)", "tipo": "DDR5", "frequencia": "4800MHz"}),
    dict(name="Memória RAM 32GB DDR5 5200MHz RGB", category="Memória RAM", brand="Corsair", price=999.00, stock=16,
         specs={"capacidade": "32GB (2x16GB)", "tipo": "DDR5", "frequencia": "5200MHz", "rgb": True}),
    dict(name="Memória RAM 16GB DDR3 1600MHz", category="Memória RAM", brand="Kingston", price=159.00, stock=20,
         specs={"capacidade": "16GB (2x8GB)", "tipo": "DDR3", "frequencia": "1600MHz"}),

    # ---------- Armazenamento (10) ----------
    dict(name="SSD NVMe 1TB PCIe 4.0", category="Armazenamento", brand="WD", price=449.00, stock=35,
         specs={"capacidade": "1TB", "interface": "NVMe PCIe 4.0", "leitura": "7000MB/s"}),
    dict(name="SSD SATA 480GB", category="Armazenamento", brand="Kingston", price=179.00, stock=50,
         specs={"capacidade": "480GB", "interface": "SATA III", "leitura": "550MB/s"}),
    dict(name="HD 2TB 7200RPM", category="Armazenamento", brand="Seagate", price=389.00, stock=28,
         specs={"capacidade": "2TB", "interface": "SATA III", "rpm": 7200}),
    dict(name="SSD NVMe 2TB PCIe 4.0", category="Armazenamento", brand="Samsung", price=899.00, stock=17,
         specs={"capacidade": "2TB", "interface": "NVMe PCIe 4.0", "leitura": "7450MB/s"}),
    dict(name="HD 4TB 5400RPM", category="Armazenamento", brand="WD", price=649.00, stock=15,
         specs={"capacidade": "4TB", "interface": "SATA III", "rpm": 5400}),
    dict(name="SSD NVMe 500GB PCIe 3.0", category="Armazenamento", brand="Kingston", price=249.00, stock=40,
         specs={"capacidade": "500GB", "interface": "NVMe PCIe 3.0", "leitura": "3500MB/s"}),
    dict(name="SSD SATA 1TB", category="Armazenamento", brand="Crucial", price=339.00, stock=30,
         specs={"capacidade": "1TB", "interface": "SATA III", "leitura": "560MB/s"}),
    dict(name="SSD NVMe 4TB PCIe 4.0", category="Armazenamento", brand="Samsung", price=1899.00, stock=6,
         specs={"capacidade": "4TB", "interface": "NVMe PCIe 4.0", "leitura": "7000MB/s"}),
    dict(name="HD 1TB 7200RPM", category="Armazenamento", brand="Seagate", price=259.00, stock=32,
         specs={"capacidade": "1TB", "interface": "SATA III", "rpm": 7200}),
    dict(name="SSD NVMe 256GB PCIe 3.0", category="Armazenamento", brand="WD", price=169.00, stock=45,
         specs={"capacidade": "256GB", "interface": "NVMe PCIe 3.0", "leitura": "2400MB/s"}),

    # ---------- Fontes (10) ----------
    dict(name="Fonte 650W 80 Plus Bronze", category="Fontes", brand="Corsair", price=399.00, stock=26,
         specs={"potencia": "650W", "certificacao": "80 Plus Bronze", "modular": "Semi"}),
    dict(name="Fonte 750W 80 Plus Gold Modular", category="Fontes", brand="EVGA", price=649.00, stock=19,
         specs={"potencia": "750W", "certificacao": "80 Plus Gold", "modular": "Total"}),
    dict(name="Fonte 1000W 80 Plus Platinum", category="Fontes", brand="Corsair", price=1299.00, stock=7,
         specs={"potencia": "1000W", "certificacao": "80 Plus Platinum", "modular": "Total"}),
    dict(name="Fonte 500W 80 Plus White", category="Fontes", brand="Corsair", price=249.00, stock=33,
         specs={"potencia": "500W", "certificacao": "80 Plus White", "modular": "Não"}),
    dict(name="Fonte 550W 80 Plus Bronze", category="Fontes", brand="EVGA", price=329.00, stock=28,
         specs={"potencia": "550W", "certificacao": "80 Plus Bronze", "modular": "Não"}),
    dict(name="Fonte 850W 80 Plus Gold Modular", category="Fontes", brand="Corsair", price=899.00, stock=14,
         specs={"potencia": "850W", "certificacao": "80 Plus Gold", "modular": "Total"}),
    dict(name="Fonte 1200W 80 Plus Platinum", category="Fontes", brand="EVGA", price=1899.00, stock=4,
         specs={"potencia": "1200W", "certificacao": "80 Plus Platinum", "modular": "Total"}),
    dict(name="Fonte 450W Sem Certificação", category="Fontes", brand="Redragon", price=159.00, stock=38,
         specs={"potencia": "450W", "certificacao": "Nenhuma", "modular": "Não"}),
    dict(name="Fonte 700W 80 Plus Bronze Semi-Modular", category="Fontes", brand="MSI", price=479.00, stock=22,
         specs={"potencia": "700W", "certificacao": "80 Plus Bronze", "modular": "Semi"}),
    dict(name="Fonte 750W 80 Plus Silver", category="Fontes", brand="Cooler Master", price=549.00, stock=17,
         specs={"potencia": "750W", "certificacao": "80 Plus Silver", "modular": "Semi"}),

    # ---------- Gabinetes (10) ----------
    dict(name="Gabinete Gamer Mid Tower RGB", category="Gabinetes", brand="Redragon", price=299.00, stock=24,
         specs={"formato": "Mid Tower", "vidro_lateral": True, "fans_inclusos": 3}),
    dict(name="Gabinete Compacto Micro-ATX", category="Gabinetes", brand="Cooler Master", price=349.00, stock=15,
         specs={"formato": "Micro-ATX", "vidro_lateral": True, "fans_inclusos": 2}),
    dict(name="Gabinete Full Tower", category="Gabinetes", brand="NZXT", price=899.00, stock=6,
         specs={"formato": "Full Tower", "vidro_lateral": True, "fans_inclusos": 4}),
    dict(name="Gabinete Mini-ITX", category="Gabinetes", brand="Cooler Master", price=549.00, stock=10,
         specs={"formato": "Mini-ITX", "vidro_lateral": True, "fans_inclusos": 1}),
    dict(name="Gabinete Mid Tower Econômico", category="Gabinetes", brand="Redragon", price=189.00, stock=30,
         specs={"formato": "Mid Tower", "vidro_lateral": False, "fans_inclusos": 1}),
    dict(name="Gabinete Full Tower RGB", category="Gabinetes", brand="NZXT", price=1199.00, stock=5,
         specs={"formato": "Full Tower", "vidro_lateral": True, "fans_inclusos": 6}),
    dict(name="Gabinete Mid Tower Branco", category="Gabinetes", brand="Cooler Master", price=419.00, stock=18,
         specs={"formato": "Mid Tower", "vidro_lateral": True, "fans_inclusos": 3}),
    dict(name="Gabinete ATX com 6 Fans", category="Gabinetes", brand="Lian Li", price=999.00, stock=7,
         specs={"formato": "ATX", "vidro_lateral": True, "fans_inclusos": 6}),
    dict(name="Gabinete Micro-ATX RGB", category="Gabinetes", brand="Redragon", price=259.00, stock=26,
         specs={"formato": "Micro-ATX", "vidro_lateral": True, "fans_inclusos": 2}),
    dict(name="Gabinete Full Tower Vidro Temperado", category="Gabinetes", brand="Corsair", price=1099.00, stock=6,
         specs={"formato": "Full Tower", "vidro_lateral": True, "fans_inclusos": 3}),

    # ---------- Coolers (10) ----------
    dict(name="Water Cooler 240mm RGB", category="Coolers", brand="Cooler Master", price=549.00, stock=13,
         specs={"tipo": "Líquido (AIO)", "radiador": "240mm", "rgb": True}),
    dict(name="Cooler Box para CPU", category="Coolers", brand="Deepcool", price=129.00, stock=45,
         specs={"tipo": "Ar", "compatibilidade": "AM4/AM5/LGA1700"}),
    dict(name="Water Cooler 360mm RGB", category="Coolers", brand="NZXT", price=899.00, stock=8,
         specs={"tipo": "Líquido (AIO)", "radiador": "360mm", "rgb": True}),
    dict(name="Cooler Box Intel Original", category="Coolers", brand="Intel", price=79.00, stock=50,
         specs={"tipo": "Ar", "compatibilidade": "LGA1700"}),
    dict(name="Water Cooler 120mm", category="Coolers", brand="Cooler Master", price=329.00, stock=20,
         specs={"tipo": "Líquido (AIO)", "radiador": "120mm", "rgb": False}),
    dict(name="Water Cooler 280mm RGB", category="Coolers", brand="Corsair", price=699.00, stock=11,
         specs={"tipo": "Líquido (AIO)", "radiador": "280mm", "rgb": True}),
    dict(name="Cooler a Ar Duplo Fan", category="Coolers", brand="Deepcool", price=249.00, stock=24,
         specs={"tipo": "Ar", "compatibilidade": "AM4/AM5/LGA1700", "fans": 2}),
    dict(name="Cooler a Ar Single Tower", category="Coolers", brand="Cooler Master", price=179.00, stock=28,
         specs={"tipo": "Ar", "compatibilidade": "AM4/AM5/LGA1700", "fans": 1}),
    dict(name="Water Cooler 360mm Branco", category="Coolers", brand="NZXT", price=949.00, stock=6,
         specs={"tipo": "Líquido (AIO)", "radiador": "360mm", "rgb": True}),
    dict(name="Cooler a Ar Low Profile", category="Coolers", brand="Deepcool", price=159.00, stock=19,
         specs={"tipo": "Ar", "compatibilidade": "AM4/LGA1700", "fans": 1}),

    # ---------- Monitores (10) ----------
    dict(name="Monitor Gamer 24' 144Hz Full HD", category="Monitores", brand="AOC", price=899.00, stock=22,
         specs={"tamanho": "24 polegadas", "resolucao": "1920x1080", "taxa_atualizacao": "144Hz", "painel": "VA"}),
    dict(name="Monitor Gamer 27' 165Hz QHD", category="Monitores", brand="LG", price=1799.00, stock=14,
         specs={"tamanho": "27 polegadas", "resolucao": "2560x1440", "taxa_atualizacao": "165Hz", "painel": "IPS"}),
    dict(name="Monitor Ultrawide 34' 144Hz", category="Monitores", brand="Samsung", price=2999.00, stock=6,
         specs={"tamanho": "34 polegadas", "resolucao": "3440x1440", "taxa_atualizacao": "144Hz", "painel": "VA"}),
    dict(name="Monitor 21.5' Full HD 75Hz", category="Monitores", brand="AOC", price=649.00, stock=28,
         specs={"tamanho": "21.5 polegadas", "resolucao": "1920x1080", "taxa_atualizacao": "75Hz", "painel": "IPS"}),
    dict(name="Monitor Gamer 24' 240Hz Full HD", category="Monitores", brand="BenQ", price=1699.00, stock=9,
         specs={"tamanho": "24 polegadas", "resolucao": "1920x1080", "taxa_atualizacao": "240Hz", "painel": "IPS"}),
    dict(name="Monitor 27' 4K 60Hz", category="Monitores", brand="LG", price=2399.00, stock=8,
         specs={"tamanho": "27 polegadas", "resolucao": "3840x2160", "taxa_atualizacao": "60Hz", "painel": "IPS"}),
    dict(name="Monitor Curvo 29' Ultrawide 100Hz", category="Monitores", brand="Samsung", price=1899.00, stock=10,
         specs={"tamanho": "29 polegadas", "resolucao": "2560x1080", "taxa_atualizacao": "100Hz", "painel": "VA"}),
    dict(name="Monitor Gamer 32' 165Hz QHD", category="Monitores", brand="AOC", price=2199.00, stock=7,
         specs={"tamanho": "32 polegadas", "resolucao": "2560x1440", "taxa_atualizacao": "165Hz", "painel": "VA"}),
    dict(name="Monitor 24' IPS 100Hz", category="Monitores", brand="LG", price=999.00, stock=18,
         specs={"tamanho": "24 polegadas", "resolucao": "1920x1080", "taxa_atualizacao": "100Hz", "painel": "IPS"}),
    dict(name="Monitor Curvo 34' 165Hz", category="Monitores", brand="Samsung", price=3499.00, stock=5,
         specs={"tamanho": "34 polegadas", "resolucao": "3440x1440", "taxa_atualizacao": "165Hz", "painel": "VA"}),

    # ---------- Teclados (10) ----------
    dict(name="Teclado Mecânico RGB Switch Red", category="Teclados", brand="Redragon", price=249.00, stock=38,
         specs={"tipo": "Mecânico", "switch": "Red", "layout": "ABNT2", "rgb": True}),
    dict(name="Teclado Mecânico Wireless", category="Teclados", brand="Logitech", price=699.00, stock=16,
         specs={"tipo": "Mecânico", "switch": "Tátil", "conexao": "Wireless/Bluetooth"}),
    dict(name="Teclado Membrana Gamer", category="Teclados", brand="HyperX", price=179.00, stock=42,
         specs={"tipo": "Membrana", "layout": "ABNT2", "rgb": True}),
    dict(name="Teclado Mecânico Switch Blue", category="Teclados", brand="HyperX", price=329.00, stock=25,
         specs={"tipo": "Mecânico", "switch": "Blue", "layout": "ABNT2", "rgb": True}),
    dict(name="Teclado Mecânico Compacto 60%", category="Teclados", brand="Redragon", price=219.00, stock=30,
         specs={"tipo": "Mecânico", "switch": "Red", "layout": "60%", "rgb": True}),
    dict(name="Teclado Sem Fio Slim", category="Teclados", brand="Logitech", price=249.00, stock=33,
         specs={"tipo": "Membrana", "conexao": "Wireless", "layout": "ABNT2"}),
    dict(name="Teclado Mecânico Switch Brown", category="Teclados", brand="Corsair", price=549.00, stock=17,
         specs={"tipo": "Mecânico", "switch": "Brown", "layout": "ABNT2", "rgb": True}),
    dict(name="Teclado Gamer TKL RGB", category="Teclados", brand="HyperX", price=429.00, stock=21,
         specs={"tipo": "Mecânico", "switch": "Red", "layout": "TKL", "rgb": True}),
    dict(name="Teclado ABNT2 Office", category="Teclados", brand="Logitech", price=89.00, stock=60,
         specs={"tipo": "Membrana", "layout": "ABNT2", "rgb": False}),
    dict(name="Teclado Mecânico Hot-swappable", category="Teclados", brand="Redragon", price=379.00, stock=15,
         specs={"tipo": "Mecânico", "switch": "Hot-swap", "layout": "TKL", "rgb": True}),

    # ---------- Mouses (10) ----------
    dict(name="Mouse Gamer 12000 DPI", category="Mouses", brand="Logitech", price=249.00, stock=48,
         specs={"dpi": 12000, "botoes": 6, "conexao": "USB"}),
    dict(name="Mouse Sem Fio Ultraleve", category="Mouses", brand="Razer", price=449.00, stock=21,
         specs={"dpi": 20000, "botoes": 5, "conexao": "Wireless", "peso": "58g"}),
    dict(name="Mouse Gamer RGB 7200 DPI", category="Mouses", brand="Redragon", price=129.00, stock=55,
         specs={"dpi": 7200, "botoes": 7, "conexao": "USB", "rgb": True}),
    dict(name="Mouse Office Simples", category="Mouses", brand="Logitech", price=49.00, stock=70,
         specs={"dpi": 1000, "botoes": 3, "conexao": "USB"}),
    dict(name="Mouse Vertical Ergonômico", category="Mouses", brand="Logitech", price=299.00, stock=20,
         specs={"dpi": 4000, "botoes": 6, "conexao": "Wireless"}),
    dict(name="Mouse Gamer 16000 DPI RGB", category="Mouses", brand="Corsair", price=349.00, stock=24,
         specs={"dpi": 16000, "botoes": 8, "conexao": "USB", "rgb": True}),
    dict(name="Mouse Sem Fio Silencioso", category="Mouses", brand="Logitech", price=179.00, stock=32,
         specs={"dpi": 4000, "botoes": 5, "conexao": "Wireless", "silencioso": True}),
    dict(name="Mouse Gamer Ultraleve 63g", category="Mouses", brand="Razer", price=549.00, stock=13,
         specs={"dpi": 26000, "botoes": 5, "conexao": "Wireless", "peso": "63g"}),
    dict(name="Mouse Gamer com Fio 26000 DPI", category="Mouses", brand="SteelSeries", price=399.00, stock=18,
         specs={"dpi": 26000, "botoes": 6, "conexao": "USB"}),
    dict(name="Mouse Trackball", category="Mouses", brand="Logitech", price=449.00, stock=9,
         specs={"dpi": 4000, "botoes": 8, "conexao": "Wireless", "tipo": "Trackball"}),

    # ---------- Headsets (10) ----------
    dict(name="Headset Gamer 7.1 Surround", category="Headsets", brand="HyperX", price=349.00, stock=30,
         specs={"som": "7.1 Surround", "microfone": "Removível", "conexao": "USB/P2"}),
    dict(name="Headset Sem Fio com Cancelamento de Ruído", category="Headsets", brand="SteelSeries", price=899.00, stock=11,
         specs={"som": "Estéreo", "microfone": "Integrado", "conexao": "Wireless 2.4GHz", "anc": True}),
    dict(name="Headset Gamer RGB", category="Headsets", brand="Redragon", price=199.00, stock=40,
         specs={"som": "Estéreo", "microfone": "Flexível", "conexao": "P2", "rgb": True}),
    dict(name="Headset Office com Microfone", category="Headsets", brand="Logitech", price=99.00, stock=55,
         specs={"som": "Estéreo", "microfone": "Fixo", "conexao": "P2"}),
    dict(name="Headset Gamer Wireless", category="Headsets", brand="Razer", price=799.00, stock=14,
         specs={"som": "7.1 Surround", "microfone": "Removível", "conexao": "Wireless 2.4GHz"}),
    dict(name="Headset Gamer 7.1 USB RGB", category="Headsets", brand="Corsair", price=549.00, stock=19,
         specs={"som": "7.1 Surround", "microfone": "Removível", "conexao": "USB", "rgb": True}),
    dict(name="Headset Bluetooth", category="Headsets", brand="JBL", price=349.00, stock=26,
         specs={"som": "Estéreo", "microfone": "Integrado", "conexao": "Bluetooth"}),
    dict(name="Headset Gamer com Cancelamento de Ruído", category="Headsets", brand="HyperX", price=999.00, stock=8,
         specs={"som": "Estéreo", "microfone": "Removível", "conexao": "Wireless 2.4GHz", "anc": True}),
    dict(name="Headset In-ear Gamer", category="Headsets", brand="Razer", price=249.00, stock=23,
         specs={"som": "Estéreo", "microfone": "Embutido no cabo", "conexao": "P2"}),
    dict(name="Headset Gamer PS5/PC", category="Headsets", brand="SteelSeries", price=649.00, stock=16,
         specs={"som": "7.1 Surround", "microfone": "Removível", "conexao": "USB/P2"}),
]


def run():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        category_map: dict[str, models.Category] = {}
        for name in CATEGORIES:
            category = db.query(models.Category).filter_by(name=name).first()
            if not category:
                category = models.Category(name=name, slug=slugify(name))
                db.add(category)
                db.flush()
            category_map[name] = category

        created = 0
        for p in PRODUCTS:
            slug = slugify(f"{p['name']}-{p['brand']}")
            if db.query(models.Product).filter_by(slug=slug).first():
                continue
            category = category_map[p["category"]]
            product = models.Product(
                name=p["name"],
                slug=slug,
                description=f"{p['name']} da {p['brand']}. Ideal para quem busca desempenho e custo-benefício em {category.name.lower()}.",
                brand=p["brand"],
                price=p["price"],
                stock=p["stock"],
                image_url=f"/products/{CATEGORY_IMAGES[p['category']]}",
                specs=p["specs"],
                category_id=category.id,
            )
            db.add(product)
            created += 1
        db.flush()

        updated = 0
        for product in db.query(models.Product).all():
            image_url = f"/products/{CATEGORY_IMAGES[product.category.name]}"
            if product.image_url != image_url:
                product.image_url = image_url
                updated += 1

        db.commit()
        total = db.query(models.Product).count()
        print(f"Seed concluído: {created} produto(s) novo(s), {updated} imagem(ns) atualizada(s), {total} produtos no total.")
    finally:
        db.close()


if __name__ == "__main__":
    run()
