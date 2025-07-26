# Popover - show on page load

## Question

**Joh** asked on 06 Mar 2025

Is there a way to load a popover when the component loads? I want to use it as a notification on new features in the app.

## Answer

**Hristian Stefanov** answered on 06 Mar 2025

Hi Johan, Yes, you can show a Popover when the component loads by using the OnAfterRenderAsync lifecycle method in Blazor. This method allows you to execute logic after the component has been rendered, which is a suitable place to show the Popover programmatically. Here's a basic example of how you can achieve this: <TelerikPopover @ref="@PopoverRef" AnchorSelector=".popover-target" ShowOn="@PopoverShowOn.Click" Position="@PopoverPosition.Bottom" Offset="20"> <PopoverContent> Telerik Popover for Blazor </PopoverContent> <PopoverActions> <TelerikButton OnClick="@( ()=> PopoverRef?.Hide() )" Icon="@SvgIcon.X"> Close </TelerikButton> </PopoverActions> </TelerikPopover> <TelerikButton Class="popover-target"> Show Popover </TelerikButton> @code {
private TelerikPopover? PopoverRef { get; set; } protected override async Task OnAfterRenderAsync(bool firstRender)
{
if (firstRender)
{
await Task.Delay(30); //Add a slight delay for better UX
PopoverRef?.Show();
}
} } Regards, Hristian Stefanov
