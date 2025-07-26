# Automatic form builder

## Question

**Bla** asked on 11 Mar 2022

Hello! I am wondering if the new FormEditorType approach for automatic form generation could be extended in order to support more input types like ColorPicker for example? Thanks.

### Response

**Dimo** commented on 16 Mar 2022

Theoretically, it's possible, but all the ColorPicker settings will be inaccessible. This may be a blocker and developers will still resort to a form item template.

### Response

**Blazorist** commented on 18 Mar 2022

@Dimo, I'm working over the RenderTreeBuilder creating the form items based on the viewmodel dataannotations. In some cases I taking advantage of the autogeneration properties provided by Telerik and in other cases creating the formitem from the scratch. I'm hoping to get an extensible auto-generated form with many kinds of input types and editors to avoid repetitive tasks every time I need a form.
