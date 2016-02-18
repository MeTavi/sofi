class Table(object):
    """Implements the <table> tag"""

    def __init__(self, striped=False, bordered=False, hover=False, condensed=False, responsive=False, cl=None, ident=None, style=None):
        self.children = list()

        self.cl = cl
        self.ident = ident
        self.style = style

        self.striped = striped
        self.bordered = bordered
        self.hover = hover
        self.condensed = condensed
        self.responsive = responsive

    def __str__(self):
        output = [ "<table" ]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        output.append(" class=\"table")

        cls = []
        if self.striped:
            cls.append('table-striped')

        if self.bordered:
            cls.append('table-bordered')

        if self.hover:
            cls.append('table-hover')

        if self.condensed:
            cls.append('table-condensed')

        if self.cl:
            cls.append(self.cl)

        if len(cls) > 0:
            output.append(" ")
            output.append(" ".join(cls))

        output.append("\"")

        if self.style:
            output.append(" style=\"")
            output.append(self.style)
            output.append("\"")

        output.append(">")

        for child in self.children:
            output.append(str(child))

        output.append("</table>")

        if self.responsive:
            return "<div class=\"table-responsive\">" + "".join(output) + "</div>"
        else:
            return "".join(output)


    def additem(self, item):
        if item is not None:
            self.children.append(item)
