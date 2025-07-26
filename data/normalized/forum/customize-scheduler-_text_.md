# Customize scheduler (text)

## Question

**Ste** asked on 24 Nov 2020

Hi everybody, is there a way to set all labels of scheduler component by code? I need a scheduler where the whole text should be changeable independent from current culture (buttons, date and time strings,...) Thx, Stefan

## Answer

**Bozhidar** answered on 27 Nov 2020

Hello, In the current implementation the only way to change strings is through the ITelerikStringLocalizer interface. This affects all telerik components. So you can define a custom service that implements this interface, and returns strings on some other factor, rather than culture. However this will affect all telerik components, not just the scheduler. using Telerik.Blazor.Services; public class SampleResxLocalizer: ITelerikStringLocalizer { // this is the indexer you must implement public string this [ string name]
{ get { return GetStringFromResource(name);
}
} // sample implementation - uses .resx files in the ~/Resources folder named TelerikMessages.<culture-locale>.resx // You can get the values from anywhere you need however public string GetStringFromResource ( string key ) { return Resources.TelerikMessages.ResourceManager.GetString(key, Resources.TelerikMessages.Culture); ;
}
} Regards, Bozhidar

### Response

**Stefan** answered on 02 Dec 2020

Hi Bozhidar, thx for your answer. Indeed: I modified my own translation service by implementing ITelerikStringLocalizer interface and it works as you described. Thank you for your support! Regards, Stefan
