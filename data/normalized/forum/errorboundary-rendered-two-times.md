# ErrorBoundary rendered two times

## Question

**Art** asked on 28 Dec 2023

Hi, I'm trying to implement global error handling in my blazor application using Telerik ErrorBoundary. Implementation is very simple in the MainLayout.razor I have this code <ErrorBoundary @ref="errorBoundary"> <ChildContent> @Body </ChildContent> <ErrorContent Context="ex"> @{
OpenNotification("Unhandled exception ocurred. Please try again later.", ThemeColor.Error, CloseAfter.Success);
// TODO: this code is called twice!

} </ErrorContent> </ErrorBoundary> Open Notification it's a private method to show error message private void OpenNotification ( string text, string theme, int closeAfter ) {
Notification.Instance.Show( new NotificationModel
{
Text=text,
ThemeColor=theme,
CloseAfter=closeAfter
});
} so when error happens notification is shown 2 times, I set console log in this code and it's logging two times execution. Any idea what could be the problem? Thanks

## Answer

**Svetoslav Dimitrov** answered on 02 Jan 2024

Hello Artem, Can you replace the Notification with the Window component for example? My best guess is that the ErrorBoundary refreshes the content of the ErrorContent when the error occurs, and because you call a method there - the page is rendered again. If the window renders more times than expected, I would like to ask for a runnable application where I can investigate. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Artem** commented on 02 Jan 2024

Hi Svetoslav, even if I remove any code from the Error Content section and only leave console log, it shows two executions in the log <ErrorContent Context="ex"> @{
Console.WriteLine("Error contect entered!");
} </ErrorContent> which means for me that usage of the method is not what triggers double execution, now second execution happens if I click on any part of the page this is the sequence: 1. Enter to the page 2. Click on the menu item to request data 3. Error happens because API is not available (made in purpose just for debug and generate an error) 4. Error content executed. Notification shown. Log in console shown 5. Click on any part of the page 6. Error content executed again. Notification shown. Log in console shown I tried with Window component, it also executed two times but it's not visible because second modal looks like the same/first modal Thanks

### Response

**Svetoslav Dimitrov** commented on 05 Jan 2024

Hello Artem, If you remove all components and still the Console.WriteLine is printed twice there is something specific with how the Microsoft Blazor ErrorBoundary works. I am not aware of the intricacies of the implementation of this component as it is developed and supported by Microsoft. Regards, Svetoslav
