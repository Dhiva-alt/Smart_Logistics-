from flask import Blueprint
from services.otif_service import calculate_otif

otif_bp=Blueprint(
'otif',
__name__
)

@otif_bp.route('/otif')

def otif():

    return calculate_otif()