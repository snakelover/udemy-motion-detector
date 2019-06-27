from motion import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnarDataSource

df["Start_string"] = df["Start"].dt.strtime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strtime("%Y-%m-%d %H:%M:%S")
cds = ColumnarDataSource(df)

p = figure(x_axis_type='datetime', height=100, width=500, sizing_mode='scale_width', title="Motion Graph")
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks = 1

hover = HoverTool(tootips=[("Start","@Start_string"), ("End","@End_string")])
p.add_tools(hover)

q = p.quad(left="Start", right="End", bottom=0, top=1, source=cds)
show(p)
