# Formatting guide for NumericTextBox

## Question

**Chr** asked on 09 Nov 2023

The custom format optin in NumericTextBox is pretty useful, but I could not see any clear documentation. It links to the dotnet format guide, but also works with #s? E.g. missing 0s i logged this (and then answered it myself) NumericTextBox with a format field does not display the digit '0' in UI for Blazor | Telerik Forums "# unit(s)" works, but "there is # unit(s)" does not Apologies if there is such a documentation and i missed it!

## Answer

**Dimo** answered on 13 Nov 2023

Hi Chris, The NumericTextBox simply calls Value.ToString(Format, CultureInfo.CurrentCulture). As a result: The observed behavior is a direct result of the standard .NET behavior with regard to 0 and #. We have linked the .NET documentation at NumericTextBox Parameters, but let us know if you think we need to clarify something better. By the way, please ask the license holder at your company to assign you as a license developer. This will ensure that your account is in good standing and compliant with our license agreement. ToString("there are #.# units") behavior <br /> <br /> 2.5: @TwoHalf.ToString("there are #.# units") <br /> 2: @Two.ToString("there are #.# units") <br /> 0: @Zero.ToString("there are #.# units") <br /> <br /> ToString("there are 0.## units") behavior <br /> <br /> 2.5: @TwoHalf.ToString("there are 0.## units") <br /> 2: @Two.ToString("there are 0.## units") <br /> 0: @Zero.ToString("there are 0.## units")

@code {
int NumValue { get; set; }=2;

const decimal TwoHalf=2.5m;
const int Two=2;
const int Zero=0;
} Regards, Dimo Progress Telerik
