# can we use telerikdatepicker with user's based date instead of server's date for "today" on calender

## Question

**Ana** asked on 03 Jul 2025

i am using TelerikDatePicker. I want to use user's timezone based date which i am getting in "OnAfterRenderAsync" but the telerikdatepicker is mixing up between server's date and user's timezone based date. when i click today instead of selecting user's timezone based date(3 july), it selects the server based date i-e 2 july (which is different). Moreoever, as per in attached image user's timezone based date is 3 july 2025 and server's date is 2 july 2025 and the font of 2 july 2025 is red however the highlighter has moved to 3 july 2025. I want the datepicker to use user's timezone based date and deal it like it has been dealing with server's date. this is my razor page <TelerikDatePicker Format="dd-MMM-yyyy" @bind-Value="@abc.rcvdDateDW" Enabled="@isDetailEditable" OnOpen="OnDatePickerOpenDW" OnClose="OnDatePickerCloseDW" /> this is how i am setting things up in my razor.cs protected override async Task OnAfterRenderAsync(bool firstRender) { if (firstRender && !_initialized) { _initialized=true; try { var userTimeZoneId=await tokenStorage.GetTokenAsync(UserTimeZoneInfokey); var timeZoneId=string.IsNullOrWhiteSpace(userTimeZoneId) ? "UTC" : userTimeZoneId; TimeZoneInfo userTimeZone=TimeZoneInfo.FindSystemTimeZoneById(timeZoneId); userTimeInTimeZone=TimeZoneInfo.ConvertTimeFromUtc(DateTime.UtcNow, userTimeZone); } catch { userTimeInTimeZone=DateTime.UtcNow; // fallback } await ShowData(); InitializeTabsBasedOnPermissions(); await Tasks(); StateHasChanged(); }} public async Task OnDatePickerOpenDW(DatePickerOpenEventArgs args) { if (abc.rcvdDateDW==null && !isTempDateDWReceived) { abc.rcvdDateDW=userTimeInTimeZone; isTempDateDWReceived=true; StateHasChanged(); } } public async Task OnDatePickerCloseDW(DatePickerCloseEventArgs args) { if (isTempDateDWReceived && abc.rcvdDateDW==userTimeInTimeZone) { abc.rcvdDateDW=null; isTempDateDWReceived=false; StateHasChanged(); } } thats the output i am getting Does telerikdatepicker do support this or not ? if yes kindly guide me how can i achieve this. I have tried many ways but none of them worked. Thanks

## Answer

**Tsvetomir** answered on 04 Jul 2025

Hi Anas, Thank you for the detailed explanation of your scenario. We have an open feature request for adding such functionality in the date components: Time zone for NOW and TODAY button (or function to be called) I have voted on your behalf to raise its priority. In the meantime, the possible alternatives are: Setting the value to local date. The approach should look like this: @inject IJSRuntime JsRuntime <h3> Select Date (User's Local Time) </h3> <TelerikDatePicker @bind-Value="@LocalDateTime" Format="dd-MMM-yyyy" OnOpen="HandlePickerOpen" /> <p> Selected (Local Time): @LocalDateTime.ToString("dd-MMM-yyyy") </p> @code {
private DateTime LocalDateTime { get; set; }=DateTime.UtcNow;
private TimeSpan UserOffset { get; set; }=TimeSpan.Zero;

protected override async Task OnAfterRenderAsync(bool firstRender)
{
if (firstRender)
{
int offsetInMinutes=await JsRuntime.InvokeAsync <int> ("GetTimezoneValue");
UserOffset=TimeSpan.FromMinutes(-offsetInMinutes);
LocalDateTime=DateTime.UtcNow + UserOffset;

StateHasChanged();
}
}

private void HandlePickerOpen(DatePickerOpenEventArgs args)
{
// Reset value to local date if it’s not already set
LocalDateTime=DateTime.UtcNow + UserOffset;
}
} <script> function GetTimezoneValue ( ) { return new Date ().getTimezoneOffset();
} </script> Use Header Template to use a custom "Today" button that you can handle its click event and change the value as desired. And finally, you can subscribe to the feature request item to receive email notification for any status changes. I hope the provided information serves you well. Regards, Tsvetomir Progress Telerik

### Response

**Anas** commented on 04 Jul 2025

The provided solution is getting date from client's machine, but my requirement is to use the time zone that I have fetched from database.

### Response

**Tsvetomir** commented on 09 Jul 2025

Thank you for coming back with feedback Anas. If the result of the first approach does not align with your expectation, I recommend creating a custom "Today" button that will handle the value changed as desired. Use the Calendar Header Template to render the custom button. Based on your feedback, this is the only available approach that can serves you well, until the linked feature request item is completed. Regards, Tsvetomir
