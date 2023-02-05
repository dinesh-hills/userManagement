from io import BytesIO
from reportlab.platypus import Frame, BaseDocTemplate, PageTemplate, Table, Paragraph
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from openpyxl import Workbook


# ReportLab Page Setup
def on_page(canvas, doc, pagesize=A4):
    page_num = canvas.getPageNumber()
    canvas.drawCentredString(pagesize[0] / 2, 20, str(page_num))


def on_page_landscape(canvas, doc):
    return on_page(canvas, doc, pagesize=landscape(A4))


padding = dict(leftPadding=54, rightPadding=54, topPadding=54, bottomPadding=54)
landscape_frame = Frame(0, 0, *landscape(A4), **padding)


landscape_template = PageTemplate(
    id="landscape",
    frames=landscape_frame,
    onPage=on_page_landscape,
    pagesize=landscape(A4),
)


def create_table(data):
    """
    data = [ [header1, ...], [row1, ...], [ row2, ...]]
    """
    return Table(
        data,
        style=[
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.gray),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ],
        hAlign="CENTER",
    )


def export_to_pdf(data):
    buffer = BytesIO()
    doc = BaseDocTemplate(buffer, pageTemplates=[landscape_template])
    styles = getSampleStyleSheet()
    story = [
        Paragraph("Users Data", styles["Heading1"]),
        create_table(data),
    ]
    doc.build(story)
    return buffer


# Openpyxl
def export_to_excel(data: list):
    """
    data = [ [header1, ...], [row1, ...], [ row2, ...]]
    """
    buffer = BytesIO()
    wb = Workbook(write_only=True)
    ws = wb.create_sheet()
    for row in data:
        ws.append(row)

    wb.save(buffer)
    return buffer


def generate_report(data, o_type):
    if o_type == "xlsx":
        buffer = export_to_excel(data)
        content_type = (
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        filename = "user_data.xlsx"
    else:
        buffer = export_to_pdf(data)
        content_type = "application/pdf"
        filename = "user_data.pdf"

    return (buffer, content_type, filename)
