# Why does Blazor version 7.1.0 not default to system culture to format DateTime and numbers?

## Question

**Fra** asked on 17 Dec 2024

Out of the box, after updating today to 7.1.0, converted the Weather page from table to TelerikGrid component and the date was being displayed with coma as separator. My html tag's lang was set to en-US, and the SatelliteResourceLanguage property was set to en-US, my OS's regional setting is US and yet the display was European culture. var cult=CultureInfo.GetCultureInfo( "en-US" );
CultureInfo.DefaultThreadCurrentCulture=cult;
CultureInfo.DefaultThreadCurrentUICulture=cult; Adding the above code, resolved the issue. But my expectation is to default to the system's culture even when the application is supporting globalization/localization.

## Answer

**Dimo** answered on 20 Dec 2024

Hello Francis, I confirm that our components apply numeric and date formats, depending on the current app culture. In this case, I would double-check the app and OS configuration. Also review Home.razor in the attached app, which compares the app culture formats with the Telerik component formats. Regards, Dimo Progress Telerik
