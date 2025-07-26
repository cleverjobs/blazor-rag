# ProgressBar not updating in a DialogContent tag

## Question

**Web** asked on 16 Feb 2023

I have a relatively long running task and would like to show a Dialog box informing the user stuff is happening with a ProgressBar to show completion progress. However when the ProgressBar is in DialogContent it is not updating the UI when I update the Value of the progressbar. If I put the progressbar in the body of the page it works as expected. Razor Code is something like: <TelerikDialog @bind-Visible="@DialogVisible" Width="500px" ShowCloseButton="false" CloseOnOverlayClick="false"> <DialogTitle> Updating </DialogTitle> <DialogContent> <p> Assigning stuff... </p> <TelerikProgressBar Value="@ProgressValue" Max="100"> </TelerikProgressBar> </DialogContent> </TelerikDialog> Then code is: @code { private bool DialogVisible { get; set; }=false; private double ProgressValue=0; private async void ButtonClick ( ) {
DialogVisible=true; for ( var i=0; i <20; i++)
{
ProgressValue=Math.Round(( double )i / 20 * 100 );
StateHasChanged(); await Task.Delay( 1000 );
}
}
}

## Answer

**Nadezhda Tacheva** answered on 21 Feb 2023

Hi WebDev, The Dialog will not automatically update to reflect such a programmatic change in its content. To force it to do so, you may invoke the Refresh method of the component instead of calling StateHasChanged(): TelerikDialog DialogRef; private async void ButtonClick ( ) {
DialogVisible=true; for ( var i=0; i <20; i++)
{
ProgressValue=Math.Round(( double )i / 20 * 100 ); DialogRef.Refresh(); await Task.Delay( 1000 );

}
} Here is a runnable version of the modified code, so you can easily test it: [https://blazorrepl.telerik.com/wxaGwFbg34K8Hqy230.](https://blazorrepl.telerik.com/wxaGwFbg34K8Hqy230.) I hope you will find the above information and sample useful. Please let us know if any other questions are raised. Regards, Nadezhda Tacheva
