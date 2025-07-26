# Using both '.' and ',' as decimal separators in a NumericTextBox

## Question

**Joh** asked on 29 Apr 2021

Hello, I am using a NumericTextBox in a form to input a decimal number. The only decimal-separating character is " , ". I would like to be able to also use ' . ' as it's commonly used and easier to access on the keyboard while using the numeric pad. The component doesn't seem to allow me to set which separator is used. The only information I have found is that it's fully dependant on the app's culture. Our culture is set to French (France), which uses ' , ' as a separator, so it's the only symbol the component will allow. Is there any way to allow multiple decimal separators without changing the entire app's culture? (Even in this case I don't know if that would enable me to use both commas and dots) Thank you, Johnny

### Response

**Juan Angel** commented on 20 Nov 2021

If you are reading this, it means that your users have already complained that they cannot use the "NumpadDecimal" key as in Excel or accounting applications for example, which make intensive use of decimal values. They also cannot copy and paste decimal values from other applications. I have tried to explain the magnitude of the problem to the support department and they have opened a feature request: [https://feedback.telerik.com/blazor/1541217-numpad-delimiter-character-should-input-a-delimiter-based-on-the-culture](https://feedback.telerik.com/blazor/1541217-numpad-delimiter-character-should-input-a-delimiter-based-on-the-culture) If you need this feature, please vote for it to get it to production as soon as possible. For my users (and some others, see wikipedia attachment ) it is a must. It is simply unacceptable to them that the "NumpadDecimal" key behaves different in Excel and accounting applications than in a Blazor application, in addition to the impossibility to copy and paste. The possibility of making serious mistakes is extremely high when entering decimal values: "1.000 €" in Spanish=1000 € "1.000 €" in English=1 € "1.000 V" in Spanish=1000 Volts "1.000 V" in English=1 Volt "1.000 kg of TNT" in Spanish=1000 kg of TNT "1.000 kg of TNT" in English=1 kg of TNT Thanks.

## Answer

**Marin Bratanov** answered on 30 Apr 2021

Hello Johnny, The .NET framework usually has correct decimal and thousands separators according to the culture and keyboard layouts it uses. Nevertheless, you can consider changing the decimal separator of the culture your app uses if the default one does not suit your needs. The Telerik component needs to take that information from the app, because this is the only place it can take such information from. Adding settings per component will result in massive api bloat, a performance hit, and is highly likely to introduce bugs. Moreover, two decimal separators cannot be used at the same time because: it will break the .NET parsing (the numeric textbox needs to have a string representation of the value that can be converted to the number back and forth, and we rely on the framework methods to do that) it will cause invalid data input and issues because there are many culture where a decimal and a thousand separator are both used, and they are always a dot (".") and a comma (","), with the only variation being which is a decimal separator and which is a thousand separator. Thus, they cannot be mixed together to serve only one purpose. Regards, Marin Bratanov

### Response

**Juan Angel** commented on 07 Oct 2021

We are Spanish and we have the same problem. The "dot" key on the numeric keypad is commonly used as a "decimal separator". This is the behaviour of Excel for example in Spanish language. It is a big accessibility problem that the "NumpadDecimal" key enters a "." instead of "local decimal separator", "Comma" in Spanish in other languages. I've tried a workaround capturing @onkeypress from a container div, but I can't replace "." by ",". <div @onkeypress="ntb_KeyPress" @onkeypress:preventDefault="false"> <TelerikNumericTextBox Value="22" /> </div> public void ntb_KeyPress ( KeyboardEventArgs e ) { if (e.Code=="NumpadDecimal" )
{
e.Key=",";
e.Code="Comma";
}
} Seriously consider implementing this feature. It's a big accessibility problem for any language where "." is not the decimal separator.

### Response

**Marin Bratanov** commented on 09 Oct 2021

This sounds like an issue with the keyboard layout that is being used and as such it is part of the OS, and not something a web application (or a component from a web application) can influence. We must use the decimal and thousands separators that come with the .NET framework, and so if your users are having an issue with that, I recommend you change them in the culture settings of your app, as this issue will manifest elsewhere as well, not just with Telerik inputs.
