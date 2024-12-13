from mod.plot_registry import PlotRegistry 

print("in experiments/run.py", PlotRegistry.registry)

cp = PlotRegistry.registry["ContourPlot"]()
print(type(cp))

np = PlotRegistry.registry["NewPlot"]()
print(type(np))
