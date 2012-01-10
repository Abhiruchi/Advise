import sys

class Visualizer(object):

  def __init__(self, data=None, clusters=None, pagetitle="demo"):
    """
    Creates an empty Visualizer object that creates a scatter plot of facebook pages
    @param clusters: Matrix of similar facebook pages 
    """
    self._data = data
    self._clusters = clusters
    self._pagetitle = pagetitle
    self._build()

  def _build(self):
    htmlsource = "<!DOCTYPE HTML>\n"
    htmlsource += "<html>\n"
    htmlsource +=  "\t<head>\n"
    htmlsource += "\t\t<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\n"
    htmlsource += "\t\t<title>Clustering Demo</title>\n"
    htmlsource += "\t\t<script type=\"text/javascript\" src=\"http://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js\"></script>\n"
    htmlsource += "\t\t<script type=\"text/javascript\" src=\"./js/highcharts.js\"></script>\n"
    htmlsource += "\t\t<script type=\"text/javascript\" src=\"./js/modules/exporting.js\"></script>\n"
    htmlsource += "\t\t<script type=\"text/javascript\">\n"
    htmlsource += " \
                  var chart;\n \
                  $(document).ready(function() {\n \
                    chart = new Highcharts.Chart({\n \
                      chart: {\n \
                          renderTo: 'container',\n \
                          defaultSeriesType: 'scatter',\n \
                          zoomType: 'xy'\n \
                      },\n \
                      title: {\n \
                          text: 'Height Versus Weight of 507 Individuals by Gender'\n  \
                      },\n \
                      subtitle: {\n \
                          text: 'Source: Facebook'\n \
                      },\n \
                      xAxis: {\n \
                          title: {\n \
                              enabled: true,\n \
                              text: 'Likes'\n \
                          }\n \
                          startOnTick: true,\n \
                          endOnTick: true,\n \
                          showLastLabel: true\n \
                      },\n \
                      yAxis: {\n \
                          title: {\n \
                              text: 'Talking About Count'\n \
                          }\n \
                      },\n \
                      tooltip: {\n \
                          formatter: function() {\n \
                              return ''+\n \
                              this.x +' likes, '+ this.y +' talking about count';\n \
                          }\n \
                      },\n \
                      legend: {\n \
                          layout: 'vertical',\n \
                          align: 'left',\n \
                          verticalAlign: 'top',\n \
                          x: 100,\n \
                          y: 70,\n \
                          floating: true,\n \
                          backgroundColor: '#FFFFFF',\n \
                          borderWidth: 1\n \
                      },\n \
                      plotOptions: {\n \
                          scatter: {\n \
                              marker: {\n \
                                  radius: 5,\n \
                                  states: {\n \
                                      hover: {\n \
                                          enabled: true,\n \
                                          lineColor: 'rgb(100,100,100)'\n \
                                      }\n \
                                  }\n \
                              },\n \
                              states: {\n \
                                  hover: {\n \
                                      marker: {\n \
                                          enabled: false\n \
                                      }\n \
                                  }\n \
                              }\n \
                          }\n \
                      },\n \
                      series: [{\n \
                        name: 'Female',\n \
                        color: 'rgba(223, 83, 83, .5)',\n \
                        data: [[161.2, 51.6], [167.5, 59.0], [159.5, 49.2], [157.0, 63.0], [155.8, 53.6] ]\n \
                      }]\n \
                    });\n \
                  });\n \
                  "
    htmlsource += "</script>\n"
    htmlsource += "\t</head>\n"
    htmlsource += "\t<body>\n"
    htmlsource += "\t\t<div id=\"container\" style=\"width: 800px; height: 400px; margin: 0 auto\"></div>\n"
    htmlsource += "\t</body>\n"
    htmlsource += "</html>\n"

    html_title = self._pagetitle + ".htm"
    file = open(html_title, "w")
    file.write(htmlsource)
    file.close()

