# Telerik Button

## Question

**Pra** asked on 29 Nov 2024

Multiple clicking on button causing method(SaveAndSubmitClicked) to call twice. Even keeping bool variable(IsClicked ) to disable button not working. OnClick="()=> {IsClicked=true;SaveAndSubmitClicked();

## Answer

**Hristian Stefanov** answered on 02 Dec 2024

Hi Prashant, To prevent the SaveAndSubmitClicked method from being called twice when you click multiple times on the button, you can implement the following approach: <TelerikButton Enabled="@IsClicked" OnClick="@OnButtonClick"> Save and Submit </TelerikButton> @code {
private bool IsClicked { get; set; }=true;

private async Task OnButtonClick()
{
// Disable the button immediately to prevent further clicks
IsClicked=false;

// Perform the desired action
await SaveAndSubmitClicked();
}

private async Task SaveAndSubmitClicked()
{
// Simulate the save and submit operation
await Task.Delay(500); // Simulated delay for the operation
Console.WriteLine("Save and Submit action performed.");
}
} Key points Immediate Disabling: " IsClicked" is set to " false " immediately when the button is clicked, preventing further clicks. async/await: The " SaveAndSubmitClicked " method is " awaited " to ensure proper asynchronous behavior if the operation involves asynchronous tasks like saving data to a server. Regards, Hristian Stefanov Progress Telerik
