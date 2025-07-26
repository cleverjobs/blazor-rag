# NumericTextBox decimal separator

## Question

**Rob** asked on 25 Oct 2019

There is a note on the documentation page for NumericTextBox saying "The decimal separator is . for the time being. When localization features get implemented in the Telerik UI for Blazor suite... Currency symbols are also rendered by the framework and they come from the current culture as well." Is that note still relevant? I made a simple test.. <TelerikNumericTextBox @bind-Value="Number" Format="C"></TelerikNumericTextBox> @code { public decimal Number { get; set; }=(decimal)2.59; protected override void OnInitialized() { System.Globalization.CultureInfo.DefaultThreadCurrentCulture=new System.Globalization.CultureInfo("hr-HR"); } } The numer in numeric text box is displayed as expected - "2,59 kn" (Notice that it has the correct decimal separator and currency simbol) When I want to change the number I cannot input "," (comma) as a decimal separator - numericTextBox won't accept it. So I tried with "." (dot). I can input "." (dot) but when I enter a number after "." the "." disappears leaving me with an whole number in numericTextBox. Is this a bug or a missing feature? The note above is confusing because NumericTextBox get's it's formating options from current culture so why doesn't it apply the correct decimal separator? Thank you

## Answer

**Marin Bratanov** answered on 25 Oct 2019

Hello Robert, The shortest answer is "it's a missing feature". The information in the docs is still true, we have not gotten to implementing localization and globalization yet. You can track this particular feature here: [https://feedback.telerik.com/blazor/1433191-numeric-text-box-not-working-correctly-when-running-under-a-different-locale.](https://feedback.telerik.com/blazor/1433191-numeric-text-box-not-working-correctly-when-running-under-a-different-locale.) The component is an actual <input type=text> under the covers so it can render decimal and thousands separators, and custom symbols/formats. The initial string value is correct because .NET's .ToString(theCustomFormat) is used and it works. We have not yet implemented in our code all the other things that are required to transfer all that ability into client-side user experience (it is not a trivial task). I hope this answers the question in detail. Regards, Marin Bratanov
