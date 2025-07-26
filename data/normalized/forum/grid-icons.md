# Grid Icons

## Question

**Sco** asked on 25 Aug 2020

How do we change the icons used by the filter mode on the Blazor Grid? For example the calendar and filter icon I have shown in my attachment are using Telerik Icons but we want to use Office UI Fabric Icons to match the rest of the site.

## Answer

**Marin Bratanov** answered on 26 Aug 2020

Hello Scott, One way would be to inspect the rendered HTML and devise CSS rules in your app that override the built-in icons with other icons. I made a sample for you that shows the general concept and it is attached at the end of this post. Another would be to use the filter template to implement your own code, styling and filtering logic. Regards, Marin Bratanov

### Response

**Scott** answered on 27 Aug 2020

Thanks. The CSS styling is good answer.
