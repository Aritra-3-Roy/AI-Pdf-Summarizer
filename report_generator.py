from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit


def generate_pdf(summary):
    pdf_path = "summary_report.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)



    # Page settings
    width, height = letter
    margin_x = 50  # Left margin
    margin_y = 750  # Start writing from here
    line_height = 20  # Space between lines
    max_width = width - 2 * margin_x  # Available width for text


    # Split summary into wrapped lines
    c.setFont("Helvetica", 12)
    wrapped_text = simpleSplit(summary, "Helvetica", 12, max_width)

    y_position = margin_y
    for line in wrapped_text:
        if y_position < 50:  # If near bottom, create new page
            c.showPage()
            c.setFont("Helvetica", 12)
            y_position = height - 50  # Reset y-position for new page
        c.drawString(margin_x, y_position, line)
        y_position -= line_height  # Move to next line

    c.save()
    return pdf_path
