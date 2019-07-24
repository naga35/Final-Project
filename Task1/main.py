import weather_scrapy as scrapy
import csv_writer as cw

if __name__ == "__main__":
    url = "https://karki23.github.io/Weather-Data/assignment.html"
    links = scrapy.get_all_links_from_web_page(url)
    for link in links:
        cw.write_data_into_csv('data_all\weather_data_all.csv', rows[1:], 'a')
