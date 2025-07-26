# How to disable autocomplete with TextBox

## Question

**Mic** asked on 01 Aug 2020

What's the best way to disable the autocomplete suggestions displayed when a user first clicks on a TextBox or is entering characters?

## Answer

**Marin Bratanov** answered on 02 Aug 2020

Hello Michael, You can set its Autocomplete parameter to the desired string value for the autocomplete attribute of the input that it will set. You can read more about it here: [https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete.](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete.) The typical setting to instruct the browser to turn off suggestions is setting Autocomplete="off", yet it is up to the browser to honor this. Often it works only when the input is in a <form> that has autocomplete disabled altogether. Regards, Marin Bratanov

### Response

**Daniel** answered on 07 Apr 2021

A related question: how do I turn autocomplete ON. It seems to be off by default on my page but when I set AutoComplete="on" in TelerikTextBox it still does nothing. Then I read you need to make sure it has a unique Name attribute. But that did not help either. Any ideas?

### Response

**Marin Bratanov** answered on 08 Apr 2021

Hi Daniel, It is the browser that controls that, not our components. Enabling the autocomplete is one thing, but then the browser needs to decide to store values for it before the user can see suggestions. This usually happens when the input is in a form and the form gets submitted. If you need to be sure your users get suggestions you want them to get, you can use the Telerik AutoComplete component. It is a textbox where they can put in arbitrary text, bit also lets you show them suggestions from your app, you can even load them on demand as they type. Regards, Marin Bratanov

### Response

**Sabina** commented on 09 Dec 2024

I am using MaskedTextBox, and I would like to have autocomplete enabled. I see that the TelerikMaskedTextBox markup has autocomplete="off" Therefore, it is always disabled. Why? I understand that the browser actually implements the autocomplete, and Telerik cannot control that behavior. The browser behavior would be fine for us. I tried using the AutoComplete component, but it does not provide masked input functionality.

### Response

**Hristian Stefanov** commented on 10 Dec 2024

Hi Sabina, The TelerikMaskedTextBox component has the autocomplete attribute set to "off" by default to prevent conflicts between the autocomplete suggestions and the mask format, ensuring that the input strictly adheres to the specified mask. As a potential alternative approach to address your requirement, you can manually manage autocomplete suggestions and apply them to the MaskedTextBox. This involves listening to input events, fetching suggestions based on user input, and ensuring that selected suggestions conform to the mask. This approach requires additional development effort to handle and validate user input against the mask. Here's a basic example to illustrate how you might start implementing a custom solution: <div class="component-container"> <h5> MaskedTextBox with Custom Autocomplete </h5> <TelerikMaskedTextBox Value="@TextValue" ValueChanged="@HandleInput" Mask="0000-0000-0000-0000" Width="300px"> <MaskedTextBoxSuffixTemplate> <TelerikSvgIcon Icon="@SvgIcon.Eye" /> </MaskedTextBoxSuffixTemplate> </TelerikMaskedTextBox> <!-- Custom autocomplete suggestions logic here --> </div> @code {
private string TextValue { get; set; }

private void HandleInput(string newVal)
{
// Implement custom autocomplete logic here
}
} For more information on managing autocomplete attributes, you can refer to the following resource: [https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete) Kind Regards, Hristian
