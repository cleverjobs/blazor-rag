# Grid copying data for edit

## Question

**Mic** asked on 04 Oct 2022

I have found that when the telerik grid creates a copy of my data for the editor, it doesn't correctly copy every field from the original object. I'm able to work around this by hooking into the state changed event and then using our own methods to copy properties from the original, but I'd like to know why it's not working by default. I found a related post about a similar problem: [https://www.telerik.com/forums/blazor-telerikgrid-editor-template-copy.](https://www.telerik.com/forums/blazor-telerikgrid-editor-template-copy.) However when I tried using the code posted there, it worked correctly and all my properties were copied into the cloned new instance. Has the logic for creating a clone changed since that forum post?

## Answer

**Dimo** answered on 07 Oct 2022

Hello Michael, There is one change in our cloning code since June 2021. It's from Sept 1, 2021 in ClonePropertiesFrom: (the red line was replaced by the two green lines) // skip props with IgnoreDataMemberAttribute because of the ef core lazy loading if (originalProp.CanWrite && originalProp.CustomAttributes.All(a=> a.AttributeType !=typeof (IgnoreDataMemberAttribute)))
{ originalProp.SetValue(target, originalProp.GetValue(item)?.Clone()); var propValue=item.GetPropertyValue(originalProp.Name);
originalProp.SetValue(target, propValue?.Clone()); } If this change broke your Grid, this would mean that it has worked until version 2.26 and not worked from 2.27 onwards. Can you confirm this? Can you provide a simple test page with dummy data, so that we can inspect your model class definition? Regards, Dimo
