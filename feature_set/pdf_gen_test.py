# responsible for generating pdf GDD

from datetime import date
from reportlab.pdfgen import canvas
from reportlab.platypus import Image, SimpleDocTemplate, Paragraph, BaseDocTemplate, PageTemplate, Frame, PageBreak, Flowable
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, LineStyle, ListStyle, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY, TA_CENTER, TA_RIGHT
from reportlab.lib.colors import HexColor, black, red, yellow, green
from reportlab.graphics.barcode import code39
from reportlab.lib.units import mm, inch
from reportlab.pdfbase.pdfmetrics import stringWidth
import os
import data as dt


# database data
name_of_project = "Sonar Bangla"
rnd_number = 1.0
version_number = ("Version [%s]" % rnd_number)
date_of_generation = date.today()
pdf_file_name = "GDD " + "(" + name_of_project + ") " + str(date_of_generation) + ".pdf"
selected_platform = "Android"
selected_genre = "Action"
selected_age_target = "10+"
initial_release_date = date.today()
publisher = "Pandor Astrum"
quick_overview = "Lorem Ipsum Bla bla bla bla and It will be filled from qt gui"
high_concept = "Lorem Ipsum Bla bla bla bla and It will be filled from qt gui"
imgDir = os.getenv("LOCALAPPDATA") + "\\PandorAstrum\\Image\\"
logo_of_company = imgDir + "final_transparent.png"
unique_selling_points = "List of points from the gui"
selected_device_detail = "Selected device detail"
# main pdf
# doc = SimpleDocTemplate(pdf_file_name, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
im = Image(logo_of_company, 3*inch, 3*inch)


# styles
def stylesheet():
    styles = {
        'default': ParagraphStyle(
            'default',
            fontName='Times-Roman',
            fontSize=10,
            leading=12,
            leftIndent=0,
            rightIndent=0,
            firstLineIndent=0,
            alignment=TA_LEFT,
            spaceBefore=0,
            spaceAfter=0,
            bulletFontName='Times-Roman',
            bulletFontSize=10,
            bulletIndent=0,
            textColor=black,
            backColor=None,
            wordWrap=None,
            borderWidth=0,
            borderPadding=0,
            borderColor=None,
            borderRadius=None,
            allowWidows=1,
            allowOrphans=0,
            textTransform=None,  # 'uppercase' | 'lowercase' | None
            endDots=None,
            splitLongWords=1,
        ),
    }
    styles['version_number'] = ParagraphStyle(
        'version_number',
        parent=styles['default'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=8,
        alignment=TA_RIGHT,
        textColor=HexColor(0xff8100),
        spaceAfter=20,
    )
    styles['gdd'] = ParagraphStyle(
        'gdd',
        parent=styles['default'],
        leading=14,
        borderColor=black,
        borderWidth=1,
        borderPadding=5,
        borderRadius=2,
        spaceBefore=10,
        spaceAfter=10,
    )
    styles['project_name'] = ParagraphStyle(
        'project_name',
        parent=styles['default'],
    )
    styles['heading'] = ParagraphStyle(
        'heading',
        parent=styles['default'],
        alignment=TA_CENTER,
    )
    return styles


# c.showPage()
page_width, page_height = A4
#<editor-fold desc="Custom Flowable Classes">
class Sep_Line(Flowable):
    # ----------------------------------------------------------------------
    def __init__(self, width, height=0, space_after=0):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.space_after = space_after

    # ----------------------------------------------------------------------
    def __repr__(self):
        return "Line(w=%s)" % self.width

    # ----------------------------------------------------------------------
    def draw(self):
        """
        draw the line
        """
        self.canv.setStrokeColorRGB(0.372549, 0.619608, 0.627451)
        self.canv.line(0, self.height - self.space_after, self.width, self.height - self.space_after)

sep_line = Sep_Line(450, space_after=10)

class Headlines(Flowable):
    # ----------------------------------------------------------------------
    def __init__(self, x=0, y=0, width=390, height=0, text="", space_after=10):
        Flowable.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.space_after = space_after
        self.text_width = stringWidth(self.text, fontName='Helvetica', fontSize=20)

    # ----------------------------------------------------------------------
    def __repr__(self):
        return

    # ----------------------------------------------------------------------
    def draw(self):
        """
        draw a line
        draw the string line
        draw another line
        """

        self.canv.linearGradient(105 * mm, 200 * mm, 180 * mm, 100 * mm, (red, yellow, green), (0, 0.8, 1), extend=False)
        self.canv.rect(80, -55, 290, 50,
                       fill=True,
                       stroke=False)

        self.canv.setStrokeColorRGB(0.372549, 0.619608, 0.627451)
        self.canv.line(60, self.height - self.space_after, self.width, self.height - self.space_after)

        self.canv.setFillColorRGB(0.541176, 0.168627, 0.886275)
        self.canv.setFont("Helvetica", 22)
        self.canv.drawCentredString((page_width - self.text_width)/2.5, self.y-36, self.text)

        self.canv.setStrokeColorRGB(0.372549, 0.619608, 0.627451)
        self.canv.line(60, self.height - self.space_after*5, self.width, self.height - self.space_after*5)

# </editor-fold>

headlines = Headlines(text="Index")
# c.showPage()
# create a barcode object
# (is not displayed yet)
# The encode text is "123456789"
# barHeight encodes how high the bars will be
# barWidth encodes how wide the "narrowest" barcode unit is
# barcode=code39.Extended39(pdf_file_name,barWidth=0.2*mm,barHeight=20*mm)
# drawOn puts the barcode on the canvas at the specified coordinates
# barcode.drawOn(c,100*mm,100*mm)
class Barcode_gen(Flowable):
    def __init__(self, text_array_to_encode):
        Flowable.__init__(self)
        self.text_array_to_encode = text_array_to_encode
        self.encoded_all = ""

        for e in self.text_array_to_encode:
            self.encoded_all = self.encoded_all + " " + e

    def draw(self):
        barcode = code39.Extended39(self.encoded_all, barWidth=0.2 * mm, barHeight=20 * mm)
        barcode.drawOn(self.canv, 100 * mm, 100 * mm)

text_array = ["mango", "people", "and",]
barcode = Barcode_gen(text_array)

def build_flowables(stylesheet):
    return [
        # cover page
        Paragraph(version_number, stylesheet['version_number']),
        Paragraph(str(date_of_generation), stylesheet['version_number']),
        im,
        Paragraph("Game Design Document", stylesheet['gdd']),
        Paragraph(name_of_project, stylesheet['project_name']),
        PageBreak(),
        # index page
        Paragraph("Index", stylesheet['heading']),
        PageBreak(),
        #Game overview
        Paragraph("Game Overview",  stylesheet['heading']),
        Paragraph("Title: " + name_of_project, stylesheet['default']),
        Paragraph("Platform: " + selected_platform, stylesheet['default']),
        Paragraph("Genre: " + selected_genre, stylesheet['default']),
        Paragraph("Targeted age: " + selected_age_target, stylesheet['default']),
        Paragraph("Initial Release Date: " + str(initial_release_date), stylesheet['default']),
        Paragraph("Publisher: " + publisher, stylesheet['default']),
        Paragraph("Quick Review: " + quick_overview, stylesheet['default']),
        #high concept
        Paragraph("High Concept", stylesheet['heading']),
        Paragraph(high_concept, stylesheet['default']),
        #Unique sellign points
        Paragraph("Unique Selling Points", stylesheet['heading']),
        Paragraph(unique_selling_points, stylesheet['default']),
        #platform requirements according to selected
        Paragraph("Platform Minimum Requirements", stylesheet['heading']),
        Paragraph(selected_platform, stylesheet['default']),
        Paragraph(selected_device_detail, stylesheet['default']),
        #competence title
        Paragraph("Competence Title", stylesheet['heading']),
        Paragraph(name_of_project + "By " + publisher, stylesheet['default']),
        #Game objective
        Paragraph("Game Objective", stylesheet['heading']),
        Paragraph("About the game", stylesheet['default']),
        #Game rules
        Paragraph("Game Rules", stylesheet['heading']),
        Paragraph("Here Goes all the Rules", stylesheet['default']),
        #Gameplay
        Paragraph("Gameplay", stylesheet['heading']),
        Paragraph("According to selection of platfrom and gameplay type next will go image", stylesheet['default']),
        #Player NPC
        Paragraph("Player and NPC", stylesheet['heading']),
        Paragraph("All the Player and NPC Type", stylesheet['default']),
        #Concept art and mock
        Paragraph("Concept Art", stylesheet['heading']),
        Paragraph("Image 1, 2, 3, 4, 5 for iteration of every picture", stylesheet['default']),
        #Wish list
        Paragraph("Wish List", stylesheet['heading']),
        Paragraph("hear will go a list of wishes or re iteration", stylesheet['default']),
        # Barcode
        sep_line,
        headlines,
        barcode,




    ]



def build_pdf(filename, flowables):
    doc = BaseDocTemplate(filename)
    doc.addPageTemplates(
        [
            PageTemplate(
                frames=[
                    Frame(
                        doc.leftMargin,
                        doc.bottomMargin,
                        doc.width,
                        doc.height,
                        id=None
                    ),
                ]
            ),
        ]
    )
    doc.build(flowables)

build_pdf(pdf_file_name, build_flowables(stylesheet()))