# Enable/Disable DateTime picker inside a popup

## Question

**Eri** asked on 18 Nov 2024

I need to toggle the Enabled state of a TelerikDateTimePicker which resides inside a TelerikPopup based on the checked state of a TelerikCheckBox. This works great outside of a popup, but once in a popup, the Enabled state no longer changes. Here is a REPL: [https://blazorrepl.telerik.com/cIlvvWbC29lZInK522](https://blazorrepl.telerik.com/cIlvvWbC29lZInK522) <div style="padding: 12px;"> <p> Outside popup, toggling checkbox toggles enabled state: </p> <TelerikDateTimePicker @bind-Value="@SelectedTime" Format="MM/dd/yyyy hh:mm tt" ShowWeekNumbers="true" Id="selected-date" Width="250px" Enabled="@(!chkNowSelected)"> </TelerikDateTimePicker> <TelerikCheckBox Id="chkNow" @bind-Value="@chkNowSelected" /> <label for="chkNow"> Now </label> </div> <div style="padding: 12px;"> <p> Inside popup, toggling checkbox does nottoggle enabled state: </p> <TelerikPopup @ref="@PopupRef" AnchorSelector=".popup1" AnimationType="@AnimationType.SlideDown" AnimationDuration="300" Width="260px"> <div style="padding: 20px;"> <TelerikDateTimePicker @bind-Value="@SelectedTime" Format="MM/dd/yyyy hh:mm tt" ShowWeekNumbers="true" Id="selected-date" Enabled="@(!chkNowSelected)"> </TelerikDateTimePicker> <TelerikCheckBox Id="chkNow" @bind-Value="@chkNowSelected" /> <label for="chkNow"> Now </label> </div> </TelerikPopup> <TelerikButton OnClick="@OpenPopup" Class="popup1"> Open Popup </TelerikButton> </div> @code {
#nullable enable

private DateTime? SelectedTime=DateTime.Now;
private bool chkNowSelected { get; set; }=true;
private bool EndTimeEnabled { get; set; }=false;
private TelerikPopup? PopupRef { get; set; }

private void OpenPopup()
{
PopupRef?.Show();
}
}

## Answer

**Erik** answered on 18 Nov 2024

I figured it out. Because popup is under RootComponent it does not automatically update. We have to call the Refresh() method on the popup. <TelerikCheckBox Id="chkNow" Value="@chkNowSelected" ValueChanged="@( (bool value)=> NowChanged(value) )" /> private void NowChanged(bool value)
{
chkNowSelected=value;
PopupRef?.Refresh();
}

### Response

**Hristian Stefanov** commented on 18 Nov 2024

Hi Erik, I'm glad to hear that you have quickly resolved the matter on your own. Indeed, the scenario requires calling the Refresh() method of the popup. Thank you for sharing how things turned out publicly so other developers in the same situation can benefit from this. Kind Regards, Hristian
