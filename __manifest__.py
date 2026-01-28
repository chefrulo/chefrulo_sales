{
    "name": "Chefrulo Sale Customizations",
    "version": "17.0.1.0.0",
    "summary": "Show product cost on sale order lines",
    "description": """
        Sale Order Customizations
        =========================
        - Shows product cost column on quotation/sale order lines
        - Visible to internal users only
    """,
    "category": "Sales",
    "author": "Chefrulo",
    "license": "LGPL-3",
    "depends": ["sale"],
    "data": [
        "views/sale_order_views.xml",
    ],
    "installable": True,
    "auto_install": False,
}
