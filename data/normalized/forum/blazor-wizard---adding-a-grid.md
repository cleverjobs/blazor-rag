# Blazor Wizard - Adding a Grid

## Question

**Geo** asked on 29 Sep 2022

Is it possible to add the Grid control or a component with a grid to one of the forms within a Blazor Wizard?

## Answer

**George** answered on 29 Sep 2022

I may have answered my own question after doing some research. I think using a Form Template might do the trick, I haven't tried it yet but I found this information to do it. [https://docs.telerik.com/blazor-ui/components/form/formitems/template#use-the-template-to-provide-custom-editors](https://docs.telerik.com/blazor-ui/components/form/formitems/template#use-the-template-to-provide-custom-editors)

### Response

**George** commented on 30 Sep 2022

My developer tried to add the Grid to the form template within a Wizard and it still didn't work. Anyone have any luck?

### Response

**Dimo** commented on 03 Oct 2022

@George - here is a simple test page with a Grid inside a Form inside a Wizard. In general, you can nest any component in any component, as long as there is a suitable exposed template or content tag (i.e. Blazor RenderFragment ). What exactly seems to be the problem in your scenario? Saying that something "doesn't work" may not be actionable for the other forum users or technical support.

### Response

**George** commented on 03 Oct 2022

@Dimo. This should work! I'll share this with my developer, I'm not directly working on it. Thank you for the reply.
