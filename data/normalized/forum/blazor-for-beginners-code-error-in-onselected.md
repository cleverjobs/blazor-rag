# Blazor for Beginners code error in OnSelected

## Question

**Ken** asked on 26 Mar 2020

Is anyone using the code from the free book and getting it to build/run? I can't get past the event call back code on pages 46-47. I find the code references OnSelected="HandleItemSelected" delegate when no procedure/var exists with that name. I think I need to add a delegate to WeatherDay component. Book: <WeatherDay TemperatureC="forecast.TemperatureC" Summary="@forecast.Summary" DayOfWeek="forecast.Date.DayOfWeek" OnSelected="HandleItemSelected" Selected="forecast.Selected"> I tried: <WeatherDay TemperatureC="forecast.TemperatureC" Summary="@forecast.Summary" DayOfWeek="forecast.Date.DayOfWeek" OnSelected="HandleOnSelected" Selected="forecast.Selected">

## Answer

**Marin Bratanov** answered on 27 Mar 2020

Hi Kenneth, Thank you for reaching out. Indeed, it seems that a sample handler is missing from the book, and I will forward this issue to the people working on it. Here's a sample handler that you can try in the WeeklyForecast.razor file (I am also attaching a runnable project that demonstrates it): async Task HandleItemSelected ( DayOfWeek day ) {
WeatherForecast selectedForecast=forecasts.Where(f=> f.Date.DayOfWeek==day).First(); if (selectedForecast !=null )
{
selectedForecast.Selected=!selectedForecast.Selected;
}
} Regards, Marin Bratanov

### Response

**DR** commented on 21 Jan 2022

Almost 2 years later, and the book has not yet been corrected? Also other 'typos' like above Summary="@forecast.Summary" where the leading @is not needed page 25 "API endpionts for data" (endpoints spelled wrong) page 33 "where it should to be placed" page 66 "diffing algorithm to to ensure"

### Response

**Hristian Stefanov** commented on 26 Jan 2022

Hi Dennis, I've reached out to the author of the book. We are now waiting for a response. I will keep you updated. Thank you for your patience while we investigate the matter here.

### Response

**Ed** commented on 02 Feb 2022

above Summary="@forecast.Summary" where the leading @is not needed Addressing the typos, however the statement above is correct. Because the parameter Summary is a String, if the `@` is omitted then the value becomes the string literal "forecast.Summary" and not the value of the property `forecast.Summary`.

### Response

**Ed** answered on 26 Jan 2022

Thanks for making me aware of these issues. There are currently plans to replace the ebook with a much larger and complete ebook from O'Riley for free to our customers and community 🥳 In the mean time Ill see if theres a way to quicky address the typos described here. Best regards, Ed Charbeneau

### Response

**DR** commented on 27 Jan 2022

Thanks Ed. Hopefully you will use Visual Studio 2022 / .NET 6, and address the warnings, etc. ;) (Also, for Theme Chooser demo, it's not clear about where light.css and dark.css come from and where to reference them.)

### Response

**Ed** commented on 02 Feb 2022

It was implied that there was a theoretical app with light and dark themes, no code for those .css files is shown in the e-book. However, you can easily create them using a tool like themebuilder.telerik.com or visit [https://bootswatch.com/](https://bootswatch.com/) (see Darkly & Flatly).

### Response

**Ed** commented on 02 Feb 2022

There's also a GitHub repo. I'm updating it for .NET 6 per your request. [https://github.com/EdCharbeneau/BlazorBookExamples](https://github.com/EdCharbeneau/BlazorBookExamples)

### Response

**Ed** commented on 02 Feb 2022

The GitHub project is updated to .NET 6. I think the warnings you refer to are due to the new `Nullable` feature in C# 9? These warnings can get quite bothersome in Razor. I addressed them in the repo, but it will take time to get the edits into the book.
