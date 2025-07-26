# Using client-side time zone for time columns in Blazor Server grid

## Question

**Pet** asked on 07 Jun 2023

Hi, in an older web app with kendo ui for asp.net core I have a grid which shows timestamps. The Server send the json data in the post request in the server timezone , i.e. "2023-06-07T07:53:40.6227+02:00" . The javascripte code of the grid component then show the time in the timezone of the client to the user. A newer web app I made with Blazor Server. The grid always show a datetime column in the grid in the server timezone. I think there are the tasks needed: 1. determine the timezone of the client with javascript code. 2. applying the timezone of the request to the displayed datetimes in the grid. 3. applying the client timezone in the filter request. Any ideas how this can be solved? Best regards, Peter

## Answer

**Yanislav** answered on 09 Jun 2023

Hello Peter, If I have misunderstood anything, please feel free to correct me. Based on the description provided, it seems that you are looking for similar behavior to the one described here. This behavior is related to the browser's handling of dates, where it converts all dates according to the local time. However, in a Blazor app, this behavior is different because we are not working with JavaScript Date objects. To achieve the desired outcome, I recommend converting all DateTime objects to the local time. Here's how you can do it When the OnAfterRender event is fired, execute a JavaScript script to retrieve the user's time zone offset. Iterate through the Grid data and apply the offset to the DateTime objects. Implement a custom DateTimePicker filter. When the OnChange event of the picker is triggered, programmatically apply a new filter to filter the Grid data. It's important to note that there might be a slight discrepancy between the selected date from the user and the data in the Grid, as we cannot obtain the exact milliseconds. To work around this issue, I suggest applying two filters with different operators (IsLessThan & IsGreaterThan with a difference of 1 second) when the OnChange event of the picker is triggered. This way, you can cover a very narrow range of dates that correspond to the selected date. Here is a REPL example that demonstrates the approach: [https://blazorrepl.telerik.com/GdOguXPn28vOQJyv53](https://blazorrepl.telerik.com/GdOguXPn28vOQJyv53) I hope you find it useful. Regards, Yanislav
