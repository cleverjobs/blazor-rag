# Global TelerikLoaderContainer, almost there, but unable to set load text

## Question

**Mar** asked on 08 Dec 2021

Hi I have added the LoadContainer to the MainLayout. Now I can inject it like this [CascadingParameter] protected ShowProgressIndicator Progress { get; set; } MainLayout.razor <TelerikRootComponent> <NavMenu /> <div class="page"> <TelerikNotification @ref="@Notification.Instance" HorizontalPosition="@NotificationHorizontalPosition.Right" VerticalPosition="@NotificationVerticalPosition.Top" Class="bi-notification"> </TelerikNotification> <TelerikLoaderContainer Visible="@ProgressIndicator.Visible" Text="Working on it .." Size="@LoaderSize.Large" /> <CascadingValue IsFixed="true" Value="@Notification"> <CascadingValue Value="@ProgressIndicator"> @Body </CascadingValue> </CascadingValue> </div> </TelerikRootComponent> @code
{
Notification Notification { get; }=new();
ShowProgressIndicator ProgressIndicator { get; }=new();
} What I can't get to work is setting the loading text on the LoadContainer. It's always using the default text "Loading ..." Show/Hide works fine. Progress.Visible=true; public class ShowProgressIndicator { public TelerikLoaderContainer LoaderContainer { get; set; } public bool Visible { get; set; } public string Text { get; set; }="Working on it .."; // public void Show() // { // Text="Working on it .."; // Visible=true; // } // // public void Hide() // { // Visible=false; // } }

### Response

**Marin Bratanov** commented on 11 Dec 2021

At a quick glance, the Text is hardcoded with Text="Working on it .." perhaps it should be something like Text="@ProgressIndicator.Text"
