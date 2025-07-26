# Having an edit filed with format currency and Hint?

## Question

**imw** asked on 09 Feb 2022

Am I correct that it is currently not possible to have a form field that is both formatted as currency and has a hint text? In order to format as anything, it seems we need to use templates, and if we do, the stuff like HintText, Labeltext etc also goes missing? Having to always use templates for most basic stuff in grids, forms etc. like getting a bool to show up as a checkbox or a simple int to be displayed as currency, is really starting to get to me to be honest...

## Answer

**Dimo** answered on 13 Feb 2022

Hi Patrick, Yes, that is correct. On one hand, the Hint attribute relies on our built-in rendering. On the other hand, the FormItem <Template> allows full customization of the rendering. As a result, the two properties are mutually exclusive. Perhaps we might support the DisplayFormatAttribute, so that the model property configuration is able to control the FormItem behavior. If you think this approach can be beneficial for you, we may consider this as a feature request. Regards, Dimo

### Response

**imwise** commented on 15 Feb 2022

Hi, Does this also mean that it is impossible for format the text in form item to something like 0:C and still have a hint, as the Telerik Blazor form does not seem to support formatting so you have to use a template for each field and then the ability to use hint goes away as well?

### Response

**Dimo** commented on 15 Feb 2022

I am not sure what is the difference between... " it is currently not possible to have a form field that is both formatted as currency and has a hint text " " it is impossible for format the text in form item to something like 0:C and still have a hint " Both statements sound the same to me, but they are both correct.

### Response

**imwise** commented on 15 Feb 2022

Sorry, was a bit unclear, even if we disregard the Hint problem, how would be format the contents of a Form item to something like 0:C without using templates? The Model is decorated as it should with [DisplayFormat(DataFormatString="{0:C}")] but that does not seem to make a difference.

### Response

**Dimo** commented on 15 Feb 2022

Yes, this will not work now, but that was my suggestion above - if we log built-in DisplayFormat support as a feature request and implement it, there will be no need for a FormItem template, and Hints will work too.
