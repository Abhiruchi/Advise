import sys, random, os
import shlex, subprocess

class Visualizer(object):

  def __init__(self, data=None, clusters=None, pagetitle="kmeans-demo"):
    """
    Creates an empty Visualizer object that creates a scatter plot of facebook pages
    @param clusters: Matrix of similar facebook pages 
    """
    self._data = data
    self._clusters = clusters
    self._pagetitle = pagetitle
    self._build()

  def _build(self):
    """
    Creates a html page by building a scatter plot of the different facebook pages.
    Each cluster have a different color.
    """
    colors = random.sample(xrange(0,255), len(self._clusters)*3)
    # start of the html code
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
          text: '"+ self._pagetitle +"'\n \
        },\n \
        subtitle: {\n \
          text: 'Source: Facebook'\n \
        },\n \
        xAxis: {\n \
          title: {\n \
            enabled: true,\n \
            text: 'Likes'\n \
          },\n \
          startOnTick: true,\n \
          endOnTick: true,\n \
          showLastLabel: true\n \
        },\n \
        yAxis: {\n \
          title: {\n \
            text: 'Talking about count'\n \
          }\n \
        },\n \
        tooltip: {\n \
          formatter: function() {\n \
            return '<a href=\"'+this.point.name+'\">'+this.point.name+'</a><br>'+\n \
            this.x +' likes, '+ this.y +' talking';\n \
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
        series: [\n \
          "
    for index in range(0, len(self._clusters)):
      htmlsource += "{\n"
      red = colors[index*3]
      green = colors[index*3 + 1]
      blue = colors[index*3 + 2]
      alpha = 0.5
      name = "Cluster"+ str(index)
      htmlsource += "name: '" + name + "',\n"
      htmlsource += "color: 'rgba("+str(red)+", "+str(green)+", "+str(blue)+", "+str(alpha)+")',\n"
      data = ""
      for id in self._clusters[index]:
        likes = self._data[id]['likes']
        talking = self._data[id]['talking_about_count']
        link = self._data[id]['link']
        data += "{name: '"+ link +"',\nx: "+str(likes)+",\n y: "+str(talking)+"},\n"
      # endfor id
      htmlsource += "data: ["+data + "]\n"
      htmlsource += "},\n"
    # endfor index
    htmlsource += " \
        ]\n \
      });\n \
    });\n \
    "
    htmlsource += "</script>\n"
    htmlsource += "\t</head>\n"
    htmlsource += "\t<body>\n"
    htmlsource += "\t\t<div id=\"container\" style=\"width: 960px; height: 500px; margin: 0 auto\"></div>\n"
    htmlsource += "\t</body>\n"
    htmlsource += "</html>\n"

    html_title = self._pagetitle + ".htm"
    file = open(html_title, "w")
    file.write(htmlsource)
    file.close()

  def visualize(self):
    """
    Opens the html page on a browser
    """
    command_line = "open " + self._pagetitle +".htm"
    args = shlex.split(command_line)
    subprocess.Popen(args)
