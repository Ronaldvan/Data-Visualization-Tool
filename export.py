def export_to_pdf(data, filename='report.pdf'):

    """ Export the report as a PDF (simple layout) """
    from fpdf import FPDF
    
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt='Data Analysis Report', ln=True, align='C')
    
    pdf.set_font("Arial", size=12)
    # Adding a basic summary of the dataset
    for col in data.columns:
        pdf.cell(200, 10, txt=f'{col}: {data[col].dtype}', ln=True)

    pdf.output(filename)
