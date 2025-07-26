# Translate format mask

## Question

**Que** asked on 09 Jul 2024

Hello, We are using blazor Webassembly with Telerik and its localization/globalization. Everything works fine. Client ask us a little detail, to "translate" the mask format for date input ( TelerikDatePicker, ... ). For example, if we use the french culture "fr-BE"we would like to transform "dd/MM/yyyy" to "jj/MM/aaaa" ( d ay=> j our; M onth=> M ois; y ear=> a nnée) or something similar. In Telerik UI for Angular, we have it translated=> How can we achieve that for Telerik UI for Blazor ? Kind regards, Quentin.

## Answer

**Dimo** answered on 11 Jul 2024

Hi Quentin, You can use FormatPlaceHolder, which is available for all our DateTime input components. Regards, Dimo Progress Telerik

### Response

**Quentin** answered on 11 Jul 2024

Hi Dimo, Thanks for the solution! I just saw and try the PlaceHolder attribute in the docs. Kind regards, Quentin.
