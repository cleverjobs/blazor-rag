# Enable TextBox based on CheckBox value

## Question

**Jon** asked on 02 May 2020

Hi How do I disable / enable a Telerik TextBox based on the value of CheckBox - and when the value changes? Use ValueChanged? How do I reference my TextBox 'WaterNotes" control? <TelerikCheckBox ValueChanged="@((bool value)=> ValueChanged(value))" id="water" class="form-control" style="width: 50px;" Value="Customer.Water" /> <ITelerikTextBoxid="WaterNotes" class="form-control" style="height: 40px;" Value="Customer.WaterNotes" /> private void ValueChangedWaterSink(bool value) { if (value) ??????? } Thx Again

## Answer

**Svetoslav Dimitrov** answered on 04 May 2020

Hello Jonathan, You can use the @bind-Value (two-way data binding) for the TelerikCheckBox and bind the Enabled parameter of the TelerikTextBox to the same bool variable. I have made a small code snippet to illustrate that: <p> <label for="toggleTextbox"> Enable/Disable Texbox </label> <TelerikCheckBox Id="toggleTextbox" @bind-Value="isEnabled"> </TelerikCheckBox> </p> <TelerikTextBox @bind-Value="userInput" Enabled="isEnabled"> </TelerikTextBox> @if (!String.IsNullOrEmpty(userInput))
{ <p> The user input is: <strong> @userInput </strong> </p> }

@code {
public bool isEnabled { get; set; }
public string userInput { get; set; }=String.Empty;
} Regards Svetoslav Dimitrov

### Response

**Jonathan** answered on 06 May 2020

thx again!
