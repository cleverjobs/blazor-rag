# Activate or deactivate a Telerik Button

## Question

**Jav** asked on 16 Mar 2021

I need to activate or deactivate a Telerik Button depending on the content of a Telerik textbox.

## Answer

**Svetoslav Dimitrov** answered on 16 Mar 2021

Hello Javier, You can use the Enabled parameter of the TelerikButton and set it to false based on the value of the TextBox. Below, I have added a basic example of this. You can use it as a base and extend it in your application. Code snippet: <TelerikTextBox @bind-Value="@TextBoxValue"> </TelerikTextBox> <TelerikButton Enabled="@( TextBoxValue==" Test " ? false: true )"> Type Test to disable the button </TelerikButton> @code {
private string TextBoxValue { get; set; }
} I hope this helps you move forward with your application. Regards, Svetoslav Dimitrov
