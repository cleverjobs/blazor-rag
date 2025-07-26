# UI update on long-running task

## Question

**Dre** asked on 07 Apr 2021

I have the following scenario: - file download from a site; - process records on file to store in a database. The first take about 4 seconds and the second around a minute or a little more. Followed the sample of ProgressBar to signal that records are being processed, however, the UI is not being updated. The environment is Blazor with .NET 5.04 and the latest version of UI for Blazor Below is the Razor component where the data is handled. Any suggestions on how to update the UI and reflect the current status? Thanks @page "/importPeers" @using DataLoader.Models @using DataLoader.Services @using System.Timers @implements IDisposable @inject LoadDataFIService service <h1>CVM FI Download</h1> <p>componente para realizar o download de informações da CVM e carga no banco de dados</p> <hr /> <br /> <div class="row"> <div class="col-sm-8 col-md-8"> <div class="row"> <div class="col-sm-6 col-md-6"> <span> Mês Referência: <TelerikDatePicker @bind-Value="@selectedDate" BottomView="@CalendarView.Year" Format="MMM yyyy"> </TelerikDatePicker> </span> </div> <div class="col-sm-3 col-md-3"> <TelerikButton OnClick="@OnProcessDataClick">Processar</TelerikButton> </div> </div> </div> </div> <br /> <div class="row"> <div class="col-sm-8 col-md-8"> @processingAction <br /> <TelerikProgressBar Indeterminate="@isIndeterminate" Value="@CurrentValue" Max="@MaxValue" /> </div> </div> @currentCount importados... <hr /> @code { public string processingAction { get; set; } public bool isIndeterminate { get; set; }=false; public int progressValue { get; set; }=0; DateTime selectedDate { get; set; }=DateTime.Now; int currentCount=0; public double MaxValue { get; set; }=100; public double CurrentValue { get; set; }=0; public double StepValue { get; set; }=5; public Timer Clock { get; set; }=new Timer(); void OnProcessDataClick() { currentCount++; ProcessData(); } void ProcessData() { //signal progress bar for download processingAction="Downloading..."; MaxValue=5 * 1000; // download should take no more than 4 seconds StartProgress(); var result=service.DownloadFile(selectedDate); // signal end of downloading processingAction="Downloaded!"; StopProgress(); System.Diagnostics.Stopwatch watch=new System.Diagnostics.Stopwatch(); if (result) { processingAction="Processing records..."; MaxValue=65 * 1000; // data processing should last about a minute or more StartProgress(); //watch.Start(); currentCount=service.ReadCsvFile(selectedDate); //watch.Stop(); processingAction="Records processed!"; StopProgress(); } // Console.WriteLine(watch.Elapsed); } public void Dispose() { StopProgress(); Clock?.Close(); } public void StartProgress(int interval=200) { if (Clock?.Enabled==false) { Clock.Interval=interval; Clock.Elapsed -=OnClockElapsedEvent; Clock.Elapsed +=OnClockElapsedEvent; Clock.AutoReset=true; Clock.Start(); } } public void OnClockElapsedEvent(Object source, ElapsedEventArgs e) { if (CurrentValue <MaxValue) { UpdateProgress(); } else { StopProgress(); } } public void UpdateProgress() { CurrentValue +=StepValue; InvokeAsync(StateHasChanged); } public void StopProgress() { Clock?.Stop(); InvokeAsync(StateHasChanged); } }

## Answer

**Nadezhda Tacheva** answered on 12 Apr 2021

Hi Marcello, After revising the below snippet, I see that depending on the time needed for a task to be completed, you are changing the max value of the ProgressBar. Its value is actually correctly changed, but you are not able to see it since the max value is constantly changed. Usually, when the progress is measured in percent, a value of 100% indicates that a task is completed. With that being said, an approach you might try is keep the max value of 100% and to change the time interval depending on the time needed for a task to be completed. This will allow the ProgressBar tо move faster for the downloading the file ( this is the faster task of the two, taking 4 seconds ) and to move slower for the processing records task ( taking about a minute or more ). For both tasks a completed state will mean reaching the 100% in the end of the ProgressBar. You can also restart the timer in the StartProgress method by setting its value to 0 to indicate that a new task is starting and to track its individual progress. Another point to take into consideration is when dealing with asynchronous operations ( such as data processing from a service ), it would be better to work with async tasks instead of voids. I've modified the snippet you have sent to better illustrate the described approach. I have placed some task delays where needed to simulate the service activity in terms of downloading and processing the records. I have also commented out the change of the max values of the ProgressBar to demonstrate how its value is correctly updated if the max value is not changed. To identify the tasks I am checking the processingAction value, you can also use some flags in the service for that purpose. Important points are highlighted for clarity. See code comments for more details on the spot. @*@page "/importPeers" @using DataLoader.Models
@using DataLoader.Services*@@using System.Timers
@*@implements IDisposable
@inject LoadDataFIService service*@<h1>CVM FI Download</h1>

<p>componente para realizar o download de informações da CVM e carga no banco de dados</p>
<hr />
<br />

<div class="row">
<div class="col-sm-8 col-md-8">
<div class="row">
<div class="col-sm-6 col-md-6">
<span>
Mês Referência:
<TelerikDatePicker @bind-Value="@selectedDate" BottomView="@CalendarView.Year" Format="MMM yyyy">
</TelerikDatePicker>
</span>
</div>
<div class="col-sm-3 col-md-3">
<TelerikButton OnClick="@OnProcessDataClick">Processar</TelerikButton>
</div>
</div>
</div>
</div>
<br />
<div class="row">
<div class="col-sm-8 col-md-8">
@processingAction
<br />
<TelerikProgressBar Indeterminate="@isIndeterminate" Value="@CurrentValue" Max="@MaxValue" />
</div>
</div>
@currentCount importados...
<hr />

@code { public string processingAction { get; set; } public bool isIndeterminate { get; set; }=false; public int progressValue { get; set; }=0;
DateTime selectedDate { get; set; }=DateTime.Now; int currentCount=0; public double MaxValue { get; set; }=100; public double CurrentValue { get; set; }=0; public double StepValue { get; set; }=5; public Timer Clock { get; set; }=new Timer(); public int TimeInterval { get; set; } void OnProcessDataClick ( ) {
currentCount++;
ProcessData();

} async Task ProcessData ( ) { //signal progress bar for download processingAction="Downloading..."; /*MaxValue=5 * 1000;*/ // download should take no more than 4 seconds StartProgress(); //simulating server activity await Task.Delay( 4000 ); //var result=service.DownloadFile(selectedDate); // signal end of downloading processingAction="Downloaded!";

StopProgress(); //leave the "Downloaded" notification for a while before starting the new task await Task.Delay( 1000 );

System.Diagnostics.Stopwatch watch=new System.Diagnostics.Stopwatch(); //dummy check if the downloading task is completed, so the records processing task could start. // you can perform that check through the result you are getting from the service if ( processingAction=="Downloaded!" )
{
processingAction="Processing records..."; /*MaxValue=65 * 1000; */ // data processing should last about a minute or more StartProgress(); await Task.Delay( 10000 ); //watch.Start(); //currentCount=service.ReadCsvFile(selectedDate); //watch.Stop(); processingAction="Records processed!";

StopProgress();
} // Console.WriteLine(watch.Elapsed); } public void Dispose ( ) {
StopProgress();
Clock?.Close();
} public void StartProgress ( ) { //identify the tasks using the processingAction value in order to accordingly change the time interval for the tasks if (processingAction=="Downloading..." )
{
TimeInterval=200;
} else if (processingAction=="Processing records..." )
{
TimeInterval=500;
} if (Clock?.Enabled==false )
{ //restart the ProgressBar value, so it can start tracking the new task progress accordingly CurrentValue=0; Clock.Interval=TimeInterval;
Clock.Elapsed -=OnClockElapsedEvent;
Clock.Elapsed +=OnClockElapsedEvent;
Clock.AutoReset=true;
Clock.Start();
}
} public void OnClockElapsedEvent ( Object source, ElapsedEventArgs e ) { if (CurrentValue <MaxValue)
{
UpdateProgress();
} else {
StopProgress();
}
} public void UpdateProgress ( ) {
CurrentValue +=StepValue;
InvokeAsync(StateHasChanged);
} public void StopProgress ( ) {
Clock?.Stop();
InvokeAsync(StateHasChanged);
}

} I hope you will find the above information useful. If any further questions appear, please do not hesitate to contact us. Thank you for choosing Telerik UI for Blazor! Regards, Nadezhda Tacheva

### Response

**Drewanz** answered on 16 Apr 2021

Thanks for the explanation Nadezhda, it made things clear as the process is way too fast to address the new values, better signal the update interval. Also, I changed all the methods to async so everything is now running smoothly.
