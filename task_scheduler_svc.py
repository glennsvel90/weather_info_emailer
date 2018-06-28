from collections import OrderedDict
import schedule
from Get_Weather_Data import get_weather_data
from Create_Html_file import create_html_report
from email_via_gmail import send_gmail

import win32service
import win32serviceutil
import win32event

class PythonTaskSvc(win32serviceutil.ServiceFramework):
    _svc_name_ = "PythonTaskSvc"
    _svc_display_name_ = "Python Task Scheduling Service"
    _svc_description_ = "This Python service schedules tasks"

    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcDoRun(self):
        def job():
            weather_dict, icon = get_weather_data('KLAX')
            weather_dict_ordered = OrderedDict(sorted(weather_dict.items()))

            email_file = "Email_File.html"
            create_html_report(weather_dict_ordered, icon, email_file)
            send_gmail(email_file)

        schedule.every(1).minute.do(job)

        rc = None
        while rc != win32event.WAIT_OBJECT_0:
            schedule.run_pending()
            rc = win32event.WaitForSingleObject(self.hWaitStop, 5000)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(PythonTaskSvc)
