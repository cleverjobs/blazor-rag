# Blazor TelerikButton text always is upper-case?

## Question

**Jus** asked on 07 Dec 2021

<TelerikButton>Hello</TelerikButton> generates a button with "HELLO" as the text...all uppercase. Looks like the .k-button css class has "text-transform: uppercase" on it. Is this due to the Material theme? I am using Telerik.UI.for.Blazor.2.29.0, which is the latest as of this writing. I would like the casing of the text to be how I decide. Thanks, Justin

### Response

**Apostolos** commented on 08 Dec 2021

Hi Justin, You are correct, the style is specific to our Material theme. This theme follows the guidelines of Material Angular design. Regards, Apostolos

## Answer

**Matthias** answered on 08 Dec 2021

Hi Justin, yes, this is due to the material theme. But you can easily change it without changing the theme: .k-button-text { text-transform: lowercase; text-transform: capitalize;
} regards Matthias
