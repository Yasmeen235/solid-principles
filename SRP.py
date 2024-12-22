class Report:
    def init(self, content):
        self.content = content

    def generate(self):
        return f"Report Content: {self.content}"

class ReportPrinter:
    def print_report(self, report):
        print(report.generate())


report = Report("Sales Data")
printer = ReportPrinter()
printer.print_report(report)