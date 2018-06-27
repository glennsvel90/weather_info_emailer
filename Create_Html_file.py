from datetime import datetime
from Get_Weather_Data import get_weather_data

def create_html_report(data_dict, icon_url, html_file):
    alt_var = data_dict['weather']

    with open(html_file, mode='w') as outfile:
        outfile.write('\t<tr><td align="center">' + datetime.now().strftime(
        "%m-%d-%Y %H:%M:%S") + '</td></tr><br>\n')
        outfile.write('<img alt={} src=')







if __name__ == '__main__':
    weather_dict, icon = get_weather_data('KNYC')
    create_html_report(weather_dict, icon, "Test_Email_File.html")
