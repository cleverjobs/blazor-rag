# How to format headings in a TelerikForm on a Blazor razor page?

## Question

**Dav** asked on 13 Jun 2022

I have Blazor razor page with a TelerikForm. The form has a variety of form items in various groups. Q How can I forrmat the group headings; specifically set them to bold and to set the color? I guess that something needs to be added to: <FormGroup LabelText="Form Heading" Columns="2" ColumnSpacing="15px"> or something in <TelerikForm EditContext="@EditContext" Orientation="@FormOrientation" OnValidSubmit="@HandleValidSubmit" OnInvalidSubmit="@HandleInvalidSubmit">

## Answer

**Tsvetomir** answered on 16 Jun 2022

Hi, David, The headers of the form groups can be modified via CSS. A class parameter can be added to the FormGroup. Or, alternatively, you can access them by index (nth-of-child), or by nth-of-type CSS rule. <FormGroup LabelText="Employee Information" Class="my-class">

<style>.my-class,.my-class legend { background-color: aliceblue;
}
</style> Let me know if there is anything else I can help with. Kind regards, Tsvetomir

### Response

**David** commented on 18 Jun 2022

Thanks for the info. I tried: <FormItems> <FormGroup LabelText="Athlete and submitter details" class="my-class" Columns="2" ColumnSpacing="15px"> <style>.my-class,.my-class legend { background-color: aliceblue;
} </style> When I ran the app it failed: Microsoft.AspNetCore.Components.Server.Circuits.RemoteRenderer: Warning: Unhandled exception rendering component: Object of type 'Telerik.Blazor.Components.FormGroup' does not have a property matching the name 'class'. System.InvalidOperationException: Object of type 'Telerik.Blazor.Components.FormGroup' does not have a property matching the name 'class'. PS I tried a caital for class (Class) with same outcome.

### Response

**Tsvetomir** commented on 20 Jun 2022

Hi, David, I apologize for the misinformation. The Class option will be available with the release that is scheduled for this Wednesday (22nd of June). Therefore, currently, the Class is not part of the public API of the component. Also, the style tag should be placed outside of the component since it is a conventional CSS tag rather than an option for the component. The code snippet that I provided earlier was intended to show the configuration for the form and, separately, the CSS snippet. Until the option is released, I can recommend that you access the form groups by index, for instance via nth-child or nth-of-type CSS rules.

### Response

**David** commented on 21 Jun 2022

OK. Thanks for the info. Not "in production" yet. I'll look for an update at the end of the month and use the class option.

### Response

**Tsvetomir** commented on 22 Jun 2022

Hi David, the 3.4.0 release is now available. Upgrade to the latest version and the Class parameter should be available.

### Response

**David** commented on 23 Jun 2022

I upgraded from V2.x to 3.4.0 I then appropiately added: <style> body { background-color: beige;
}.my-form-group-class { color: purple; font-style: normal; font-weight: bold; font-size: medium;
}.my-form-group-class legend { color: green; font-style: italic; font-weight: bold; font-size: larger;
}
</style> The background is for whole page. And then in the Form: <FormItems> <FormGroup LabelText="Athlete and submitter details" Class="my-form-group-class" Columns="2" ColumnSpacing="15px"> The only thing that doesn't work is the legend color. It is always black. The headings in the rest of the Form Group are purple. See legend.png

### Response

**Tsvetomir** commented on 24 Jun 2022

Hi David, The CSS specificity for the legend's color is stronger than the selector that you have declared. Therefore, the default color will be taken into account. Increasing the specificity will apply the coloring accordingly: <style>.k-form.my-class legend { color: red;
}
</style>
