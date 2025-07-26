# TelerikTimePicker is somehow validated when using inside TelerikCard

## Question

**Tho** asked on 16 Jul 2025

Hi, I've some TelerikCard components that host different other components but when using lets say the TelerikTimePicker then as soon as you try to input a time via keyboard it gets a red border and seems to invalidate the input. When using the TelerikTimePicker outside in a simple div then it seems to work. Also when using the popup to set the time it works. Only keyboard input seems to trigger some sort of validation. When losing focus the timepicker resets to 00:00:00. Here's the code of the razor page to replicate the problem: <TelerikCard Width="20rem"> <CardHeader> <CardTitle> Time Selector </CardTitle> </CardHeader> <CardBody> Startzeitpunkt <br> <TelerikTimePicker @bind-Value="@SelectedStartTime" Format="HH:mm:ss" Width="6rem" /> <br> Endzeitpunkt <br> <TelerikTimePicker @bind-Value="@SelectedEndTime" Format="HH:mm:ss" Width="6rem" /> <br> </CardBody> <CardSeparator> </CardSeparator> <CardFooter> footer </CardFooter> </TelerikCard> @code {
protected DateTime SelectedStartTime { get; set; }
protected DateTime SelectedEndTime { get; set; }
} I use the latest telerik blazor components 9.1.0 and VS 2022 17.14.9. Maybe someone has a hint what's wrong with it. Regards, Thomas

## Answer

**Georgi** answered on 18 Jul 2025

Hi Thomas, Thanks for reaching out. When a DateTime object is not explicitly initialized, it defaults to DateTime.MinValue which is 01/01/0001 12:00:00 AM. However the TelerikTimePicker component's default Min value is 01/01/1900. This mismatch is what triggers the validation. To resolve this, you can set the initial value of the bound DateTime property to a date after the default TelerikTimePicker Min value. Here is an example: [https://blazorrepl.telerik.com/wfYVPiaA16ZIewVY44](https://blazorrepl.telerik.com/wfYVPiaA16ZIewVY44) Let us know if you need further assistance with implementation. Regards, Georgi Progress Telerik

### Response

**Thomas** commented on 18 Jul 2025

Hi Georgi, thank you for the explanation. Now it works like a charm again! Regards, Thomas
