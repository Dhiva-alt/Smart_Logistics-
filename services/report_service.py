from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib import styles
import pandas as pd


def create_pdf():

    doc=SimpleDocTemplate(
        "Smart_Logistics_Report.pdf"
    )

    style=styles.getSampleStyleSheet()

    elements=[]

    elements.append(
        Paragraph(
            "Smart Logistics Report",
            style['Title']
        )
    )

    elements.append(
        Spacer(1,20)
    )

    elements.append(
        Paragraph(
        "Total Orders : 1000",
        style['Normal']
        )
    )

    elements.append(
        Paragraph(
        "Average Delivery Time : 56 mins",
        style['Normal']
        )
    )

    elements.append(
        Paragraph(
        "Best Vehicle : Bike",
        style['Normal']
        )
    )

    doc.build(elements)

    print("PDF Created")


def create_excel():

    data={

        "Metric":[
            "Orders",
            "Avg Delivery",
            "Best Vehicle"
        ],

        "Value":[
            1000,
            56,
            "Bike"
        ]

    }

    df=pd.DataFrame(data)

    df.to_excel(
        "Smart_Logistics_Report.xlsx",
        index=False
    )

    print("Excel Created")