# Is it possible for the datepicker to default open to Time page?

## Question

**Gra** asked on 08 Feb 2022

I have a cases where I need the users to be able to change the date and time, but mostly will just be editing the time? Is there a way to default open to the Time Page rather than opening the date page every time?

## Answer

**Hristian Stefanov** answered on 11 Feb 2022

Hi Grant, I understand the need in such a scenario. You have right. Currently, the DateTimePicker doesn't have the possibility to open the Time page by default. As a result, I opened a feature request on your behalf on our Public Feedback Portal: Allow the DateTimePicker to open the Time portion/page by default This feature will allow you to achieve the desired result. We prioritize feature requests based on community demands and interests. I already added your vote there. You are also automatically subscribed to receive email notifications for status updates. Regards, Hristian Stefanov Progress Telerik

### Response

**Andrew** answered on 11 Oct 2024

FYI, I found a javascript work-around that seems to allow the TIME tab to be auto-selected when the picker is opened. First set the OnOpen event: <TelerikDateTimePicker Id="expectedCheckInTime" @bind-Value="CheckoutCrewViewModel.ExpectedCheckinTime" Format="MMM dd, hh:mm tt" OnOpen="@OnCheckInDateTimePickerOpen"> <DateTimePickerSteps Minute="5" /> </TelerikDateTimePicker> In your @code: @inject IJSRuntime JsRuntime private async Task OnCheckInDateTimePickerOpen(DateTimePickerOpenEventArgs args) { await JsRuntime.InvokeVoidAsync("switchToTimeTab", "expectedCheckInTime"); } In your script.js file: function switchToTimeTab(pickerId) { setTimeout(function () { const picker=document.querySelector('.k-datetime-wrap-md'); if (picker) { const timeTab=picker.querySelector('.k-button-group-stretched button.telerik-blazor.k-button:not(.k-selected) span.k-button-text'); if (timeTab && timeTab.textContent.trim()==='Time') { timeTab.closest('button').click(); } } }, 100); // Slight delay before clicking to allow popup to appear. } Credit goes to Claude AI for that solution (GPT wasn't able to figure it out). Hope that helps! :)

### Response

**Hristian Stefanov** commented on 14 Oct 2024

Hi Andrew, Thank you for sharing the workaround you have found. This will help other developers facing the same scenario. Your effort is highly appreciated. Kind Regards, Hristian
