# Slider buttons

## Question

**Rob** asked on 07 Sep 2023

Why are the slider buttons of type 'submit' and how do I change them not to be?

## Answer

**Hristian Stefanov** answered on 08 Sep 2023

Hi Robert, I can confirm that the behavior you encountered is indeed a bug in the Slider. I have created a public item on your behalf to address this: The Slider default button type is "submit", which causes an unexpected form submission. You are automatically subscribed as a creator, which means you will receive email notifications regarding the status updates of this item. Workaround In the interim, as a temporary solution, you can use a small JavaScript function that manually changes the Slider buttons type to " button ". I have prepared an example for you that shows the approach: @inject IJSRuntime js <TelerikSlider @bind-Value="@SliderValue" Min="0" Max="100" SmallStep="1" LargeStep="20" Width="400px"> </TelerikSlider> <script suppress-error="BL9992"> window.changeButtonTypes=function ( ) { var buttons=document.querySelectorAll( ".k-slider button" ); for ( var i=0; i <buttons.length; i++) {
buttons[i].type="button";
}
}; </script> @code {
public int SliderValue { get; set; }

protected override async Task OnAfterRenderAsync(bool firstRender)
{
if (firstRender)
{
await js.InvokeVoidAsync("changeButtonTypes");
}
}
}=====Additionally, as a token of appreciation for bringing this problem to our attention, I have credited your account with Telerik points. Regards, Hristian Stefanov Progress Telerik
