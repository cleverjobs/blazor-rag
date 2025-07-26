# Example of Grid populated by real remote source and HttpClient

## Question

**Rog** asked on 12 Aug 2021

I have struggled for years with foo bar examples and Telerik Documentation that does not contain any examples acquiring the data for a Grid that does not assume that you are using jsonp or odata. I am trying to populate a Blazor Grid with data from a simple REST API over which I have no control. Do you have any examples that show this? I haven't been able to find any. I would like to to be able to capture the data from the remote API (e.g. metaweather) and use that data to populate the grid. Here's an example of a demo Blazor app where I populate an html table using that API: page "/weather"
@using System.Net.Http.Json

@inject IHttpClientFactory _clientFactory <h3> WeatherData </h3> @if (string.IsNullOrWhiteSpace(errorString)==false)
{ <h2 style="color: red;"> @errorString </h2> }
else if (forecast is null)
{ <div class="h4"> Loading... </div> }
else
{ <table class="table table-stripped"> <thead class="thead-dark"> <tr> <th> Date </th> <th> Weather State </th> <th> Low </th> <th> High </th> </tr> </thead> <tbody> @foreach (var w in forecast.consolidated_weather)
{ <tr> <td> @w.applicable_date </td> <td> @w.weather_state_name </td> <td> @w.min_temp </td> <td> @w.max_temp </td> </tr> } </tbody>> </table> }

@code {

VancouverForecast forecast;
string errorString;

protected override async Task OnInitializedAsync()
{
var request=new HttpRequestMessage(HttpMethod.Get, "[https://www.metaweather.com/api/location/9807");](https://www.metaweather.com/api/location/9807");)
var client=_clientFactory.CreateClient();

HttpResponseMessage response=await client.SendAsync(request);

if (response.IsSuccessStatusCode)
{
forecast=await response.Content.ReadFromJsonAsync <VancouverForecast> ();
errorString=null;
}
else
{
errorString=$"There was an error getting our forecast: {response.ReasonPhrase}()";
}
}
} My eventual goal is to create a properly structured app with separation of concerns doing this sort of thing. Anything you could point me to to assist me in that goal would be greatly appreciated.

## Answer

**Matthias** answered on 12 Aug 2021

Hi Roger, as far as I understood correctly, you want to display the data in the grid with an API call. I have tested the call (your example on [https://www.metaweather.com)](https://www.metaweather.com)) and created the necessary classes. I'm sure you will have done the same in another file. The corresponding classes are inserted again at the very end. Actually, you've written almost everything for this already. I have, since there is a nice demo at Telerik also implemented a calendar with it. What looks like this in the end: Code: (quick and dirty=> the code still requires error handling and improvements, of course. ) <TelerikButton OnClick="GetWeather"> get </TelerikButton> <TelerikGrid Data="@ConsolidatedWeathers"> <GridColumns> <GridColumn Field="@nameof(ConsolidatedWeather.applicable_date)" /> <GridColumn Field="@nameof(ConsolidatedWeather.weather_state_name)" /> <GridColumn Field="@nameof(ConsolidatedWeather.min_temp)" /> <GridColumn Field="@nameof(ConsolidatedWeather.max_temp)" /> </GridColumns> </TelerikGrid> <div class="demo-section auto"> <TelerikCalendar Date="@startDate" View="CalendarView.Month" SelectionMode="@CalendarSelectionMode.Multiple" OnCellRender="@OnCellRenderHandler"> </TelerikCalendar> </div> public VancouverForecast forecast { get; set; }
ObservableCollection<ConsolidatedWeather> ConsolidatedWeathers { get; set; } public DateTime startDate { get; set; } async Task GetWeather ( ) { var request=new HttpRequestMessage(HttpMethod.Get, "[https://www.metaweather.com/api/location/9807"](https://www.metaweather.com/api/location/9807") ); var client=_clientFactory.CreateClient();

HttpResponseMessage response=await client.SendAsync(request); if (response.IsSuccessStatusCode)
{
forecast=await response.Content.ReadFromJsonAsync<VancouverForecast>();
ConsolidatedWeathers=new ObservableCollection<ConsolidatedWeather>(forecast.consolidated_weather);

startDate=Convert.ToDateTime(forecast.consolidated_weather.FirstOrDefault().applicable_date);
}
} void OnCellRenderHandler ( CalendarCellRenderEventArgs args ) { if (ConsolidatedWeathers is null || !ConsolidatedWeathers.Any()) return; string dt=args.Date.ToString( "yyyy-MM-dd" ); var fnd=ConsolidatedWeathers.FirstOrDefault(_=> _.applicable_date==dt); if (fnd is not null )
{ if (fnd.weather_state_name=="Heavy Cloud" )
args.Class="with-forecast cloudy"; if (fnd.weather_state_name=="Light Rain" )
args.Class="with-forecast rainy"; if (fnd.weather_state_name=="Light Cloud" )
args.Class="with-forecast partly-sunny";

}
} css .k-calendar.k-calendar-view { padding: 0; width: 280px; height: 280px;
}.k-calendar.k-calendar-monthview.k-link { padding: 0; width: 40px; height: 40px; line-height: 1; flex-flow: column nowrap;
}.k-calendar.calendar-monthview.k-calendar-td.with-forecast { width: 40px; height: 40px;
}.with-forecast.k-link::after { margin-top: 1px; font-size: 14px; font-family: apple color emoji, segoe ui emoji, noto color emoji, android emoji, emojisymbols, emojione mozilla, twemoji mozilla, segoe ui symbol; display: block;
}.k-calendar-monthview.sunny.k-link::after { content: '☀️' }.k-calendar-monthview.partly-sunny span::after { content: '🌤️' }.k-calendar-monthview.cloudy.k-link::after { content: '☁️' }.k-calendar-monthview.rainy.k-link::after { content: '🌧️' }.k-calendar-monthview.snowy.k-link::after { content: '🌨️' } classes public class ConsolidatedWeather { public object id { get; set; } public string weather_state_name { get; set; } public string weather_state_abbr { get; set; } public string wind_direction_compass { get; set; } public DateTime created { get; set; } public string applicable_date { get; set; } public double min_temp { get; set; } public double max_temp { get; set; } public double the_temp { get; set; } public double wind_speed { get; set; } public double wind_direction { get; set; } public double air_pressure { get; set; } public int humidity { get; set; } public double visibility { get; set; } public int predictability { get; set; }
} public class Parent { public string title { get; set; } public string location_type { get; set; } public int woeid { get; set; } public string latt_long { get; set; }
} public class Source { public string title { get; set; } public string slug { get; set; } public string url { get; set; } public int crawl_rate { get; set; }
} public class VancouverForecast { public List<ConsolidatedWeather> consolidated_weather { get; set; } public DateTime time { get; set; } public DateTime sun_rise { get; set; } public DateTime sun_set { get; set; } public string timezone_name { get; set; } public Parent parent { get; set; } public List<Source> sources { get; set; } public string title { get; set; } public string location_type { get; set; } public int woeid { get; set; } public string latt_long { get; set; } public string timezone { get; set; }
}

### Response

**Marin Bratanov** commented on 13 Aug 2021

To add two shortcuts to this already great answer: You can create a Wasm project through our VS extensions, and it will have full CRUD through a service and a server endpoint: [https://docs.telerik.com/blazor-ui/getting-started/vs-integration/new-project-wizard](https://docs.telerik.com/blazor-ui/getting-started/vs-integration/new-project-wizard) - use the Grid, Chart, Form template The following sample projects show how you can optimize those read requests to only require the current page of data as opposed to all data: [https://github.com/telerik/blazor-ui/tree/master/grid/datasourcerequest-on-server](https://github.com/telerik/blazor-ui/tree/master/grid/datasourcerequest-on-server)

### Response

**Roger** commented on 16 Aug 2021

Great - thanks to both responses!
