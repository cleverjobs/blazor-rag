# OnRead handler seems to swallow unhandled exception

## Question

**Gre** asked on 08 Dec 2020

In the WASM Blazor app I'm working on, there is a centralized/global unhandled-exception handler that we leverage in order to avoid having to try/catch all over the place. For some reason, the Grid's `OnRead` event/handler seems to be swallowing exceptions, thus circumventing the aforementioned centralized handler. Here is an example, using the bog-standard Blazor WASM template that demonstrates what I mean. Any suggestions on what to try to have exceptions that may occur in OnRead to bubble-up like everything else is? Thanks in advance. @page "/fetchdata" @using BlazorUnhandled.Shared @inject HttpClient Http <TelerikGrid Data=@forecasts AutoGenerateColumns="true" OnRead="@GridOnRead"> </TelerikGrid> @code { private WeatherForecast[] forecasts; protected override async Task OnInitializedAsync() { // This (when uncommented) results in the expected behaviour of the Blazor error handler doing what it's supposed to //throw new Exception("bad thing from OnInitializedAsync"); } protected async Task GridOnRead(GridReadEventArgs args) { var results=await Http.GetFromJsonAsync<WeatherForecast[]>("WeatherForecast"); // This does _NOT_ result in the expected behaviour of the Blazor error handler: throw new Exception("bad thing from GridOnRead"); forecasts=results; StateHasChanged(); } }

## Answer

**Bozhidar** answered on 09 Dec 2020

Hello, In some specific cases, where performance is important, we use a Discard to avoid waiting for the event handler to complete, in order to not hang certain operations. You can see the exact same approach in MS components as well, for instance here, and reproducible with this code: <EditForm Model="this"> <InputText @bind-Value="@MyProperty"> </InputText> </EditForm> @code {
public string MyProperty
{
get
{
return "Sample text";
}
set
{
throw new Exception();
}
}
} This has the same effect of hiding the exception, as the operation is completed in a separate context than the Blazor thread. As a workaround you would need to use a try-catch inside the OnRead handler, and provide the information to your global exception handler by some other method (perhaps inject it as a service, and call a method on it). Regards, Bozhidar
