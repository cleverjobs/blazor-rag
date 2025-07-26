# Errors when switching from version 2.24.1 to version 2.25.0

## Question

**Yur** asked on 25 Jun 2021

There are no errors in 2.24.1 In 2.25.0 I got 3 identical errors without specifying the source module RZ9999 The child content element " ChildContent "of the" GridCommandColumn"component uses the same parameter name ("context") as the enclosing child content element" Detailed table "of the"TelerikGrid" component. Specify a parameter name, for example: '<ChildContent context="other name"> to resolve the ambiguity of SparDeckMasterWeb D:\TutorialSparDeck\SparDeckMasterWebDevOption\SparDeckMasterWeb\RAZORGENERATE 1

## Answer

**Marin Bratanov** answered on 27 Jun 2021

Hello Yuri, As of 2.25.0, the Grid Command Column has a context parameter that provides you with the row it is bound to (enhancement request here, docs here ), which means that it now has an implicit "context" variable. If it is in a parent element that also has an unnamed (implicit) "context" variable, such a clash will occur. This happens with all nested Blazor render fragments that have unnamed context variables. The solution is to name the context variables, you can read more about this and find some similar examples here: [https://docs.telerik.com/blazor-ui/knowledge-base/nest-render-fragment.](https://docs.telerik.com/blazor-ui/knowledge-base/nest-render-fragment.) Regards, Marin Bratanov Progress Telerik
