# RC VS 2019 Preview 2

## Question

**Alb** asked on 04 Feb 2019

I am trying to use Telerik UI for Blazor with Razor Components in VS 2019 Preview 2 and looks like it doesnt work. I get error: ErrorCS0103The name 'context' does not exist in the current When using this: <KendoGrid Data=@forecasts Pageable=true PageSize=5 Sortable=true> <KendoGridColumn Field=@nameof(WeatherForecast.Date)> <Template> @($"{(context as WeatherForecast).Date:d}") </Template> </KendoGridColumn> <KendoGridColumn Field=@nameof(WeatherForecast.TemperatureC) /> <KendoGridColumn Field=@nameof(WeatherForecast.TemperatureF) /> <KendoGridColumn Field=@nameof(WeatherForecast.Summary) /> </KendoGrid> Also if not using Template column the app runs but the grid is not displayed. Is there any workaround or when is expected to have a version working with VS 2019 Preview 2?

## Answer

**Bozhidar** answered on 07 Feb 2019

Hello, I couldn't reproduce the issue locally. We are expecting to release a 0.2 version in a few days, that will add official support for blazor 0.8, alongside VS 2019 preview 2, so stay tuned and follow our blogs for the announcement. Regards, Bozhidar
