from flask import Blueprint, send_file
from services.report_service import *

report_bp = Blueprint(
    'report',
    __name__
)

@report_bp.route('/generate-report')
def report():

    create_pdf()
    create_excel()

    return {
        "message":"Reports generated successfully"
    }


@report_bp.route('/download')
def download():

    return send_file(
        "Smart_Logistics_Report.pdf",
        as_attachment=True
    )