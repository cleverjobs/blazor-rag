# All my controls have been resized with the new release!

## Question

**Jas** asked on 19 Nov 2021

I just updated Telerik and found that all the controls (TelerikTextBox, TelerikDropDownList) have been resized, mainly the height. I can't tell exactly what Telerik changed. I'm using Bootstrap, so I'd like to use those sizes, but Telerik seems to override Bootstrap. Is there a new way to make the controls the same size and the smallest possible? This is generally what I need to work, otherwise I'll have to go back to using InputText <TelerikTextBox Class="form-control form-control-sm">

## Answer

**Dimo** answered on 22 Nov 2021

Hi Jason, So far our components worked well with Bootstrap CSS classes, because our themes contained workarounds for the integration issues that have existed from day one. Recently we removed these workarounds. Here are two public pages, which discuss the changes, why we made them, and possible next steps. [https://www.telerik.com/forums/2-26-bootstrap-theme-missing-k-widget-form-control-padding-override](https://www.telerik.com/forums/2-26-bootstrap-theme-missing-k-widget-form-control-padding-override) [https://feedback.telerik.com/blazor/1532209-upgrade-from-2-25-0-to-2-26-0-combobox-appears-doubled-up-using-bootstrap-theme](https://feedback.telerik.com/blazor/1532209-upgrade-from-2-25-0-to-2-26-0-combobox-appears-doubled-up-using-bootstrap-theme) Our primary recommendation is to not use the Bootstrap form-control CSS class with our components anymore. Depending on the specific use case and overall HTML markup of your app, there may be different options to proceed in the best way. Surely, you can restore the previous looks if you add a few CSS rules to fix the issues, as shown below. However, the amount of required code will depend on how much flexibility you need. The rule of thumb for ComboBoxes and DropDownLists is to remove the padding and border styles from the component element and "transfer" the paddings to the inner.k-input element. <TelerikTextBox @bind-Value="@Value" Class="form-control form-control-sm" /> <TelerikDropDownList @bind-Value="@Value" Data="@Data" Class="form-control form-control-sm" /> <TelerikDropDownList @bind-Value="@Value" Data="@Data" /> <TelerikComboBox @bind-Value="@Value" Data="@Data" Class="form-control form-control-sm" /> <TelerikComboBox @bind-Value="@Value" Data="@Data" /> <style> /* textbox */ input.form-control-sm, /* combobox, dropdownlist */.k-widget.form-control-sm { font-size: . 875em; border-radius: . 2rem;
} input.form-control-sm,.form-control-sm.k-input { padding: . 25rem. 5rem; height: auto;
}.k-widget.form-control:not(.k-textbox) { padding: 0; border: 0;
} input.form-control-sm { min-height: calc ( 1.5em + . 5rem + 2px );
} /* needed only in this example to display all components on a single row */.form-control { display: inline-block!important; width: 200px!important;
} </style> @code {
string Value { get; set; }="foo";
List<string> Data { get; set; }=new () { "foo", "bar" };
} Regards, Dimo

### Response

**Jason** commented on 22 Nov 2021

Thank you for this. I read the release notes, but none of this was in there. I rolled back to the old version until I can fix this. You have to understand that Bootstrap is more valuable to me than Telerik. Since I'm not a true designer and all I'm creating are business apps, Bootstrap gives me all the design I need and it just works. Telerik is making that harder not easier. If you are going to break form-control-sm, I need a Telerik equivalent.

### Response

**Dimo** commented on 23 Nov 2021

Hi Jason, Indeed, I understand that developers rely on our Blazor library for building layouts and that is why we provide tools for that. In early 2022 we also plan to introduce our own sizing mechanism, which will allow you to set small / medium / large sizes to input components.
