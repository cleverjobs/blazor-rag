# Custom Layout for Form

## Question

**Joh** asked on 25 Jun 2021

I am using a Grid and Popup for the EditMode. I wanted to use a custom form for the popup to add/edit or View the line item details. So far, I have a command column, command buttons. The form I have is somewhat large so I am using a TabStrip to break the form into "sections". Also I do not use a strict column layout. Is this something that can be done? As an alternative, I can navigate away for a detail page. But I'd like to return to the same spot when I close the detail page. I would think I'm not the first one with a requirement like this. Can I use TabStrip inside the Popup form? Can I have more control over placement of fields inside the form? Is there a way to "return" to the same place in the grid if I have to navigate away? Thanks, John

## Answer

**Marin Bratanov** answered on 26 Jun 2021

Hello John, The following sample project shows how to build a custom popup form for the grid so you can implement the desired functionality and layout in it: [https://github.com/telerik/blazor-ui/tree/master/grid/custom-popup-form.](https://github.com/telerik/blazor-ui/tree/master/grid/custom-popup-form.) Whether that layout will be done with the TelerikForm, or with your own form, layout and code is something you are free to choose - you can select the option that best fits your needs. The pointer I can offer with regard to the Telerik Form is that is is great for basic cases - it can generate the entire form for you with a few lines of code based on your model, but if you want to implement customizations that are not part of its built-in layout logic, it may be easier to do so with the standard EditForm. The Telerik inputs and validation messages components work with both. As for going back in the grid where you left off - you can do so with its state, you can see examples here and here. Regards, Marin Bratanov Progress Telerik

### Response

**John** commented on 26 Jun 2021

Thanks, those samples are going to be a major help.
