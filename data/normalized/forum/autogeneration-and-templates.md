# AutoGeneration And Templates

## Question

**Tim** asked on 09 Apr 2021

Is it possible to use both Auto Generation ([https://demos.telerik.com/blazor-ui/form/auto-generated)](https://demos.telerik.com/blazor-ui/form/auto-generated)) and Templates ([https://demos.telerik.com/blazor-ui/form/templates)?](https://demos.telerik.com/blazor-ui/form/templates)?) In other words, specify the template for a couple of items and let it autogenerate the rest? This would be incredibly useful for handling situations like dropdown that need external data.

## Answer

**Marin Bratanov** answered on 09 Apr 2021

Hello Timothy, Fully automatic generation requires that you do not use templates. Once you start defining your own items in the form, you must define all of them. You could use reflection to get all the fields and define a simple FormItem for each, and then add a template only when needed, but you would still have to define the form yourself. Regards, Marin Bratanov
