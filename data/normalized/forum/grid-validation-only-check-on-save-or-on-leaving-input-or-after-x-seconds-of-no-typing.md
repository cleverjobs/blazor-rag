# Grid Validation: Only check on save (or on leaving input, or after x seconds of no typing)

## Question

**Tho** asked on 12 May 2022

Hello We have added validation to the Grid using Fluent Validation and this works perfectly. However in the validation we have to go to a back-end API to check if the value is not a duplicate. The current behavior is that the Fluent Validation goes off whenever you type, this causes a lot of load on the API. Is there a way to change this? Maybe so it only occurs when you press the Save button, or when you leave the input field, or after x seconds of no typing... Another valid option would be to do the check in the Update or Create Handler, but how do we display a nice error message that way to the user? Thank you in advance Thomas

## Answer

**Tsvetomir** answered on 16 May 2022

Hi Thomas, Since the server-side validation can be executed only once, I recommend that you add the logic in the Update/Create ActionMethods in the backend. Whenever a value does not pass the validation, return a BadRequest status via the BadRequest() method exposed by the framework: [ HttpPost ] public async Task<IActionResult> Update ( WeatherForecast forecastToUpdate ) { if (ModelState.IsValid)
{ // save to db return Ok(forecastToUpdate);
} else { // do not update the db, return BadRequest status return BadRequest(ModelState);
}
} On the client-side, add a try-catch block that will handle any bad request statuses and prompt the user that the validation of the input data has failed. <TelerikGrid Data="@forecasts OnUpdate=" @UpdateHandler " OnCreate="@CreateHandler" EditMode="@GridEditMode.Popup"> // . . .

public async Task CreateHandler (GridCommandEventArgs args)
{
WeatherForecast currItem=args.Item as WeatherForecast;

try
{
// get the inserted data from the server in case it alters it further (e.g., provides an ID)
WeatherForecast insertedForecast=await ForecastService.InsertForecastAsync(currItem);
// update the view data
forecasts.Insert(0, insertedForecast);
} catch (Exception ex) {
// keep the grid in insert mode
args.IsCancelled=true;
// show information to the user ShowErrorNotification(ex.Message);
}
} There are no limitations on how the error is presented to the user. The above approach can use a TelerikNotification component: <TelerikNotification @ref="@Notification" HorizontalPosition="@NotificationHorizontalPosition.Center" VerticalPosition="@NotificationVerticalPosition.Top" Class="big-notification">
</TelerikNotification> // . . . void ShowErrorNotification ( string message ) {
Notification.Show( new NotificationModel { CloseAfter=0, Text=message, ThemeColor=Telerik.Blazor.ThemeColors.Error });
} The complete example is available in the GitHub repository below. It contains a README.md file that has additional information. [https://github.com/telerik/blazor-ui/tree/master/grid/remote-validation](https://github.com/telerik/blazor-ui/tree/master/grid/remote-validation) Let me know if there is anything else I can help with. Kind regards, Tsvetomir

### Response

**Thomas** commented on 18 May 2022

Thank you for the detailed explanation! We have adjusted our code to work like this. So there's currently no way to make the client validation only go off when saving? So it will always go off during every keypress? Maybe a nice feature to add in the future. :) King regards Thomas

### Response

**Tsvetomir** commented on 19 May 2022

Hi, Thomas. Thank you very much for the provided feedback. Indeed, it is a great idea to expose the option to configure the validation options of the grid via the built-in configuration. I have logged the idea in our

### Response

**Thomas** commented on 23 May 2022

Thanks for the fantastic feedback!
