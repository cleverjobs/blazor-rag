# Deselecting/Clearing TelerikRadioGroup item by clicking on "Same" selected value

## Question

**JimJim** asked on 09 Jan 2025

I am trying to clear all selected values from a TelerikRadioGroup. I would like to do this by clicking on the selected value. The problem is the OnChange and the ValueChanged does not fire unless you are clicking on a different value. <TelerikRadioGroup Data="@genderOptions" Value="@selectedGender" OnChange="@OnChangeHandler" ValueChanged="@((int newValue)=> OnGenderChanged(newValue))" ValueField="@nameof(GenderModel.GenderId)" TextField="@nameof(GenderModel.GenderText)" Layout="RadioGroupLayout.Horizontal"> </TelerikRadioGroup> @code { private int selectedGender; private void OnGenderChanged(int newValue) { if (selectedGender==newValue) { var aa=123; } else { selectedGender=newValue; Console.WriteLine($"Gender changed to: {newValue}"); } } async Task OnChangeHandler(object newValue) { // the handler receives an object that you may need to cast to the type of the component // if you do not provide a Value, you must provide the Type parameter to the component Console.WriteLine($"ValueChanged fired with value: {newValue as string}"); } }

## Answer

**Hristian Stefanov** answered on 10 Jan 2025

Hi Jim, Indeed, the ValueChanged and OnChanged events do not fire when an already selected value is chosen again, as deselecting is not supported. Our TelerikRadioGroup component is based on standard HTML radio groups, and in standard HTML, radio buttons do not natively support deselecting an already selected option. This is the nature of the radio buttons. Radio buttons are designed to allow the selection of one option from a group, with the expectation that one option will always remain selected (or none initially). If you require functionality where clicking an already selected radio button deselects it—enabling a null or "no selection" state—you would need to implement some custom logic using JavaScript that listens for a click on the separate radio buttons. Additionally, if you are interested, here is another article I found on the internet regarding this topic: " Why is it impossible to deselect HTML "radio" inputs? ". Regards, Hristian Stefanov Progress Telerik
