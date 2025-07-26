# Error en TelerikListView

## Question

**Ale** asked on 10 Aug 2024

Al crear una TelerikListView no me marca error en codigo pero al mostrarlo en la pagina me sale este error Microsoft.JSInterop.JSException: Could not find 'TelerikBlazor.initListView' ('initListView' was undefined). Error: Could not find 'TelerikBlazor.initListView' ('initListView' was undefined) como lo podria solucionar?

### Response

**Dimo** commented on 14 Aug 2024

@Alejandro - this error means that the telerik-blazor.js file is old and doesn't include a ListView. This is strange, because the ListView is a 4-year-old component. Are you by any chance using a very old Telerik UI for Blazor version? If not, then please send us a runnable example for inspection. Please note that the communication in our forums and tickets is only in English.
