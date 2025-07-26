# Gridcolumn with only two decimal places

## Question

**Mir** asked on 17 Jul 2020

Hi, I want to allow the input of a decimal number with exactly two decimal places in one column and in another column a number with three decimal places. How can I implement this in a GridColumn? DataAnnotations does not work. [RegularExpression(@"^\d+\.\d{0,2}$")] [Range(0, 9999999999999999.99)] Thanks in advance

## Answer

**Marin Bratanov** answered on 17 Jul 2020

Hi Miriam, Data annotation validation is available for popup editing only. You can read more about this and see workarounds here (feel free to Vote for the edit template and to Follow its implementation if it would suit your needs). As for controlling the decimal places - by default they are two, and you can change them by defining a custom editor with the desired settings (e.g., a TelerikNumericTextbox with 3 decimals). Regards, Marin Bratanov

### Response

**Miriam** answered on 17 Jul 2020

The TelerikNumericTextbox doesn't work with null values: [https://feedback.telerik.com/blazor/1429608-when-bound-to-a-nullable-decimal-the-numerictextbox-is-not-setting-the-decimal-to-null-when-you-clear-the-text-box](https://feedback.telerik.com/blazor/1429608-when-bound-to-a-nullable-decimal-the-numerictextbox-is-not-setting-the-decimal-to-null-when-you-clear-the-text-box) I always get that exception.

### Response

**Marin Bratanov** answered on 17 Jul 2020

Hello Miriam, This issue was fixed in 2.0.0 in September 2019. Could you try upgrading to the latest (2.15.0 at the moment) to see how things go? I'm also attaching here a simple project where the numeric textbox works as expected. Does that work for you too? Regards, Marin Bratanov
