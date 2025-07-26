# Panelbar ContentTemplate

## Question

**Ner** asked on 07 Jul 2021

Can i use Panelbar ContentTemplate as a dynamic template in a view? Example: i want different ContentTemplate to render depending on a property.value? code is from Telerik's own example with my addition <TelerikPanelBar Data="@FlatData" @bind-ExpandedItems="@ExpandedItems"> <PanelBarBindings> <PanelBarBinding> @{ var _c=context as object

@if(_c.GetType()=Type)
{ <ContentTemplate> <div class="panelbar-template"> <h2 class="k-text-primary"> Custom Template: </h2> @(((PanelBarItem)context).Text) </div> </ContentTemplate> }
else
{ <ContentTemplate> <div class="panelbar-template"> <h2 class="k-text-primary"> Custom Template 2: </h2> @(((PanelBarItem)context).Text) </div> </ContentTemplate> }
} <HeaderTemplate> <strong> @(((PanelBarItem)context).Text.ToUpper()) </strong> </HeaderTemplate> </PanelBarBinding> </PanelBarBindings> </TelerikPanelBar>

## Answer

**Marin Bratanov** answered on 07 Jul 2021

Hi, You can declare the RenderFragment that is the template in the C# code so you can reuse it more easily and to choose what to render programmatically, in case conditional markup is not enough for your case. You can find a very similar example in this article: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-dynamic-column-template.](https://docs.telerik.com/blazor-ui/knowledge-base/grid-dynamic-column-template.) You can also consider putting a component that will make those decisions in the template instead of solving this at the panelbar level. Regards, Marin Bratanov Progress Telerik

### Response

**Nerf herder** commented on 08 Jul 2021

Thank you for the pin point! However i cant find that panelbar can handle Template as attribute other than the element ContentTemplate and HeaderTemplate. I think ill just have to handle it without involving Templates and just load different views a.k.a components.

### Response

**Marin Bratanov** commented on 08 Jul 2021

Nested tags and templates are basically parameters on their parent component, so you can use them as such:
