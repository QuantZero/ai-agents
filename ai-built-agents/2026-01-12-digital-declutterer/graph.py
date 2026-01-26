from langgraph import StateMachine
from tools import organize_files_tool, organize_emails_tool

class DeclutterFlow(StateMachine):
    def organize_files(self, input_data):
        self.run(organize_files_tool, input_data)

    def organize_emails(self, input_data):
        self.run(organize_emails_tool, input_data)

declutter_flow = DeclutterFlow()
