# <TelerikButton Icon ="calendar" - calendar does not exist in the current context

## Question

**Kar** asked on 28 Aug 2023

<div class="btn-toolbar mb-2 mb-md-0"> <div class="btn-group mr-2"> <TelerikButton Icon="Calendar" Primary="true" OnClick="@(_=> DateRangeFilter(3))">3 Months</TelerikButton> Icon="Calendar" Primary="true" - both of the properties tell it does not exist in the current context.

## Answer

**Georgi** answered on 30 Aug 2023

Hello, Karthik, Based on the Button configuration, I understand you might be upgrading from an older version. There were breaking changes to the Icons in version 4.0.0. Due to this, currently, the Icon parameter accepts a member of the FontIcon enum or a property of the static SvgIcon class and it is set like this: <TelerikButton Icon="@FontIcon.Calendar"> Font Icon </TelerikButton> <TelerikButton Icon="@SvgIcon.Calendar"> SVG Icon </TelerikButton> Additionally, the IconClass was removed in version 4.0.0. Currently, to use a custom icon, you can create a CSS class and then pass it to the Icon parameter: <style>. my-icon { /* define a background image or a custom font icon here */ background: purple; /* dimensions and other base styles will usually come from another class */ width: 1em; height: 1em; font-size: 16px;
} </style> <TelerikButton Icon="@( " my-icon " )"> Custom Icon </TelerikButton> Lastly, due to the breaking changes in 3.0.0, the Primary parameter was removed in favour of ThemeColor of type string. You can use the old primary Button styling like this: <TelerikButton Icon="@SvgIcon.Calendar" ThemeColor="primary"> 3 Months </TelerikButton> Let me know if additional assistance is required. Regards, Georgi Progress Telerik
