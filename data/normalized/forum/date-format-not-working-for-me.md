# Date format not working for me

## Question

**Mar** asked on 22 Dec 2021

Hi I am setting the culture in program.cs var culture=new CultureInfo( "da-DK" );
culture.DateTimeFormat.ShortDatePattern="dd-MM-yyyy";
CultureInfo.DefaultThreadCurrentCulture=culture;
CultureInfo.DefaultThreadCurrentUICulture=culture; If I don't set it I get "dd.MM.yyyy" I would like to set it to "dd/MM/yyyy" but when I do that it revert to "dd.MM.yyyy" Is this me using the culture object in the wrong way or a bug in the Telerik Components?

## Answer

**Joana** answered on 27 Dec 2021

Hello Martin, The shared code snippet looks good and should work. I prepared a Repl snippet based on your code and the DatePicker successfully shows the correct format: [https://blazorrepl.telerik.com/wlFQmgQE13htPVV954](https://blazorrepl.telerik.com/wlFQmgQE13htPVV954) Perhaps, some configuration is missing in the Program.cs file, but it will be hard to predict what causes the issue. You could test the culture definition away from Telerik components through ToShortDateString method to verify whether the configuration is right. You might find useful the following resources: [https://github.com/pranavkm/LocSample](https://github.com/pranavkm/LocSample) [https://docs.microsoft.com/en-us/aspnet/core/blazor/globalization-localization?view=aspnetcore-6.0](https://docs.microsoft.com/en-us/aspnet/core/blazor/globalization-localization?view=aspnetcore-6.0) [https://docs.telerik.com/blazor-ui/globalization/overview](https://docs.telerik.com/blazor-ui/globalization/overview) Regards, Joana
