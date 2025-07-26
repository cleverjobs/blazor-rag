# Localization not work into a docker container for DatePicker and NumericTextBox components.

## Question

**Mar** asked on 04 Mar 2024

Hy, In my application I had to insert the localization with the default Italian language. I followed the points explained in this link step by step: Blazor Localization - Telerik UI for Blazor Inside my application I therefore have a Resources folder with the following files inside: TelerikMessages.resx and TelerikMessages.it-IT.resx (set as default on Program.cs). My problem is the following: in debug the localization for the DateTimePicker or NumericTextBox components works correctly showing me the date and number formats in Italian with the related translated texts. However, once I insert my application into a docker container, the localization seems to have no effect, showing both components in English language and format. My Resources Folder: However, localization for the Grid component works correctly in both cases. Attached is the behavior of the date picker in debug mode and inside a docker container. Can anyone give me a solution without using the Format property of the components but using localization? My application is in Dotnet 8 Thanks.

## Answer

**Marco** answered on 11 Mar 2024

I solved the problem independently, which does not depend in any way on the Telerik components. Localization works because inside the docker container the information is taken from the .resx resource files. Regarding globalization (and therefore for example the date format). I had to add the following package to my Alpine docker container: icu-data-full. In addition to this, remember to set the DOTNET_SYSTEM_GLOBALIZATION_INVARIANT variable to false inside the Dockerfile.

### Response

**Dimo** answered on 06 Mar 2024

Hello Marco, Based on the screenshots, the localization (translation) is working. The problem may be related to the culture settings of the app, which will depend on the regional settings of the Docker container. The default value of our DateInput Format parameter is the ShortDatePattern of the current culture: CultureInfo.CurrentCulture.DateTimeFormat.ShortDatePattern So, you can choose whether to change the whole culture, override the current culture's ShortDatePattern, or set the Format parameter. Regards, Dimo Progress Telerik
