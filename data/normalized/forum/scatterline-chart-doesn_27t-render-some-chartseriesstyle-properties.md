# ScatterLine chart doesn't render some ChartSeriesStyle properties

## Question

**Iva** asked on 19 Sep 2020

Hello! Have a problem: I can's set ChartSeriesStyle.Step for ScatterLine chart Here is sample (taken from your public sample) <ChartSeries Type="ChartSeriesType.ScatterLine" Style="ChartSeriesStyle.Step" Data="@Series1Data" Name="0.8C" XField="@nameof(ModelData.X)" YField="@nameof(ModelData.Y)"> </ChartSeries> But chart ingore Step style and rendering as normal style Also, i can't set width for series line. Trying like: <ChartSeries Type="ChartSeriesType.ScatterLine" Style="ChartSeriesStyle.Step" Data="@Series1Data" Name="0.8C" XField="@nameof(ModelData.X)" YField="@nameof(ModelData.Y)"> <ChartSeriesLine Width="20" /> </ChartSeries>

## Answer

**Marin Bratanov** answered on 21 Sep 2020

Hi Ivan, The Step appearance is supported only for categorical lines - the "standard" Line series and it can also be set for the line of an Area series ( link ). I've updated the docs with this information ( commit link ). Thank you for bringing this up. Regards, Marin Bratanov

### Response

**Ivan** answered on 21 Sep 2020

Thanks for your reply! And what about settings for line's width?

### Response

**Marin Bratanov** answered on 22 Sep 2020

Hello Ivan, The ChartSeriesLine inner tag settings apply only to an Area series. For categorical Line series the main series tag can be used, and a scatter-line series does not expose such configuration. Regards, Marin Bratanov
