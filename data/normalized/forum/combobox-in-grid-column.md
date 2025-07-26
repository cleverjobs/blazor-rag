# Combobox in Grid Column

## Question

**Mic** asked on 24 Mar 2020

Hey everyone! I'm currently focusing a lot on creating components and pages with the help of Telerik Blazor UI. One problem/question that poped-up recently is the following : I've been trying to include a Telerik Combobox inside a grid to limit the user to a set of values when creating a new row. I've been trying to do so with the Template component like the following : <GridColumn Field="@nameof(ConfigDefinitionsPatins.Face)" Title="Face"> <Template Context="ctxPatin"> @{ var patin=ctxPatin as ConfigDefinitionsPatins; <TelerikComboBox Value="patin.Face" Data="patin.Face" Placeholder="Sur le ..." TextField="@nameof(ConfigDefinitionsPatins.Face)" Id="face"> </TelerikComboBox> } </Template> </GridColumn But here's the result comes out negative. You can have a look at the attached file. What am I doing wrong? Thanks in advance and stay safe!

## Answer

**Svetoslav Dimitrov** answered on 24 Mar 2020

Hello Michael, From what I can see the Value and the Data are bound to the same property. However, the Data should be a collection of elements (array, List and etc.) whereas the Value can should be a number (int, double and so on), Guid, string or Enum. More information on the ComboBox can be found: In the documentation: [https://docs.telerik.com/blazor-ui/components/combobox/overview](https://docs.telerik.com/blazor-ui/components/combobox/overview) Live demos: [https://demos.telerik.com/blazor-ui/combobox/overview](https://demos.telerik.com/blazor-ui/combobox/overview) The next thing is that you need to use EditorTemplate. When you add a new row into the Grid it is in Edit mode, hence, using the EditorTemplate rather than Template. More information on the EditorTemplate can be found here: [https://docs.telerik.com/blazor-ui/components/grid/templates#edit-template](https://docs.telerik.com/blazor-ui/components/grid/templates#edit-template) Regards, Svetoslav Dimitrov

### Response

**Michael** answered on 24 Mar 2020

Here's what i'm trying : <GridColumn Field="@nameof(ConfigDefinitionsPatins.Face)" Title="Face"> <EditorTemplate Context="ctxPatin"> @{ var patin=ctxPatin as ConfigDefinitionsPatins; <TelerikComboBox Value="patin.Face" Data="@faces" Placeholder="Sur le ..." TextField="@nameof(ConfigDefinitionsPatins.Face)" Id="face" /> } </EditorTemplate> </GridColumn> @code { public List<ConfigDefinitionsEdgeBender> definitionsEdgeBenders=new List<ConfigDefinitionsEdgeBender>(); public enum faces { Dessus,Dessous} ; I get the error DefinitionsPatins.faces is a type, which is not valid in the given context

### Response

**Michael** answered on 24 Mar 2020

I found this post : [https://docs.telerik.com/blazor-ui/knowledge-base/dropdown-kb-bind-to-enum](https://docs.telerik.com/blazor-ui/knowledge-base/dropdown-kb-bind-to-enum) I've tried it and it works like a charm.

### Response

**Svetoslav Dimitrov** answered on 25 Mar 2020

Hello Michael, I am glad to hear you found a solution to what you encountered in our Knowledge Base. Regards, Svetoslav Dimitrov
