# Is there not a simple way to place the grid in a readonly state?

## Question

**Jef** asked on 20 May 2021

Maybe I'm missing something but I'm not seeing an EditMode=@GridEditMode.None or maybe an Editable=False option. How can I quickly set my data grid into a readonly mode? I realize I can add the "disabled" attribute to the containing <div> element but that disables scrolling and paging through the data.

## Answer

**Marin Bratanov** answered on 20 May 2021

Hello Jeffrey, The default edit mode is Inline, so if you have no command buttons, the user won't be able to edit. You can, for example, put them in conditional markup based on your flag. An alternative is to cancel the OnEdit event based on that flag if you want to keep the buttons. You can also do both at the same time, depending on the UX you want your users to have. Regards, Marin Bratanov Progress Telerik
